// Copyright (c) 2025, Abhishek Kumar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("CRM Customisation", {
// 	refresh(frm) {

// 	},
// });
frappe.listview_settings['Lead'] = {
    refresh: function(listview) {
        // Add a custom button to the list view header
        listview.page.add_inner_button(__('Custom Button'), function() {
            // Define the action when the button is clicked
            frappe.msgprint('Custom Button Clicked!');
            // Add your custom logic here, e.g., call a server method or navigate
        });
    }
};
