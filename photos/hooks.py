app_name = "photos"
app_title = "Photos"
app_publisher = "Gavin D'souza"
app_description = "Open Source Alternative to Google Photos"
app_icon = "octicon octicon-file-directory"
app_color = "orange"
app_email = "gavin18d@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/photos/css/photos.css"
# app_include_js = "/assets/photos/js/photos.js"

# include js, css files in header of web template
# web_include_css = "/assets/photos/css/photos.css"
# web_include_js = "/assets/photos/js/photos.js"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "photos.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "photos.install.before_install"
# after_install = "photos.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "photos.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {"File": {"after_insert": "photos.utils.process_file"}}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"photos.tasks.all"
# 	],
# 	"daily": [
# 		"photos.tasks.daily"
# 	],
# 	"hourly": [
# 		"photos.tasks.hourly"
# 	],
# 	"weekly": [
# 		"photos.tasks.weekly"
# 	]
# 	"monthly": [
# 		"photos.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "photos.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "photos.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
override_doctype_dashboards = {"File": "photos.utils.get_file_dashboard"}

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

app_logo_url = "/assets/photos/logo.svg"

website_context = {
    "favicon": "/assets/photos/favicon.ico",
    "splash_image": "/assets/photos/logo.svg",
}

website_route_rules = [
    {"from_route": "/gallery/<path:app_path>", "to_route": "gallery"},
]
