import frappe
from erpnext.crm.doctype.lead.lead_dashboard import get_data as original_get_data

def get_data(**kwargs):
    data = original_get_data()

    # Add Vehicle to the transactions list if not already there
    new_item = "Vehicle"
    if new_item not in data["transactions"][0]["items"]:
        data["transactions"][0]["items"].append(new_item)

    # Correct way to add a dynamic link to a dict
    # Format: fieldname: ["Section Label", "fieldname"]
    data["dynamic_links"]["lead"] = ["Lead", "lead"]

    return data
