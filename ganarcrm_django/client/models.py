from django.contrib.auth import get_user_model
from django.db import models
from team.models import Team

User = get_user_model()


class Client(models.Model):
    team = models.ForeignKey(Team, related_name='clients',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name="clients", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    created_by = models.ForeignKey(
        User, related_name="notes", on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='notes',
                             on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, related_name="notes", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
