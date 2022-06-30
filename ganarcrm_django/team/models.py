from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Plan(models.Model):
    """Plan model
    """
    name = models.CharField(max_length=255)
    max_leads = models.IntegerField(default=5)
    max_clients = models.IntegerField(default=5)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Team(models.Model):
    """Team model
    """
    PLAN_ACTIVE = 'active'
    PLAN_CANCELLED = 'cancelled'

    CHOICES_PLAN_STATUS = (
        (PLAN_ACTIVE, 'Active'),
        (PLAN_CANCELLED, 'Cancelled'),
    )

    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(
        User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    plan = models.ForeignKey(Plan, related_name='teams',
                             on_delete=models.SET_NULL, null=True, blank=True)
    plan_end_date = models.DateTimeField(blank=True, null=True)
    plan_status = models.CharField(
        max_length=20, choices=CHOICES_PLAN_STATUS, default=PLAN_ACTIVE)
    stripe_customer_id = models.CharField(
        max_length=255, blank=True, null=True)
    stripe_subscription_id = models.CharField(
        max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
