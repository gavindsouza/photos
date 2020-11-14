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
