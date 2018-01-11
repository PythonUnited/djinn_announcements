from django.conf.urls import url
from django.urls import include
from djinn_contenttypes.views.utils import generate_model_urls
from .views.announcementviewlet import AnnouncementViewlet, \
    PriorityAnnouncementViewlet, ServiceAnnouncementViewlet
from .models import ServiceAnnouncement, Announcement, AnnouncementUpdate


_urlpatterns = [

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
]

urlpatterns = [
    url(r'^announcements/', include(_urlpatterns)),
    url(r'^announcements/', include(generate_model_urls(Announcement))),
    url(r'^announcements/', include(generate_model_urls(ServiceAnnouncement))),
    url(r'^announcements/', include(generate_model_urls(AnnouncementUpdate))),
]
