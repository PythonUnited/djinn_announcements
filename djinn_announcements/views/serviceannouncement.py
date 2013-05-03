from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from djinn_contenttypes.views.base import CreateView, UpdateView
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

        if self.request.POST.get("action", None) == "cancel":
            url = self.request.user.profile.get_absolute_url()
            return HttpResponseRedirect(url)

        self.object = None

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            self.object = form.save()
        else:
            return self.form_invalid(form)

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

        return HttpResponseRedirect(self.get_success_url())


class ServiceAnnouncementCreateView(UpdateFormMixin, CreateView):

    model = ServiceAnnouncement
    form_class = ServiceAnnouncementForm


class ServiceAnnouncementUpdateView(UpdateFormMixin, UpdateView):

    model = ServiceAnnouncement
    form_class = ServiceAnnouncementForm
