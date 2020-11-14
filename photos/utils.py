# -*- coding: utf-8 -*-
# Copyright (c) 2020, Gavin D'souza and Contributors
# See license.txt


def get_image_path(file_url):
    import frappe

    if file_url.startswith("/private"):
        file_url_path = (file_url.lstrip("/"), )
    else:
        file_url_path = ("public", file_url.lstrip("/"))
    return frappe.get_site_path(*file_url_path)


def chunk(l, n):
    """Creates list of elements split into groups of n."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def image_resize(image, width=None, height=None, inter=None):
    import cv2

    if not inter:
        inter = cv2.INTER_AREA
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized