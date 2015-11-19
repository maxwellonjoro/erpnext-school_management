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
					"name": "Admit Student",
					"description": _("Admit Student")
				},
				{
					"type": "doctype",
					"name": "Payment",
					"description": _("Payment")
				},
				{
					"type": "doctype",
					"name": "Student Information",
					"description": _("Student Information")
				},
				{
					"type": "doctype",
					"name": "Student Registration",
					"description": _("Student Registration")
				},
				{
					"type": "page",
					"name": "Students",
					"description": _("Students")
				},
			]
		}
	]
