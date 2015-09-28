from __future__ import unicode_literals
import frappe
import json
import sys
import requests
from frappe.utils import strip_html_tags

no_cache = 1
no_sitemap = 1

@frappe.whitelist(allow_guest=True)
def get_school_details():
    sch_details = frappe.db.get_singles_dict("School Details")
    if sch_details:
        ret_str = json.dumps(sch_details)
    	frappe.response['data'] = ret_str

    return 

@frappe.whitelist(allow_guest=True)
def new_school_details():
    new_doc("School Details")
    return 

@frappe.whitelist(allow_guest=True)
def test():
    response = requests.post('http://localhost:8000/api/method/library_management.sample_app.ping')
    jsonStr = response.text
    responseData = json.loads(jsonStr)
    return responseData['message']

@frappe.whitelist(allow_guest=True)
def get_data_post():
    requestData = json.loads(frappe.local.request.data)
    frappe.response['data'] = requestData
    return

@frappe.whitelist(allow_guest=True)
def simulate_response():
    #requestData = json.loads(frappe.local.request.data)
    frappe.response['Result'] = 'Success'
    frappe.response['Data'] = '00'
    return

@frappe.whitelist(allow_guest=True)
def ping():
    return 'pong'

@frappe.whitelist(allow_guest=True)
def login():
	"""handle request"""
	cmd = frappe.local.form_dict.cmd

	if cmd!='login':
		execute_cmd(cmd)

	return build_response("json")

@frappe.whitelist(allow_guest=True)
def api_trials():
    requestData = json.loads(frappe.local.request.data)
    return requestData['tnxType']

@frappe.whitelist(allow_guest=True)
def receive_payment_info():
    try:
	    requestData = json.loads(frappe.local.request.data)
	    try:
		tnxType = requestData['tnxType']
		studentName = requestData['studentName']
		amount = requestData['amount']
		regNo = requestData['regNo']
		Desc = requestData['Desc']
		if not tnxType or not studentName or not amount or not regNo or not Desc:
			frappe.response['Data']='300'
			frappe.response['Result']='Failed'
			frappe.response["Message"] = 'Invalid request - fields empty'
			return

		else:
		    try:
			payment = frappe.get_doc({"doctype": "Payment","admit_student": regNo,"session": "First", "fee_total": amount, "fee_paid": amount, "fee_status": "Paid","payment_method": "Cash"}) 
			payment.insert(ignore_permissions=True)
			payment.submit()
		    except Exception as e:
			frappe.response['Message']='Student not found'
			frappe.response['Result']='Failed'
			frappe.response['Data']='302'
			frappe.response['Extra']=e.args
		    else:
			frappe.response['Message']='Payment information received successfully'
			frappe.response['Result']='Success'
			frappe.response['Data']='OK'

	    except Exception as e:
		frappe.response['Data']='300'
		frappe.response['Result']='Failed'
		frappe.response["Message"] = 'Invalid request - fields missing'
		frappe.response["Extra"] = e.args

    except Exception as e:
	frappe.response['Data']='500'
	frappe.response['Result']='Failed'
	frappe.response["Message"] = 'An error has occured'
	frappe.response["Extra"] = e.args


    return


