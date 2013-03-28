from django.utils.translation import ugettext_lazy as _

ANNOUNCEMENT_STATUS = {0: _("Open"), 20: _("Closed"), 10: _("In progress")}

ANNOUNCEMENT_STATUS_VOCAB = (("", "---"), ) + \
    tuple(sorted(ANNOUNCEMENT_STATUS.items()[:2]))

SERVICEANNOUNCEMENT_STATUS_VOCAB = (("", "---"), ) + \
    tuple(sorted(ANNOUNCEMENT_STATUS.items()))

ANNOUNCEMENT_PRIORITY = {0: _("Normal"), 1: _("High")}

ANNOUNCEMENT_PRIORITY_VOCAB = sorted(ANNOUNCEMENT_PRIORITY.items())

STATUS_CLASSES = {0: "open", 20: "closed", 10: "progress"}
