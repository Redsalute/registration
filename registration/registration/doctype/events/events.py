# -*- coding: utf-8 -*-
# Copyright (c) 2018, ayampenyet and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt, getdate, nowdate, now, fmt_money
from frappe import msgprint, _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class Events(Document):
	def get_particpant_details(self):
		query = """select name, registration_no,chinese_name,indonesian_name 
		from `tabParticipant Data` 
		where 
		registration_no = '{0}' """.format(self.registration_no)

		# if self.get_all:
		# 	pass
		# else:
		# 	query += " and allow = 'Account'"

		entries = frappe.db.sql(query, as_dict=1)
		print entries
		# self.data1 = "pooja"
		self.set('participants', [])

		#print("\n\n")
		# return query

		for d in self.get('participants'):
			print("dkkkkk",d)
		now = frappe.utils.now
		print "\n\n\n\n\n\n"
		print (now)
		for d in entries:
			doc_req = {
				"doctype": "Event Participant",
				"participant_data": d.name,
				"registration_no": d.registration_no,
				"chinese_name": d.chinese_name,
				"indonesian_name": d.indonesian_name,
				"time_attendance":now()
			
			}
			self.append("participants", doc_req)
			# row = self.append('user_permission', {})
			# row.update(d)
			print(d,"\nl")