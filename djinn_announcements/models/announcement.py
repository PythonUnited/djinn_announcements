from django.db import models
from django.utils.translation import ugettext_lazy as _
from markupfield.fields import MarkupField
from djinn_contenttypes.registry import CTRegistry
from djinn_contenttypes.models.base import BaseContent
from djinn_announcements.settings import ANNOUNCEMENT_STATUS, \
    ANNOUNCEMENT_STATUS_CLOSED, ANNOUNCEMENT_PRIORITY_HIGH, \
    ANNOUNCEMENT_PRIORITY_NORMAL


class Announcement(BaseContent):

    text = MarkupField(_('Text'), markup_type='plain', null=True, blank=True)
    status = models.IntegerField(_('Status'), blank=True, null=True)
    priority = models.IntegerField(_("Priority"), default=0)

    @property
    def sorted_updates(self):

        return self.updates.order_by("-date")

    def __unicode__(self):

        return self.title

    __str__ = __unicode__

    @property
    def formatted_status(self):

        """ Format according to vocabulary """

        return ANNOUNCEMENT_STATUS.get(self.status, "")

    def save(self, *args, **kwargs):

        if self.status == ANNOUNCEMENT_STATUS_CLOSED and \
                self.priority == ANNOUNCEMENT_PRIORITY_HIGH:
            self.priority = ANNOUNCEMENT_PRIORITY_NORMAL

        return super().save(*args, **kwargs)

    class Meta:
        app_label = 'djinn_announcements'
        ordering = ('-created', )


CTRegistry.register("announcement",
                    {"class": Announcement,
                     "app": "djinn_announcements",
                     "label": _("Announcement"),
                     "global_add": False,
                     "add_permission": "djinn_announcements.add_announcement",
                     "filter_label": _("Announcement"),
                     "name_plural": _("announcements")})
