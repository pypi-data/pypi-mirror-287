from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    created_at = models.DateTimeField(
        _("Created at"),
        help_text=_("Date and time on which the object was created"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("Updated at"), 
        help_text=_("Date and time on which the object was updated"),
        auto_now=True,
    )
    status = models.BooleanField(
        _("Status"),
        help_text=_("Status of the object"),
        default=True,
    )

    class Meta:
        abstract = True

class Service(Base):
    """Model definition for Service."""

    name = models.CharField(
        _("Name"), 
        help_text=_("Name of the service"),
        max_length=255
    )
    slug = models.SlugField(
        _("Slug"),
        help_text=_("Slug of the service"),
        unique=True
    )
    description = models.TextField(
        _("Description"),
        help_text=_("Description of the service")
    )
    image = models.ImageField(
        _("Image"),
        help_text=_("Image of the service"),
        upload_to="services"
    )

    class Meta:
        """Meta definition for Service."""

        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        """Unicode representation of Service."""
        return self.name
