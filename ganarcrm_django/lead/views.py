from django.contrib.auth.models import User
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination
from team.models import Team

from .models import Lead
from .serializers import LeadSerializer


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
