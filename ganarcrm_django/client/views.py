from django.http.response import Http404

from rest_framework import filters, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from team.models import Team
from lead.models import Lead
from .models import Client, Note
from .serializers import ClientSerializer, NoteSerializer


class ClientPagination(PageNumberPagination):
    """Pagination class for client queryset
    """
    page_size = 10


class ClientViewSet(viewsets.ModelViewSet):
    """CRUD for clients
    """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'contact_person')

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(created_by=self.request.user, team=team)


class NoteViewSet(viewsets.ModelViewSet):
    """CRUD for notes
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.GET.get('client_id')

        return self.queryset.filter(team=team).filter(client_id=client_id)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client_id']

        serializer.save(created_by=self.request.user,
                        team=team, client_id=client_id)


@api_view(['POST'])
def convert_lead_to_client(request):
    """Convery lead to client
    """
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']

    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist as e:
        raise Http404 from e

    client = Client.objects.create(team=team, name=lead.company, contact_person=lead.contact_person,
                                   email=lead.email, phone=lead.phone, website=lead.website, created_by=request.user)

    return Response()


@api_view(['POST'])
def delete_client(request, client_id):
    """Delete a client
    """
    team = Team.objects.filter(members__in=[request.user]).first()

    client = team.clients.filter(pk=client_id)
    client.delete()

    return Response({'message': 'The client was deleted!'})
