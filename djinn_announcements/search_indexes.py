from haystack import site
from djinn_announcements.models.announcement import Announcement
from djinn_announcements.models.serviceannouncement import ServiceAnnouncement
from pgsearch.base import ContentRealTimeSearchIndex


TPL = """%(title)s %(text)s"""


class AnnouncementIndex(ContentRealTimeSearchIndex):

    """ Index for announcements """

    def __init__(self, model, backend=None):

        super(AnnouncementIndex, self).__init__(model, backend=backend)

        self.fields['text'].template_name = \
            self.fields['content_auto'].template_name = \
            "indexes/announcement_index.txt"

    def index_queryset(self):

        return self.model.objects.filter(serviceannouncement__isnull=True)


class ServiceAnnouncementIndex(AnnouncementIndex):

    def index_queryset(self):

        return self.model.objects.all()


site.register(Announcement, AnnouncementIndex)
site.register(ServiceAnnouncement, ServiceAnnouncementIndex)
