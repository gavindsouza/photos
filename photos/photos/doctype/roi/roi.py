# -*- coding: utf-8 -*-
# Copyright (c) 2020, Gavin D'souza and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import json
import numpy as np
import frappe
import face_recognition
from random import choice


class ROI(Document):
    def validate(self):
        # don't let duplicate ROIs in
        if self.name != frappe.db.exists("ROI", {
            "encoding": self.encoding,
            "location": self.location,
            "image": self.image,
        }):
            frappe.throw("ROI already exists!", frappe.DuplicateEntryError)

    def after_insert(self):
        self.process_roi()

    def process_roi(self):
        known_rois = frappe.get_all("ROI", filters={"person": ("!=", "")}, fields=["person", "encoding"])
        if known_rois:
            known_face_names, known_face_encodings = zip(*[
                (x.person, json.loads(x.encoding)) for x in known_rois
            ])
            unknown_encoding = json.loads(self.encoding)
            matches = face_recognition.compare_faces(
                np.asarray(known_face_encodings),
                np.asarray(unknown_encoding)
            )
            # # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                self.db_set("person", known_face_names[first_match_index])
                frappe.publish_realtime("refresh_roi", user=frappe.session.user)


def process_labelled_photos():
    """Compares unlabelled photos with labelled ones to label more.

    Returns:
        list: unrecognized ROIs
    """
    # frappe develop seems to have a bug which returns empty list if person is
    # filtered by None. So, using "" as replacement, since that works...
    known_rois = frappe.get_all("ROI", filters={"person": ("!=", "")}, fields=["person", "encoding"])

    unrecognized_rois = frappe.get_all("ROI", filters={"person": ""}, fields=["name", "encoding"])
    recognized_photos = {}

    # match unknown encodings with known ones
    if known_rois:
        known_face_names, known_face_encodings = zip(*[(x.person, json.loads(x.encoding)) for x in known_rois])
        for unknown in unrecognized_rois:
            unknown_encoding = json.loads(unknown.encoding)
            matches = face_recognition.compare_faces(
                np.asarray(known_face_encodings),
                np.asarray(unknown_encoding)
            )
            # # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                person = known_face_names[first_match_index]
                recognized_photos[unknown.name] = person

        # update records with newly discovered data
        for roi, person in recognized_photos.items():
            frappe.db.set_value("ROI", roi, "person", person)

        # remove any newly found entries from the unrecognized photos
        unrecognized_rois = [x for x in unrecognized_rois if x.name not in recognized_photos]

    return unrecognized_rois


def process_unlabelled_photos(unrecognized_rois=None):
    """Assigns one random label for an ROI and runs process_labelled_photos"""
    if not unrecognized_rois:
        unrecognized_rois = process_labelled_photos()
        # frappe.get_all("ROI", filters={"person": ""}, fields=["name", "encoding"])

    # compare faces of recognized with unrecognized labels
    # if no recognized ROIs exist, start grouping similar faces..ie set a temporary name for them
    roi = choice(unrecognized_rois)

    person = frappe.new_doc("Person")
    person.person_name = frappe.mock("name")
    person.save()

    frappe.db.set_value("ROI", roi.name, "person", person.name)

    return process_labelled_photos()
