frappe.pages['students'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Students',
		single_column: true
	});

	page.main.html(frappe.render_template("students", {}));

	//page.main.find(".btn-primary").on("click", function() {
	//	new_doc("School Details");
	//});

	$.ajax({
		url: "/api/resource/Admit Student",
		success: function(data) {
			if(!data.data) {				
				page.main.find(".no-student-message").removeClass('hide');
			}else{
				page.main.find(".students").removeClass('hide');
				alert(""+data.data);
				//var json;
				//json = eval("(function(){return " + data.data + ";})()");
				//var element = document.getElementById("first-name");	
				//element.innerHTML = json.first_name;

				//element = document.getElementById("school-address");	
				//element.innerHTML = json.address;

				//element = document.getElementById("school-country");	
				//element.innerHTML = json.city + ", " + json.country;
			}
		}
	});
}
