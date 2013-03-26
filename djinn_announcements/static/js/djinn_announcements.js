/**
 * Djinn Announcements JS lib.
 */

// Use djinn namespace
if (djinn == undefined) {
  var djinn = {}
}


djinn.hide_announcements_alert = function() {
  $("#announcements-alert").hide();
  $("#announcementlist").show();
}
