from django.views.generic import TemplateView
from djinn_announcements.models.announcement import Announcement
from djinn_announcements.models.serviceannouncement import ServiceAnnouncement


class AnnouncementViewlet(TemplateView):

    template_name = "snippets/announcements_viewlet.html"

    def get_context_data(self, **kwargs):

        ctx = super(AnnouncementViewlet, self).get_context_data(**kwargs)

        ctx['view'] = self

        return ctx

    def announcements(self, limit=5):

        _announcements = []

        for announcement in Announcement.objects.filter(priority=0):
            try:
                announcement.serviceannouncement
            except:
                _announcements.append(announcement)
            if len(_announcements) >= limit:
                break

        return _announcements


class PriorityAnnouncementViewlet(AnnouncementViewlet):

    template_name = "snippets/priority_announcements_viewlet.html"

    def announcements(self, limit=1):

        return Announcement.objects.filter(priority=1)[:limit]


class ServiceAnnouncementViewlet(AnnouncementViewlet):

    template_name = "snippets/serviceannouncements_viewlet.html"

    def announcements(self, limit=5):

        return ServiceAnnouncement.objects.all()[:limit]
