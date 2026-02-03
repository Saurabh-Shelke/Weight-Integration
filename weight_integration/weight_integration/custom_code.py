import frappe
import requests

# import frappe
# import requests
# from requests.exceptions import SSLError, RequestException

# @frappe.whitelist()
# def get_weight_from_php(docname):
#     try:
#         # response = requests.get("https://localhost:444/getweight.php", timeout=5, verify=False)
#         response = requests.get("http://127.0.0.1:8080/getweight.php", timeout=5, verify=False)
#         response.raise_for_status()
#         weight = float(response.text.strip())   
#         frappe.db.set_value("Delivery Note", docname, "custom_weight", weight)
#         frappe.msgprint(f"Weight fetched and updated: {weight}")  # Debugging line to confirm weight update
#         return weight
#     except Exception as e:
#         frappe.throw(f"Failed to fetch weight: {str(e)}")


@frappe.whitelist()
def get_weight_from_php(docname):
    try:
        # Get API from system settings
        api_url = frappe.db.get_single_value(
            "Weighing Machine Settings",
            "api_url"
        )

        if not api_url:
            frappe.throw("Weighing API URL is not configured in Weighing Machine Settings")

        response = requests.get(api_url, timeout=5)
        response.raise_for_status()

        weight = float(response.text.strip())

        frappe.db.set_value(
            "Delivery Note",
            docname,
            "custom_weight",
            weight
        )

        return weight

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Weighing Machine Error")
        frappe.throw(f"Failed to fetch weight: {str(e)}")

