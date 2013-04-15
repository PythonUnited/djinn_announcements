from django.forms.models import inlineformset_factory
from pgcontent.views.base import PGDetailView, PGEditView, PGDeleteView, \
    PGAddView, PGGroupAddView
from djinn_announcements.models.serviceannouncement import ServiceAnnouncement
from djinn_announcements.forms.serviceannouncement import \
    ServiceAnnouncementForm
from djinn_announcements.forms.announcementupdate import AnnouncementUpdateForm
from djinn_announcements.models.announcementupdate import AnnouncementUpdate


class UpdateFormMixin(object):

    def _create_formset(self, *args, **kwargs):

        return inlineformset_factory(ServiceAnnouncement,
                                     AnnouncementUpdate,
                                     form=AnnouncementUpdateForm,
                                     extra=1)(*args, **kwargs)
    
    def get_context_data(self, **kwargs):

        context = super(UpdateFormMixin, self).get_context_data(**kwargs)

        context['updatesform'] = self._create_formset(instance=self.object)

        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        formset = self._create_formset(request.POST, request.FILES, 
                                       instance=self.object)
        if formset.is_valid():
            formset.save()
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            ctx = self.get_context_data(form=form)
            ctx['updatesform'] = formset

            def to_label(err):
                              
                return (formset.forms[0].fields[err[0]].label, err[1])
            
            ctx['errors'] = map(to_label, formset.errors[0].items())

            return self.render_to_response(ctx)
        return super(UpdateFormMixin, self).post(request, *args, **kwargs)


class ServiceAnnouncementCreateView(UpdateFormMixin, PGAddView):

    model = ServiceAnnouncement
    form_class = ServiceAnnouncementForm


class ServiceAnnouncementUpdateView(UpdateFormMixin, PGEditView):

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
