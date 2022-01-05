from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework import filters, viewsets
from django.contrib.auth import get_user_model

from .serializers import LeadSerializer
from .models import Lead
from team.models import Team

User = get_user_model()


class LeadPagination(PageNumberPagination):
    page_size = 2


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    pagination_class = LeadPagination
    filter_backends = (filters.SearchFilter, )
    search_fields = ('company', 'contact_person')

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)

    def perform_update(self, serializer):
        obj = self.get_object()
        member_id = self.request.data['assigned_to']

        if member_id:
            user = User.objects.get(pk=member_id['id'])
            serializer.save(assigned_to=user)
        else:
            serializer.save()

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(created_by=self.request.user, team=team)


@api_view(['POST'])
def delete_lead(request, lead_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    lead = team.leads.filter(pk=lead_id)
    lead.delete()

    return Response({'message': 'The lead was deleted!'})
