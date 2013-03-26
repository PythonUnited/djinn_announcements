from django.utils.translation import ugettext_lazy as _

ANNOUNCEMENT_STATUS_VOCAB = (("", "---"), (0, _('Open')), (1, _('Closed')))

SERVICEANNOUNCEMENT_STATUS_VOCAB = ANNOUNCEMENT_STATUS_VOCAB + \
    ((2, _('In progress')),)

ANNOUNCEMENT_PRIORITY_VOCAB = ((0, _("Normal")), (1, _("High")))
