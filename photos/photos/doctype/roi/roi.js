// Copyright (c) 2020, Gavin D'souza and contributors
// For license information, please see license.txt

frappe.ui.form.on('ROI', {
	refresh: function(frm) {
		frappe.db.get_value("File", frm.doc.image, "file_url").then(payload => {
			const file_url = payload.message? payload.message.file_url : false;
			const is_viewable = frappe.utils.is_image_file(file_url);
			const box = JSON.parse(frm.doc.location).map(function(x) { return Math.ceil(x / 4) });

			frm.toggle_display("preview", is_viewable);

			if (is_viewable) {
				const wrapper = frm.get_field("preview").wrapper;
				wrapper.innerHTML = `
					<div class="img-responsive wrapper">
						<canvas id="preview" style="z-index: 500;"></canvas>
						<canvas id="cover" style="z-index: 1000;"></canvas>
					</div>
					<style>
					#wrapper{
						position:relative;
					}
					#preview,#cover{
						position:absolute; top:0px; left:0px;
						width:300px;
						height:200px;
					}
					</style>
				`;
				const canvas = document.getElementById('preview');
				const ctx = canvas.getContext('2d');
				const canover = document.getElementById('cover');
				const ctxover = canvas.getContext('2d');

				let img = new Image();
				img.src = file_url;

				// When the image is loaded, draw it
				img.onload = function () {
					canvas.width = img.width;
					canvas.height = img.height;

					canover.width = img.width;
					canover.height = img.height;

					ctx.drawImage(img, 0, 0);
					ctxover.beginPath();
					ctxover.lineWidth = "4";
					ctxover.strokeStyle = "red";
					ctxover.rect(...box);
					ctxover.stroke();
				}
			}
		});
	}
});
