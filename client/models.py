from http import client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models

from team.models import Team


# Model client
class Client(models.Model):
    team = models.ForeignKey(
        Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})


# Model notes
class Note(models.Model):
    team = models.ForeignKey(Team, related_name='notes',
                             on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, related_name='notes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='notes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse("Lead_detail", kwargs={"pk": self.pk})
