from pu_in_content.views.jsonbase import JSONCreateView
from djinn_announcements.models.announcementupdate import AnnouncementUpdate
from djinn_announcements.forms.announcementupdate import AnnouncementUpdateForm


class AnnouncementUpdateCreateView(JSONCreateView):

    model = AnnouncementUpdate
    form_class = AnnouncementUpdateForm

    def get_initial(self):

        return {'announcement': self.kwargs['announcement_pk']}

