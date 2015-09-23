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
					"name": "Dorm Allocation",
					"description": _("Dorm Allocation")
				},
				{
					"type": "doctype",
					"name": "Dorm Setup",
					"description": _("Dorm Setup")
				},
			]
		}
	]
