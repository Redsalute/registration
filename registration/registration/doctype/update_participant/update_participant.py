# -*- coding: utf-8 -*-
# Copyright (c) 2018, ayampenyet and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt, getdate, nowdate, now, fmt_money
from frappe import msgprint, _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class UpdateParticipant(Document):
	def get_particpant_details(self):
		query = """select name, registration_no,chinese_name,indonesian_name 
		from `tabParticipant Data` 
		where 
		registration_no = '{0}' """.format(self.registraion_no)

		# if self.get_all:
		# 	pass
		# else:
		# 	query += " and allow = 'Account'"

		entries = frappe.db.sql(query, as_dict=1)
		print entries
		# self.data1 = "pooja"
		self.set('participant_details', [])

		#print("\n\n")
		# return query

		for d in self.get('participant_details'):
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
			self.append("participant_details", doc_req)
			# row = self.append('user_permission', {})
			# row.update(d)
			print(d,"\nl")
		# entries = sorted(list(query))
        # self.set('user_permission', [])

   #      for d in entries:
			# row = self.append('user_permission', {})
			# d.user = user
			# d.allow = allow
			# d.for_value = for_value
			# row.update(d)

	# def update_user_permissions(self):
	# 	frappe.msgprint("")
	# 	for i in self.user_permission:
	# 		is_existing = frappe.db.get_value("User Permission",{"user":self.for_user,
	# 			"allow":i.allow,"for_value":i.for_value},"name")
	# 		if not is_existing:
	# 			user_perm_doc = frappe.new_doc("User Permission")
	# 			user_perm_doc.user = self.for_user
	# 			user_perm_doc.allow = i.allow
	# 			user_perm_doc.for_value = i.for_value	
	# 			user_perm_doc.flags.ignore_permissions = True		
	# 			user_perm_doc.insert()
	# 			user_perm_doc.save()

	# 	frappe.msgprint("User record added successfuly")

	# 	# frappe.new_doc


	def update_participant(self,target_doc):
		target_doc = frappe.get_doc("Events",self.event)
		print (target_doc)
		for i in self.participant_details:
			print("\n\n\n\n\n\n\n\n")
			print ("hello from items")
			for j in target_doc.participants:
				if j.participant_data:		
					target_doc.set('participants', [])
					k = target_doc.append('participants', {})
					print("\n\n\n\n\n\n\n\n")
					print (k)
					print ("hello from world")
					k.participant_data = i.participant_data
					k.registration_no = i.registration_no
					k.chinese_name = i.chinese_name
					k.indonesian_name = i.indonesian_name
					k.time_attendance = i.time_attendance
					doclist = get_mapped_doc("Update Participant", self, {
					"Update Participant": {
						"doctype": "Events",
						"validation": {
							"docstatus": ["=", 0]
						},
					},
					"Participant details": {
						"doctype": "participants",
						"field_map": {
							"parent": self.event
						},
					},
				}, target_doc, ignore_permissions=False)
				target_doc.save()