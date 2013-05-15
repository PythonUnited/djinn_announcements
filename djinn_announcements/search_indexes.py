from haystack import site, indexes
from djinn_announcements.models.announcement import Announcement
from djinn_announcements.models.serviceannouncement import ServiceAnnouncement
from pgsearch.base import ContentRealTimeSearchIndex


class AnnouncementIndex(ContentRealTimeSearchIndex):

    """ Index for announcements """

    text = indexes.CharField(document=True, use_template=True,
                             template_name="indexes/announcement_index.txt")


    def index_queryset(self):

        return self.model.objects.filter(serviceannouncement__isnull=True)


class ServiceAnnouncementIndex(AnnouncementIndex):

    def index_queryset(self):

        return self.model.objects.all()


site.register(Announcement, AnnouncementIndex)
site.register(ServiceAnnouncement, ServiceAnnouncementIndex)
