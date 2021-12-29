from django.contrib.auth.models import User
from rest_framework import serializers
from team.serializers import UserSerializer

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Lead
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            "id",
            "company",
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'assigned_to',
            'created_at',
            'modified_at',
        )
