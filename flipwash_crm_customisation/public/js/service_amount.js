frappe.ui.form.on('Services Item', {
    qty: function(frm, cdt, cdn) {
        calculate_amount(frm, cdt, cdn);
    },
    rate: function(frm, cdt, cdn) {
        calculate_amount(frm, cdt, cdn);
    }
});

function calculate_amount(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    if (row.qty && row.rate) {
        row.amount = row.qty * row.rate;
        frm.refresh_field('services');  // Replace with the actual child table fieldname if different
    }
}
frappe.ui.form.on('Lead', {
    refresh: function(frm) {
        frm.fields_dict['services'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    item_group: "Services"
                }
            };
        };
    }
});







