frappe.ui.form.on('Delivery Note', {
    custom_get_weight: function(frm) {
        frappe.call({
            method: "weight_integration.weight_integration.custom_code.get_weight_from_php",   // Python method
            args: {
                docname: frm.doc.name
            },
            callback: function(r) {
                if (r.message) {
                    frm.set_value("custom_weight", r.message);
                    frappe.msgprint(`Weight updated: ${r.message}`);
                }
            }
        });
    }
});

