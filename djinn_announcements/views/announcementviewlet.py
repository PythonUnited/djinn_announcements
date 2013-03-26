from django.views.generic import TemplateView
from djinn_announcements.models.announcement import Announcement


class AnnouncementViewlet(TemplateView):

    template_name = "snippets/announcements_viewlet.html"

    def get_context_data(self, **kwargs):

        ctx = super(AnnouncementViewlet, self).get_context_data(**kwargs)

        ctx['view'] = self

        return ctx

    def announcements(self, limit=5):

        return Announcement.objects.filter(priority=0)[:limit]


class PriorityAnnouncementViewlet(AnnouncementViewlet):

    template_name = "snippets/priority_announcements_viewlet.html"

    def announcements(self, limit=1):

        return Announcement.objects.filter(priority=1)[:limit]
