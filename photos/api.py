import json

import frappe

from photos.utils import get_image_path, image_resize


@frappe.whitelist(methods=["GET", "POST"])
def roi(name: str):
    import cv2

    location, img = frappe.db.get_value("ROI", name, ["location", "image"])
    _file = frappe.get_doc("File", img)
    top, right, bottom, left = json.loads(location)
    image = cv2.rectangle(
        cv2.imread(get_image_path(_file.file_url)),
        (left, top),
        (right, bottom),
        (0, 0, 255),
        6,
    )
    resized_img = image_resize(image, width=800, height=600)
    _, img = cv2.imencode(".jpg", resized_img)

    frappe.response.filename = f"temp_{_file.file_name}"
    frappe.response.type = "download"
    frappe.response.display_content_as = "inline"
    frappe.response.filecontent = img.tobytes()


@frappe.whitelist(methods=["GET"])
def photo(name: str, roi: bool = False):
    import cv2

    photo = frappe.get_doc("Photo", name)
    _file = frappe.get_doc("File", photo.photo)
    image = cv2.imread(get_image_path(_file.file_url))

    if roi:
        # draw roi for all encodings, possibly with labels
        for _roi in photo.people:
            location, person = frappe.db.get_value(
                "ROI", _roi.face, ["location", "person"]
            )
            top, right, bottom, left = json.loads(location)
            image = cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 6)

    resized_img = image_resize(image, height=400)
    _, img = cv2.imencode(".jpg", resized_img)

    frappe.response.filename = f"temp_{_file.file_name}"
    frappe.response.type = "download"
    frappe.response.display_content_as = "inline"
    frappe.response.filecontent = img.tobytes()


@frappe.whitelist()
def filter_photo(*args, **kwargs):
    return frappe.get_list(
        "File",
        filters={
            "is_folder": False,
            "name": ("not in", frappe.get_all("Photo", pluck="photo")),
        },
        fields=["name", "file_name"],
        as_list=True,
    )
