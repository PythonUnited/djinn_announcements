from django.conf.urls.defaults import patterns, url, include
from djinn_contenttypes.views.base import DetailView, DeleteView, UpdateView, \
    CreateView
from views.serviceannouncement import ServiceAnnouncementCreateView, \
    ServiceAnnouncementUpdateView
from views.announcementupdate import AnnouncementUpdateCreateView
from views.announcementviewlet import AnnouncementViewlet, \
    PriorityAnnouncementViewlet, ServiceAnnouncementViewlet
from models import ServiceAnnouncement, Announcement , AnnouncementUpdate
from forms.announcement import AnnouncementForm
from forms.announcementupdate import AnnouncementUpdateForm


_urlpatterns = patterns(
    "",

    url(r"^serviceannouncement/(?P<pk>[\d]+)/(?P<slug>[^\/]+)/?",
        DetailView.as_view(model=ServiceAnnouncement),
        name="djinn_announcements_view_serviceannouncement"),

    url(r"^add/serviceannouncement$",
        ServiceAnnouncementCreateView.as_view(),
        name="djinn_announcements_add_serviceannouncement"),

    url(r"^edit/serviceannouncement/(?P<pk>[\d]+)/?",
        ServiceAnnouncementUpdateView.as_view(),
        name="djinn_announcements_edit_serviceannouncement"),
    
    url(r"^delete/serviceannouncement/(?P<pk>[\d]+)/?",
        DeleteView.as_view(model=ServiceAnnouncement),
        name="djinn_announcements_delete_serviceannouncement"),

    # Announcement updates
    url(r"^announcementupdate/(?P<pk>[\d]+)/(?P<slug>[^\/]+)/?",
        DetailView.as_view(model=AnnouncementUpdate),
        name="djinn_announcements_view_announcementupdate"),

    url(r"^add/announcementupdate/(?P<announcement_pk>[\d]+)/?$",
        AnnouncementUpdateCreateView.as_view(),
        name="djinn_announcements_add_announcementupdate"),

    url(r"^edit/announcementupdate/(?P<pk>[\d]+)/?$",
        UpdateView.as_view(model=AnnouncementUpdate, 
                               form_class=AnnouncementUpdateForm),
        name="djinn_announcements_edit_announcementupdate"),

    url(r"^delete/announcementupdate/(?P<pk>[\d]+)/?$",
        DeleteView.as_view(model=AnnouncementUpdate),
        name="djinn_announcements_delete_announcementupdate"),

    # Announcements
    url(r"^announcement/(?P<pk>[\d]+)/(?P<slug>[^\/]+)/?$",
        DetailView.as_view(model=Announcement),
        name="djinn_announcements_view_announcement"),

    url(r"^add/announcement/?$",
        CreateView.as_view(model=Announcement, form_class=AnnouncementForm),
        name="djinn_announcements_add_announcement"),

    url(r"^edit/announcement/(?P<pk>[\d]+)/?$",
        UpdateView.as_view(model=Announcement, form_class=AnnouncementForm),
        name="djinn_announcements_edit_announcement"),

    url(r"^delete/announcement/(?P<pk>[\d]+)/?$",
        DeleteView.as_view(model=Announcement),
        name="djinn_announcements_delete_announcement"),

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

urlpatterns = patterns('',
    (r'^announcements/', include(_urlpatterns)),
)
