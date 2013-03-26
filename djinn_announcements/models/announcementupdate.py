from django.db import models
from django.utils.translation import ugettext_lazy as _
from announcement import Announcement


class AnnouncementUpdate(models.Model):

    date = models.DateTimeField(_('Date'), auto_now_add=True)
    text = models.TextField(_('Text'), max_length=150)
    announcement = models.ForeignKey(Announcement,
                                     related_name="updates")

    class Meta:
        app_label = 'djinn_announcements'
