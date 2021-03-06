from django.contrib.auth import get_user_model
from django.db import models
from team.models import Team

User = get_user_model()


class Lead(models.Model):
    """Lead model
    """
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'In progress'),
        (LOST, 'Lost'),
        (WON, 'Win')
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    )

    team = models.ForeignKey(Team, related_name='leads',
                             on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=25, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(
        max_length=25, choices=CHOICES_PRIORITY, default=MEDIUM)
    assigned_to = models.ForeignKey(
        User, related_name='assignedleads', blank=True, null=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name="leads", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company
