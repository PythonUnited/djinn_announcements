from django.core.urlresolvers import reverse
from djinn_contenttypes.views.base import CreateView
from djinn_announcements.models.announcementupdate import AnnouncementUpdate
from djinn_announcements.forms.announcementupdate import AnnouncementUpdateForm


class AnnouncementUpdateCreateView(CreateView):

    model = AnnouncementUpdate
    form_class = AnnouncementUpdateForm

    @property
    def add_url(self):

        return reverse("%s_add_%s" % (self.app_label, self.ct_name),
                       kwargs={'announcement_pk': 
                               self.kwargs['announcement_pk']})

    def get_initial(self):

        return {'announcement': self.kwargs['announcement_pk']}

