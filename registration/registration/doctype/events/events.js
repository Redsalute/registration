// Copyright (c) 2018, ayampenyet and contributors
// For license information, please see license.txt

frappe.ui.form.on('Events', {
	refresh: function(frm) {

	},
	get_details: function(frm) {
		return frappe.call({
			method: "get_particpant_details",
			doc: frm.doc,
			callback: function(r, rt) {
				frm.refresh_field("participants");
				frm.refresh_fields();
				// frappe.msgprint("hii");
			}
		});
	},
});
