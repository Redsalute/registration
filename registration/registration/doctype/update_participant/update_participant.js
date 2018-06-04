// Copyright (c) 2018, ayampenyet and contributors
// For license information, please see license.txt

frappe.ui.form.on('Update Participant', {
	refresh: function(frm) {
		frm.disable_save();
	},

	get_details: function(frm) {
		return frappe.call({
			method: "get_particpant_details",
			doc: frm.doc,
			callback: function(r, rt) {
				frm.refresh_field("participant_details");
				frm.refresh_fields();
				// frappe.msgprint("hii");
			}
		});
	},
	update_participant:function(frm) {
		return frappe.call({
			method:"update_participant",
			doc:frm.doc,
			callback:function(r,rt){
				frm.refresh_field("participant_details");
				frm.refresh_fields();
				frappe.msgprint("Participant Updated in Event")
			}
		});
		
	}
		
	//	
});
