// Copyright (c) 2020, Gavin D'souza and contributors
// For license information, please see license.txt

frappe.ui.form.on('ROI', {
	onload: function(frm) {
		frappe.db.get_value("File", frm.doc.image, "file_url").then(payload => {
			const file_url = payload.message? payload.message.file_url : false;
			const wrapper = frm.get_field("preview").$wrapper;
			const box = JSON.parse(frm.doc.location).map(function(x) { return Math.ceil(x / 4) });
			// (left, bottom), (right, bottom)
			wrapper.html(`
				<div style="position: relative;">
					<canvas id="preview" class="img-responsive" style="position: absolute; left: 0; top: 0; z-index: 500;"></canvas>
					<canvas id="cover" class="img-responsive" style="position: absolute; left: 0; top: 0; z-index: 1000;"></canvas>
				</div>
			`);

			const cover = document.getElementById("cover");
			const ctx = cover.getContext("2d");
			const canvas = document.getElementById('preview');
			const _ctx = canvas.getContext("2d");
			const img = new Image();

			img.src = file_url;

			img.onload = function () {
				canvas.width = img.width;
				cover.width = img.width;
				canvas.height = img.height;
				cover.height = img.height;

				_ctx.drawImage(img, 0, 0);
				ctx.beginPath();
				ctx.rect(...box);
				ctx.lineWidth = "4";
				ctx.strokeStyle = "red";
				ctx.stroke();
			}

		});
	}
});
