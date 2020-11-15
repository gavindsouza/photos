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
		});
	},
	refresh: function(frm) {
		frm.add_custom_button("Process Photo", function () {
			frm.call("process_photo").then(r => {
				if (!r.exc) {
					frappe.show_alert({
						message: "Photo processing queued successfully",
						indicator: "green"
					});
				} else {
					console.error(r);
				}
			});
		});
	}
});
