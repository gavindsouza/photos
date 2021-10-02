# Copyright (c) 2020, Gavin D'souza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Photo(Document):
    def validate(self):
        # TODO checklist:
        # - check if file type is supported
        # - extract and save image meta data
        # - probably parse and save as JSON which can be updated via the UI and written to the file
        pass

    def after_insert(self):
        # start processing etc, maybe via frappe.enqueue
        frappe.enqueue("photos.photos.doctype.photo.photo.process_photo", queue="long", photo=self)

    def process_photo(self):
        # re-run process photo for whatever reason
        frappe.enqueue("photos.photos.doctype.photo.photo.process_photo", queue="long", photo=self)


def process_photo(photo: Photo):
    """Processes photo and searches Persons and Objects in them.

    TODO:
     - locating objects

    Args:
        photo (Photo): Photo document object
    """
    import json

    # import cv2
    import face_recognition
    import numpy as np
    from frappe.core.doctype.file.file import get_local_image

    people = []
    image, filename, extn = get_local_image(
        frappe.db.get_value("File", photo.photo, "file_url")
    )
    img = np.asarray(image)
    # TODO: make image smaller? check if necessary and x4 box sizes before saving them
    # img = cv2.resize(np.asarray(image), (0, 0), fx=0.25, fy=0.25)
    boxes = face_recognition.face_locations(img, model='hog')
    encodings = face_recognition.face_encodings(img, boxes)

    for (encoding, location) in zip(encodings, boxes):
        roi = frappe.new_doc("ROI")
        roi.image = photo.photo
        roi.location = json.dumps(location)
        roi.encoding = json.dumps(encoding.tolist())
        try:
            roi.insert()
            people.append(roi.name)
        except frappe.DuplicateEntryError:
            pass

    for x in people:
        photo.append("people", {"face": x})

    photo.number_of_times_processed += 1
    photo.is_processed = True
    photo.save()

    frappe.publish_realtime('refresh_photo', user=frappe.session.user)

    return photo
