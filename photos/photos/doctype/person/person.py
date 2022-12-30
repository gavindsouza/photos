# Copyright (c) 2020, Gavin D'souza and contributors
# For license information, please see license.txt
import json

import frappe
from frappe.model.document import Document

from photos.utils import get_image_path


class Person(Document):
    def validate(self):
        if not self.get("person_image"):
            self.set_profile_pic(save=False)

    def set_profile_pic(self, save=True):
        if self.user:
            # get user profile pic
            self.person_image = frappe.db.get_value("User", self.user, "user_image")
        else:
            # get random pic from ROI and set the pic here
            self.person_image = self.generate_profile_pic()

        if save:
            self.save()

    def generate_profile_pic(self):
        result = frappe.get_all(
            "ROI",
            filters={"person": self.person_name},
            limit_page_length=1,
            order_by="creation desc",
            fields=["image", "location"],
            as_list=True,
        )
        if result:
            import cv2

            _image, location = result[0]
            image_path = get_image_path(frappe.db.get_value("File", _image, "file_url"))
            top, right, bottom, left = json.loads(location)
            # TODO: fix cropping logic
            img_cropped = cv2.imread(image_path)[left:right, top:bottom]
            # TODO: create a file doc for temp profile pic and link it to self.person_image
            # create and save image in the tmp dir? frappe will probs copy the contents inside?
            cv2.imwrite("./temp_crop.jpg", img_cropped)
        else:
            # random gravatar??
            pass
