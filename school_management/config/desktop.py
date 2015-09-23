# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Class": {
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Class")
		},
		"Dorm": {
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Dorm App")
		},
		"Library": {
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Library")
		},
		"Students": {
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Students")
		},
		"Teacher": {
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Teacher")
		}
	}
