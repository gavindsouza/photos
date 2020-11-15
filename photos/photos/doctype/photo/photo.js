// Copyright (c) 2020, Gavin D'souza and contributors
// For license information, please see license.txt

frappe.ui.form.on('Photo', {
	onload: function(frm) {
		frm.fields_dict["photo"].get_query = function(doc, dt, dn) {
			return {
				query:"photos.api.filter_photo",
			}
		};
		frappe.realtime.on("refresh_photo", () => {
			frm.reload_doc();
		})
	}
});
