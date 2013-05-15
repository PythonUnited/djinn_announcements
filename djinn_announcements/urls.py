from django.conf.urls.defaults import patterns, url, include
from djinn_contenttypes.views.utils import generate_model_urls
from views.announcementviewlet import AnnouncementViewlet, \
    PriorityAnnouncementViewlet, ServiceAnnouncementViewlet
from models import ServiceAnnouncement, Announcement , AnnouncementUpdate
from forms.announcement import AnnouncementForm
from forms.serviceannouncement import ServiceAnnouncementForm
from forms.announcementupdate import AnnouncementUpdateForm


_urlpatterns = patterns(
    "",

    # Viewlet
    url(r"^$",
        AnnouncementViewlet.as_view(),
        name="djinn_announcements"),

    url(r"^priority$",
        PriorityAnnouncementViewlet.as_view(),
        name="djinn_priority_announcements"),
    
    url(r"^service$",
        ServiceAnnouncementViewlet.as_view(),
        name="djinn_service_announcements"),
    )

_a_patterns = generate_model_urls(Announcement)
_sa_patterns = generate_model_urls(ServiceAnnouncement)
_au_patterns = generate_model_urls(AnnouncementUpdate)

urlpatterns = patterns('',
    (r'^announcements/', include(_urlpatterns)),
    (r'^announcements/', include(_a_patterns)),
    (r'^announcements/', include(_sa_patterns)),
    (r'^announcements/', include(_au_patterns)),
)
