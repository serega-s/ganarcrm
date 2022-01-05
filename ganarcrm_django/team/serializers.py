from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Plan, Team

User = get_user_model()


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            "id",
            "name",
            "max_leads",
            "max_clients",
            "price"
        )


class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "members",
            'created_by',
            'plan_end_date',
            "plan"
        )
