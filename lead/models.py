from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models

from team.models import Team

# Model lead


class Lead(models.Model):
    NEW = 'Nouveau'
    CONTACTED = 'Contacter'
    INPROGRESS = 'En cours'
    LOST = 'Perdu'
    WON = 'Gagner'

    CHOICES_STATUS = (
        (NEW, 'Nouveau'),
        (CONTACTED, 'Contacter'),
        (INPROGRESS, 'En cours'),
        (LOST, 'Perdu'),
        (WON, 'Gagner'),
    )

    LOW = 'Faible'
    MEDIUM = 'Moyenne'
    HIGH = 'Forte'

    CHOICES_PRIORITY = (
        (LOW, 'Faible'),
        (MEDIUM, 'Moyenne'),
        (HIGH, 'Forte'),
    )

    team = models.ForeignKey(Team, null=True, related_name='leads',
                             on_delete=models.CASCADE)
    company = models.CharField(_('Entreprise'), max_length=255)
    contact_person = models.CharField(_('Contact'), max_length=255)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Téléphone'), max_length=255)
    website = models.CharField(
        _('Site web'), max_length=255, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(
        _('Valeur estimé'), blank=True, null=True)
    status = models.CharField(
        max_length=25, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(_('Priorité'),
                                max_length=25, choices=CHOICES_PRIORITY, default=MEDIUM)
    assigned_to = models.ForeignKey(
        User, verbose_name='Assigné à', related_name='assignedleads', blank=True, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(
        User, verbose_name="Créer par", related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse("Lead_detail", kwargs={"pk": self.pk})
