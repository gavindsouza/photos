// Copyright (c) 2020, Gavin D'souza and contributors
// For license information, please see license.txt

frappe.ui.form.on('Photo', {
	onload: function(frm) {
		frm.set_query("photo", () => {
			return {
				filters: {
					is_folder: false,
				}
			}
		});
		frappe.realtime.on("refresh_photo", () => {
			frm.reload_doc();
		})
	}
});
