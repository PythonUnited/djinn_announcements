from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from djinn_contenttypes.views.base import CreateView, UpdateView, DetailView
from djinn_core.utils import urn_to_object
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

        if self.request.POST.get("action", None) == "cancel":
            return HttpResponseRedirect(self.view_url)

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ctx = self.get_context_data(form=form)

        is_valid = True

        if form.is_valid():
            # Do not return here! This sets self.object
            #
            self.form_valid(form)
        else:
            is_valid = False

        formset = self._create_formset(request.POST, request.FILES,
                                       instance=self.object)
        if formset.is_valid() and self.object:
            formset.save()
        else:
            is_valid = False
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            ctx['updatesform'] = formset

            def to_label(err):

                return (formset.forms[0].fields[err[0]].label, err[1])

            ctx['errors'] = map(to_label, formset.errors[0].items())

        if not is_valid:
            return self.render_to_response(ctx)
        else:
            return HttpResponseRedirect(self.get_success_url())


class ServiceAnnouncementView(DetailView):

    model = ServiceAnnouncement

    @property
    def link(self):

        _link = (self.object.link or "").split("::")[0]

        if _link.startswith("urn"):
            return urn_to_object(_link).get_absolute_url()
        else:
            return _link

    @property
    def link_target(self):
        try:
            return (self.object.link or "").split("::")[1]
        except:
            return None

    @property
    def link_title(self):

        _link = (self.object.link or "").split("::")[0]

        if _link.startswith("urn"):
            return urn_to_object(self.object.link).title
        else:
            return _link


class ServiceAnnouncementCreateView(UpdateFormMixin, CreateView):

    model = ServiceAnnouncement
    form_class = ServiceAnnouncementForm


class ServiceAnnouncementUpdateView(UpdateFormMixin, UpdateView):

    model = ServiceAnnouncement
    form_class = ServiceAnnouncementForm
