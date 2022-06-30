from datetime import datetime

import stripe
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserSerializer

from team.services import create_checkout_session

from .models import Plan, Team
from .serializers import TeamSerializer

User = get_user_model()


class TeamViewSet(viewsets.ModelViewSet):
    """CRUD for teams
    """
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        return self.queryset.filter(members__in=[self.request.user]).first()

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user)
        obj.plan = Plan.objects.get(name='Free')
        obj.save()


class UserDetail(APIView):
    """Getting and updating users
    """
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_stripe_pub_key(request):
    """Get Stripe public key
    """
    pub_key = settings.STRIPE_PUB_KEY

    return Response({'pub_key': pub_key})


@api_view(['GET'])
def get_my_team(request):
    """Get my team
    """
    team = Team.objects.filter(members__in=[request.user]).first()
    serializer = TeamSerializer(team)

    return Response(serializer.data)


@api_view(["POST"])
def upgrade_plan(request):
    """Upgrade a team plan
    """
    team = Team.objects.filter(members__in=[request.user]).first()
    plan = request.data['plan']

    if plan == 'free':
        plan = Plan.objects.get(name='Free')
    elif plan == 'smallteam':
        plan = Plan.objects.get(name='Small team')
    elif plan == 'bigteam':
        plan = Plan.objects.get(name='Big team')

    team.plan = plan
    team.save()

    serializer = TeamSerializer(team)

    return Response(serializer.data)


@api_view(['POST'])
def add_member(request):
    """Add member into my team
    """
    team = Team.objects.filter(members__in=[request.user]).first()
    email = request.data['email']

    user = User.objects.get(email=email)

    team.members.add(user)
    team.save()

    return Response({'data': 'Member was added'})


@api_view(['POST'])
def check_session(request):
    """Check a session
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    error = ''
    try:
        team = Team.objects.filter(members__in=[request.user]).first()
        subscription = stripe.Subscription.retrieve(
            team.stripe_subscription_id)
        product = stripe.Product.retrieve(subscription.plan.product)

        team.plan_status = Team.PLAN_ACTIVE
        team.plan_end_date = datetime.fromtimestamp(
            subscription.current_period_end)
        team.plan = Plan.objects.get(name=product.name)
        team.save()

        serializer = TeamSerializer(team)

        return Response(serializer.data)
    except Exception as e:

        return Response({'error': str(e)})


@api_view(['POST'])
def cancel_plan(request):
    """Cancel a current team plan
    """
    team = Team.objects.filter(members__in=[request.user]).first()
    plan_free = Plan.objects.get(name='Free')

    team.plan = plan_free
    team.plan_status = Team.PLAN_CANCELLED
    team.save()

    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.Subscription.delete(team.stripe_subscription_id)
    except Exception:
        return Response({'error': 'Something went wrong. Please try again'})

    serializer = TeamSerializer(team)
    return Response(serializer.data)




@api_view(['POST'])
def create_checkout_session_and_upgrade_plan(request):
    """Create chekcout session and upgrade plan
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = request.data
    plan = data['plan']

    team = Team.objects.filter(members__in=[request.user]).first()

    try:
        if plan == 'smallteam':
            plan = Plan.objects.get(name='Small team')
            price_id = settings.STRIPE_PRICE_ID_SMALL_TEAM
        else:
            plan = Plan.objects.get(name='Big team')
            price_id = settings.STRIPE_PRICE_ID_BIG_TEAM
        checkout_session = create_checkout_session(team, price_id)
        team.plan = plan
        team.save()
        serializer = TeamSerializer(team)

        return Response({'sessionId': checkout_session['id'], **serializer.data})
    except Exception as e:
        return Response({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    """Stripe webhook for accepting payments
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_key = settings.STRIPE_WEBHOOK_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_key
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignaturVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        team = Team.objects.get(pk=session.get('client_reference_id'))
        team.stripe_customer_id = session.get('customer')
        team.stripe_subscription_id = session.get('subscription')
        team.save()

    return HttpResponse(status=200)
