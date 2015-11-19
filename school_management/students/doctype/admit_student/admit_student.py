# -*- coding: utf-8 -*-
# Copyright (c) 2015, Riverbank Solutions and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document
import requests

class AdmitStudent(Document):
	def on_submit(self):
		self.f_name = self.get('first_name')
		self.l_name = self.get('last_name')
		self.r_number = self.get('registration_number')
		self.a_class = self.get('assign_class')
		self.send_student_details()

	def send_student_details(self): 
	        s_str = []

		s_str.append({"schoolid": '400555',"studentName": self.f_name+' '+self.l_name,"admissionNo": self.r_number, "Desc": self.a_class })

		json_data = {}
		json_data['students'] = s_str
		send_str = json.dumps(json_data)

		try:
		    response = requests.post('http://api.quickpay.co.ke/quickpaynotification/api/register/registerstudent', data=send_str)
	    
		    res_result = response.json()['Result']
		    res_data = response.json()['Data']

		    if res_result=='Ok' and res_data=='00':
                        frappe.db.sql("update `tabAdmit Student` set uploaded=1 where registration_number=%s",self.get("registration_number"))
		except Exception as e:
		    return
	    
	    	return 


