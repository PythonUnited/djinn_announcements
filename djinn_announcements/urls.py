from django.conf.urls.defaults import patterns, url, include
from views.serviceannouncement import \
    ServiceAnnouncementCreateView, ServiceAnnouncementDetailView, \
    ServiceAnnouncementUpdateView, ServiceAnnouncementDeleteView
from views.announcementupdate import AnnouncementUpdateCreateView, \
    AnnouncementUpdateUpdateView, AnnouncementUpdateDeleteView
from views.announcement import AnnouncementCreateView, AnnouncementDetailView, \
    AnnouncementUpdateView, AnnouncementDeleteView
from views.announcementviewlet import AnnouncementViewlet, \
    PriorityAnnouncementViewlet, ServiceAnnouncementViewlet


_urlpatterns = patterns(
    "",
             
    url(r"^serviceannouncement/(?P<pk>[\d]+)/(?P<slug>[^\/]+)/?",
        ServiceAnnouncementDetailView.as_view(),
        name="djinn_announcements_view_serviceannouncement"),
    
    url(r"^add/serviceannouncement$",
        ServiceAnnouncementCreateView.as_view(),
        name="djinn_announcements_add_serviceannouncement"),

    url(r"^edit/serviceannouncement/(?P<pk>[\d]+)/?",
        ServiceAnnouncementUpdateView.as_view(),
        name="djinn_announcements_edit_serviceannouncement"),
    
    url(r"^delete/serviceannouncement/(?P<pk>[\d]+)/?",
        ServiceAnnouncementDeleteView.as_view(),
        name="djinn_announcements_delete_serviceannouncement"),

    # Announcement updates
    url(r"^add/announcementupdate/(?P<announcement_pk>[\d]+)/?$",
        AnnouncementUpdateCreateView.as_view(),
        name="djinn_announcements_add_announcementupdate_json"),

    url(r"^edit/announcementupdate/(?P<pk>[\d]+)/?$",
        AnnouncementUpdateUpdateView.as_view(),
        name="djinn_announcements_edit_announcementupdate_json"),

    url(r"^delete/announcementupdate/(?P<pk>[\d]+)/?$",
        AnnouncementUpdateDeleteView.as_view(),
        name="djinn_announcements_delete_announcementupdate_json"),

    # Announcements
    url(r"^announcement/(?P<pk>[\d]+)/?$",
        AnnouncementDetailView.as_view(),
        name="djinn_announcements_view_announcement"),

    url(r"^add/announcement/?$",
        AnnouncementCreateView.as_view(),
        name="djinn_announcements_add_announcement_json"),

    url(r"^edit/announcementupdate/(?P<pk>[\d]+)/?$",
        AnnouncementUpdateView.as_view(),
        name="djinn_announcements_edit_announcement_json"),

    url(r"^delete/announcementupdate/(?P<pk>[\d]+)/?$",
        AnnouncementDeleteView.as_view(),
        name="djinn_announcements_delete_announcement_json"),

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
