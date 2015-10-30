from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Assign Class",
					"description": _("Assign Class")
				},
				{
					"type": "doctype",
					"name": "Class Members",
					"description": _("Class Members")
				},
				{
					"type": "doctype",
					"name": "Class Setup",
					"description": _("Class Setup")
				},
				{
					"type": "doctype",
					"name": "Class Attendance",
					"description": _("Class Attendance")
				},
				{
					"type": "doctype",
					"name": "Duration",
					"description": _("Duration")
				},
				{
					"type": "doctype",
					"name": "Subject",
					"description": _("Subject")
				}
			]
		}
	]
