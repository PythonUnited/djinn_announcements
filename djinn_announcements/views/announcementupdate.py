from pu_in_content.views.jsonbase import JSONCreateView, JSONDetailView, \
    JSONUpdateView, JSONDeleteView
from djinn_announcements.models.announcementupdate import AnnouncementUpdate
from djinn_announcements.forms.announcementupdate import AnnouncementUpdateForm


class AnnouncementUpdateCreateView(JSONCreateView):

    model = AnnouncementUpdate
    form_class = AnnouncementUpdateForm
    success_template_name = "djinn_announcements/snippets/announcementupdate.html"

    def get_initial(self):

        return {'announcement': self.kwargs['announcement_pk']}

class AnnouncementUpdateUpdateView(JSONUpdateView):

    model = AnnouncementUpdate
    form_class = AnnouncementUpdateForm
    success_template_name = "djinn_announcements/snippets/announcementupdate.html"


class AnnouncementUpdateDetailView(JSONDetailView):

    model = AnnouncementUpdate


class AnnouncementUpdateDeleteView(JSONDeleteView):

    model = AnnouncementUpdate
