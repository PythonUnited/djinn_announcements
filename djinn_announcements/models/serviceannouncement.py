from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from .announcement import Announcement
from djinn_contenttypes.registry import CTRegistry


class ServiceAnnouncement(Announcement):

    """ Announcement of 'servicing' or disturbance. Should show
    expected end date"""

    start_date = models.DateTimeField(
        _('Start date'),
        null=True, blank=True,
        default=None,
        help_text = _("Tijdstip waarop de dienstverlening is of wordt onderbroken (start storing of onderhoud)")
    )
    end_date = models.DateTimeField(
        _('(Expected) end date'),
        null=True, blank=True,
        default=None,
        help_text=_("Naar verwachting eindigt de storing/onderbreking op dit tijdstip")
    )
    remove_after_publish_to = models.BooleanField(
        _('Remove the content after publication to has past'),
        default=False
    )
    link = models.CharField(
        _('Link'),
        max_length=200,
        null=True, blank=True
    )

    @property
    def slug(self):

        return slugify(self.title)

    class Meta:
        app_label = 'djinn_announcements'
        # ordering = ('start_date', )
        ordering = ('-created', )


CTRegistry.register("serviceannouncement",
                    {"class": ServiceAnnouncement,
                     "app": "djinn_announcements",
                     "label": _("ServiceAnnouncement"),
                     "add_permission":
                     "djinn_announcements.add_serviceannouncement",
                     "filter_label": _("ServiceAnnouncements"),
                     "name_plural": _("serviceannouncements")})
