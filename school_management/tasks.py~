from __future__ import unicode_literals
import frappe
import json
import requests
#from frappe.utils import datediff, nowdate, format_date, add_days

def studentInfo(first_name, last_name, registration_number, assign_class):
	return {"schoolid": '400555',"studentName": first_name+' '+last_name,"admissionNo": registration_number, "Desc": assign_class }

@frappe.whitelist(allow_guest=True)
def test_on_submit(): 
    #send_data = {'tnxType':'pay','studentName':'Jose','amount':'10000','regNo':'E/COH/14001/000','Desc':'dafaaffd'}
    #send_str = json.dumps(send_data)
    #response = requests.post('http://localhost:8000/api/method/school_management.school_pay.receive_payment_info', data=send_str)
    students = frappe.db.sql("select first_name, last_name, registration_number, assign_class, uploaded, docstatus from `tabAdmit Student`", as_dict=True)
    for s in students:
        string = json.dumps(s)
        print "student: ",string

    return 

@frappe.whitelist(allow_guest=True)
def all(): 
    students = frappe.db.sql("select first_name, last_name, registration_number, assign_class, uploaded from `tabAdmit Student` where uploaded=0 and docstatus=1", as_dict=True)
    if students:
	s_str = []
	for s in students:
		s_str.append(studentInfo(s.first_name,s.last_name,s.registration_number,s.assign_class))

	json_data = {}
	json_data['students'] = s_str
	send_str = json.dumps(json_data)
    
	try:
            response = requests.post('http://api.quickpay.co.ke/quickpaynotification/api/register/registerstudent', data=send_str)

            res_result = response.json()['Result']
            res_data = response.json()['Data']
    
            if res_result=='Ok' and res_data=='00':
                for d in students:
	            frappe.db.sql("update `tabAdmit Student` set uploaded=1 where registration_number=%s",d.registration_number)
	except:
	    return

    return 

