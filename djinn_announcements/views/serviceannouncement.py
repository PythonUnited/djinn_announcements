from pgcontent.views.base import PGDetailView, PGEditView, PGDeleteView, \
    PGAddView, PGGroupAddView
from djinn_announcements.models.serviceannouncement import ServiceAnnouncement
from djinn_announcements.forms.serviceannouncement import \
    ServiceAnnouncementForm


class ServiceAnnouncementCreateView(PGAddView):

    model = ServiceAnnouncement
    form_class = ServiceAnnouncementForm


class ServiceAnnouncementUpdateView(PGEditView):

    model = ServiceAnnouncement
    form_class = ServiceAnnouncementForm


class ServiceAnnouncementDetailView(PGDetailView):

    model = ServiceAnnouncement


class ServiceAnnouncementDeleteView(PGDeleteView):

    model = ServiceAnnouncement
