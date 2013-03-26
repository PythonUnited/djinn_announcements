from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from announcement import Announcement
from pgcontent.registry import CTRegistry


class ServiceAnnouncement(Announcement):

    """ Announcement of 'servicing' or disturbance. Should show
    expected end date"""

    start_date = models.DateTimeField(_('Start date'), auto_now_add=True)
    end_date = models.DateTimeField(_('(Expected) end date'), null=True,
                                      blank=True, default=None)
    
    @property
    def slug(self):
        return slugify(self.title)        

    class Meta:
        app_label = 'djinn_announcements'
        ordering = ('created', )


CTRegistry.register("serviceannouncement", 
                    {"class": ServiceAnnouncement,
                     "user_can_add": True,
                     "app": "djinn_announcements",
                     "name": _("ServiceAnnouncement"),
                     "label": _("ServiceAnnouncement"),
                     "add_permission": \
                         "djinn_announcements.add_serviceannouncement",
                     "group_add": True,
                     "filter_label": _("ServiceAnnouncements"),
                     "name_plural": _("serviceannouncements")})
