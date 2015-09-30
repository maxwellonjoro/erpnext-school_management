frappe.pages['school-setup'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'School Setup',
		single_column: true
	});

	page.main.html(frappe.render_template("school_page", {}));

	//page.main.find(".btn-primary").on("click", function() {
	//	new_doc("School Details");
	//});

	$.ajax({
		url: "/api/method/school_management.school_pay.get_school_details",
		success: function(data) {
			if(!data.data) {				
				page.main.find(".pos-setting-message").removeClass('hide');
			}else{
				page.main.find(".pos-setting-message-2").removeClass('hide');
				var json;
				json = eval("(function(){return " + data.data + ";})()");
				var element = document.getElementById("school-name");	
				element.innerHTML = json.school_name;

				element = document.getElementById("school-address");	
				element.innerHTML = json.address;

				element = document.getElementById("school-country");	
				element.innerHTML = json.city + ", " + json.country;
			}
		}
	});
}
