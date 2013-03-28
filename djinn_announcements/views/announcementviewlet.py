from django.views.generic import TemplateView
from djinn_announcements.models.announcement import Announcement
from djinn_announcements.models.serviceannouncement import ServiceAnnouncement
from djinn_announcements.settings import SHOW_N_ANNOUNCEMENTS


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

    def announcements(self):

        try:
            return Announcement.objects.filter(priority=1)[:1]
        except:
            return None


class ServiceAnnouncementViewlet(AnnouncementViewlet):

    template_name = "snippets/serviceannouncements_viewlet.html"

    def announcements(self):

        try:
            priority_announcement = Announcement.objects.filter(priority=1) \
                [0].pk
        except:
            priority_announcement = -1

        return ServiceAnnouncement.objects.all(). \
            exclude(pk=priority_announcement)[:SHOW_N_ANNOUNCEMENTS]

    @property
    def show_more(self):

        return ServiceAnnouncement.objects.all().count() > SHOW_N_ANNOUNCEMENTS
