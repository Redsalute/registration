// Copyright (c) 2018, ayampenyet and contributors
// For license information, please see license.txt

frappe.ui.form.on('Participant Data', {
	refresh: function(frm) {

	},

	image: function() {
		refresh_field("image_view");
	},
});
