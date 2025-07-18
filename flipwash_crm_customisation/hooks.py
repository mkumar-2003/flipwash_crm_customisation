app_name = "flipwash_crm_customisation"
app_title = "Flipwash Crm Customisation"
app_publisher = "Abhishek Kumar"
app_description = "Flipwash Crm Customisation"
app_email = "abhishek.kumar6@oodles.io"
app_license = "unlicense"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "flipwash_crm_customisation",
# 		"logo": "/assets/flipwash_crm_customisation/logo.png",
# 		"title": "Flipwash Crm Customisation",
# 		"route": "/flipwash_crm_customisation",
# 		"has_permission": "flipwash_crm_customisation.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/flipwash_crm_customisation/css/flipwash_crm_customisation.css"
# app_include_js = "/assets/flipwash_crm_customisation/js/flipwash_crm_customisation.js"

# include js, css files in header of web template
# web_include_css = "/assets/flipwash_crm_customisation/css/flipwash_crm_customisation.css"
# web_include_js = "/assets/flipwash_crm_customisation/js/flipwash_crm_customisation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "flipwash_crm_customisation/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "flipwash_crm_customisation/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "flipwash_crm_customisation.utils.jinja_methods",
# 	"filters": "flipwash_crm_customisation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "flipwash_crm_customisation.install.before_install"
# after_install = "flipwash_crm_customisation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "flipwash_crm_customisation.uninstall.before_uninstall"
# after_uninstall = "flipwash_crm_customisation.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "flipwash_crm_customisation.utils.before_app_install"
# after_app_install = "flipwash_crm_customisation.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "flipwash_crm_customisation.utils.before_app_uninstall"
# after_app_uninstall = "flipwash_crm_customisation.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "flipwash_crm_customisation.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"flipwash_crm_customisation.tasks.all"
# 	],
# 	"daily": [
# 		"flipwash_crm_customisation.tasks.daily"
# 	],
# 	"hourly": [
# 		"flipwash_crm_customisation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"flipwash_crm_customisation.tasks.weekly"
# 	],
# 	"monthly": [
# 		"flipwash_crm_customisation.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "flipwash_crm_customisation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "flipwash_crm_customisation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "flipwash_crm_customisation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["flipwash_crm_customisation.utils.before_request"]
# after_request = ["flipwash_crm_customisation.utils.after_request"]

# Job Events
# ----------
# before_job = ["flipwash_crm_customisation.utils.before_job"]
# after_job = ["flipwash_crm_customisation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"flipwash_crm_customisation.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

after_install = "flipwash_crm_customisation.demo_data.data.create_demo.create_demo_data"

doctype_js = {
    "Lead": "public/js/service_amount.js",
}
# override_doctype_dashboards = {
# 	"Lead": "flipwash_crm_customisation.overrides.lead_dashboard.get_data"
# }

# hooks.py
scheduler_events = {
    "cron": {
        "0 * * * *": [
            "flipwash_crm_customisation.scripts.booking_notification.notify_upcoming_bookings"
        ]
    }
}
override_doctype_class = {
    "Lead": "flipwash_crm_customisation.flipwash_crm_customisation.doctype.crm_customisation.crm_customisation.CRMLeadInherit"
}

