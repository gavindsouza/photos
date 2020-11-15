import frappe
import json
import cv2
from photos.utils import get_image_path, image_resize


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
        6
    )
    resized_img = image_resize(image, width=800, height=600)
    _, img = cv2.imencode('.jpg', resized_img)
    frappe.response.filecontent = img.tobytes()


@frappe.whitelist()
def filter_photo(*args, **kwargs):
    return frappe.get_all(
        "File",
        filters={
            "is_folder": False,
            "name": ("not in", frappe.get_all("Photo", pluck="photo"))
        },
        fields=["name", "file_name"],
        as_list=True
    )
