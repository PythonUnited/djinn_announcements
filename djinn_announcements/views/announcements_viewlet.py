from django.views.generic import TemplateView
from djinn_announcements.models.announcement import Announcement


class AnnouncementsViewlet(TemplateView):

    template_name = "snippets/announcements_viewlet.html"

    def get_context_data(self, **kwargs):

        ctx = super(AnnouncementsViewlet, self).get_context_data(**kwargs)

        ctx['view'] = self

        return ctx

    def announcements(self, limit=5):

        return Announcement.objects.all(priority=0)[:limit]

    def priority_announcements(self, limit=1):

        return Announcement.objects.all(priority=1)[:limit]
