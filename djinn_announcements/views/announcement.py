from pu_in_content.views.jsonbase import JSONCreateView, JSONDetailView, \
    JSONUpdateView, JSONDeleteView
from djinn_announcements.models.announcement import Announcement
from djinn_announcements.forms.announcement import AnnouncementForm


class AnnouncementCreateView(JSONCreateView):

    model = Announcement
    form_class = AnnouncementForm
    success_template_name = "djinn_announcements/snippets/announcement.html"

    def get_initial(self):

        return {'creator': self.request.user, 'changed_by': self.request.user}


class AnnouncementUpdateView(JSONUpdateView):

    model = Announcement
    form_class = AnnouncementForm
    success_template_name = "djinn_announcements/snippets/announcement.html"


class AnnouncementDeleteView(JSONDeleteView):

    model = Announcement
