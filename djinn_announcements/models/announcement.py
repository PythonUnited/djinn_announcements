from django.db import models
from django.utils.translation import ugettext_lazy as _
from pgcontent.models.publishable import PublishableContent
from pgcontent.registry import CTRegistry
from pgcontent.models.commentable import CommentableMixin
from pgcontent.models.changeable import ChangeableBaseContent
from pgcontent.models.relatable import RelatableMixin


class Announcement(ChangeableBaseContent, RelatableMixin):

    title = models.CharField(_('Title'), max_length=200)
    text = models.TextField(_('Text'), max_length=150)
    status = models.IntegerField(_('Status'), blank=True, null=True) 
    priority = models.IntegerField(_("Priority"), default=0)

    def __unicode__(self):

        return self.title

    @property
    def title_slice(self):

        max = 51

        if len(self.title) > max:
            return "%s..." % self.title[:max]
        return self.title

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
                     "filter_label": _("Announcements"),
                     "name_plural": _("announcements")})
