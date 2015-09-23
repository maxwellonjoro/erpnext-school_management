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
					"name": "Article",
					"description": _("Article")
				},
				{
					"type": "doctype",
					"name": "Book",
					"description": _("Book")
				},
				{
					"type": "doctype",
					"name": "Library Member",
					"description": _("Library Member")
				},
				{
					"type": "doctype",
					"name": "Library Membership",
					"description": _("Library Membership")
				},
				{
					"type": "doctype",
					"name": "Library Transaction",
					"description": _("Library Transaction")
				},
			]
		}
	]
