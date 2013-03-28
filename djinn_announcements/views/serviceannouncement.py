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

    def get_template_names(self):

        if self.request.GET.get("modal", False):
            return ["djinn_announcements/snippets/serviceannouncement_modal.html"]
        else:
            return ["djinn_announcements/serviceannouncement_detail.html"]
        

class ServiceAnnouncementDeleteView(PGDeleteView):

    model = ServiceAnnouncement
