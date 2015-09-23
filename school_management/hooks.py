# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "school_management"
app_title = "School Management"
app_publisher = "QuickPay"
app_description = "Manages schools on QuickPay - students, dorms, classes, library, teachers"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@quickpay.co.ke"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/school_management/css/school_management.css"
# app_include_js = "/assets/school_management/js/school_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/school_management/css/school_management.css"
# web_include_js = "/assets/school_management/js/school_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "school_management.install.before_install"
# after_install = "school_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "school_management.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
 	"all": [
 		"school_management.tasks.all"
 	],
# 	"daily": [
# 		"school_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"school_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"school_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"school_management.tasks.monthly"
# 	]
}

# Testing
# -------

# before_tests = "school_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "school_management.event.get_events"
# }

