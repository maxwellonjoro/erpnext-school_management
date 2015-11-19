# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt
from __future__ import unicode_literals

import frappe
import json

no_cache = 1
no_sitemap = 1

def get_context(context):
	if frappe.session.user == "Guest":
		frappe.local.flags.redirect_location = "/login"
		raise frappe.Redirect

	students = frappe.db.sql("select first_name, last_name, registration_number, assign_class, uploaded from `tabAdmit Student` where docstatus=1", as_dict=True)

	return {"students":students, "user":frappe.session.data}

def studentInfo(first_name, last_name, registration_number, assign_class):
	return {"studentName": first_name+' '+last_name,"admissionNo": registration_number, "Desc": assign_class }
