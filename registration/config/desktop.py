# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Registration",
			"color": "blue",
			"icon": "octicon octicon-clippy",
			"type": "module",
			"label": _("Registration")
		},
		{
			"module_name": "Events",
			"_doctype": "Events",
			"color": "#b512de",
			"icon": "fa fa-calendar-check-o",
			"type": "link",
			"link": "List/Events"
		},
		{
			"module_name": "Participant Data",
			"_doctype": "Participant Data",
			"color": "#800000",
			"icon": "fa fa-file-powerpoint-o",
			"type": "link",
			"link": "List/Participant Data"
		},
		{
			"module_name": "Update Participant",
			"_doctype": "Update Participant",
			"color": "#b512de",
			"icon": "fa fa-upload",
			"type": "link",
			"link": "List/Update Participant"
		},
	]
