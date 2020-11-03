from frappe.core.doctype.file.file import File, get_local_image
import numpy as np
from PIL import Image
import face_recognition
import json
import frappe

def generate_encodings(file: File, *args, **kwargs):
    frappe.enqueue("photos.api.insert_face_data", queue="long", file=file)


def insert_face_data(file):
    img_path = file.file_url
    image, filename, extn = get_local_image(img_path)
    img = np.asarray(image)

    boxes = face_recognition.face_locations(img, model='hog')
    encodings = face_recognition.face_encodings(img, boxes)

    for (encoding, face_location) in zip(encodings, boxes):
        face = frappe.new_doc("Face")
        face.image = file.name
        face.face_location = json.dumps(face_location)
        face.face_encoding = json.dumps(encoding.tolist())
        face.save()

    frappe.db.commit()
