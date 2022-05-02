from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Model Team


class Team(models.Model):
    PLAN_ACTIVE = 'active'
    PLAN_CANCELLED = 'cancelled'

    CHOICES_PLAN_STATUS = (
        (PLAN_ACTIVE, 'Active'),
        (PLAN_CANCELLED, 'Cancelled')
    )

    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(
        User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})
