from django.db import models
from django.utils.translation import ugettext_lazy as _
from pgcontent.registry import CTRegistry
from pgcontent.models.changeable import ChangeableBaseContent
from pgcontent.models.relatable import RelatableMixin
from djinn_announcements.settings import ANNOUNCEMENT_STATUS


class AnnouncementManager(models.Manager):

     def get_query_set(self):
         return super(AnnouncementManager, self).get_query_set().filter(
             is_initiated=False).exclude(title="")


class Announcement(ChangeableBaseContent, RelatableMixin):

    title = models.CharField(_('Title'), max_length=200)
    text = models.TextField(_('Text'))
    status = models.IntegerField(_('Status'), blank=True, null=True) 
    priority = models.IntegerField(_("Priority"), default=0)

    objects = AnnouncementManager()

    def __unicode__(self):

        return self.title

    @property
    def title_slice(self):

        """ Give title summary up to 50 chars """

        if len(self.title) > 50:
            return "%s..." % self.title[:50]
        return self.title

    @property
    def formatted_status(self):

        """ Format according to vocabulary """

        return ANNOUNCEMENT_STATUS.get(self.status, "")

    class Meta:
        app_label = 'djinn_announcements'
        ordering = ('-created', )


CTRegistry.register("announcement", 
                    {"class": Announcement,
                     "user_can_add": True,
                     "app": "djinn_announcements",
                     "name": _("Announcement"),
                     "label": _("Announcement"),
                     "add_permission": "djinn_announcements.add_announcement",
                     "group_add": True,
                     "filter_label": "",
                     "name_plural": _("announcements")})
