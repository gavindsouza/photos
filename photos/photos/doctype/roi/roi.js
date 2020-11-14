// Copyright (c) 2020, Gavin D'souza and contributors
// For license information, please see license.txt

frappe.ui.form.on('ROI', {
	onload: function(frm) {
		frappe.realtime.on("refresh_roi", () => {
			frm.reload_doc();
		});
	},
	refresh: function(frm) {
		const wrapper = frm.get_field("preview").$wrapper;
		wrapper.html(`
			<div class="img_preview">
				<img class="img-responsive" src="/api/method/photos.api.roi?name=${frm.doc.name}"></img>
			</div>
		`);
	}
});
