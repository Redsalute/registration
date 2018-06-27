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
		entries = frappe.db.sql(query, as_dict=1)
		print entries
		# self.data1 = "pooja"
		self.set('participant_details', [])

		

		for d in self.get('participant_details'):
			print("dkkkkk",d)
		now = frappe.utils.now
		
		if entries:
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
		else:
			frappe.msgprint("No Record Found")


	def update_participant(self,target_doc):
		target_doc = frappe.get_doc("Events",self.event)
		print (target_doc)
		# print(target_doc.participants[0].participant_data)
		for i in self.participant_details:
			print("\n\n\n\n\n\n\n\n")
			print ("hello from items")
			print(i.participant_data)
			myflag = True
			for k in target_doc.participants:
				if k.participant_data == i.participant_data:
					myflag = False
			if myflag == True:
				doc_req = {
					"doctype": "Event Participant",
					"participant_data": i.participant_data,
					"time_attendance": i.time_attendance
				}
				target_doc.append("participants", doc_req)
				print(len(target_doc.participants))
				target_doc.save()
				frappe.msgprint("Participant Updated in Event")
			else:
				frappe.msgprint("Card allready punched, Thanks for comming")
			