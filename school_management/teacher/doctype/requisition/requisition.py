# -*- coding: utf-8 -*-
# Copyright (c) 2015, Riverbank solutions and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Requisition(Document):
	def validate(self):
		if self.cost >= 10000:
			frappe.throw(_("Amount entered is above minimum limit. Use Bulk Requisition"))
