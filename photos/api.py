import frappe
import json
import cv2
from photos.utils import get_image_path


@frappe.whitelist(methods=["GET", "POST"])
def roi(name):
    location, img = frappe.db.get_value("ROI", name, ["location", "image"])
    _file = frappe.get_doc("File", img)
    frappe.response.filename = f"temp_{_file.file_name}"
    frappe.response.type = "download"
    frappe.response.display_content_as = "inline"
    top, right, bottom, left = json.loads(location)
    image = cv2.rectangle(
        cv2.imread(
            get_image_path(_file.file_url)
        ),
        (left, top), (right, bottom),
        (0, 0, 255),
        2
    )
    _, img = cv2.imencode('.jpg', image)
    frappe.response.filecontent = img.tobytes()
