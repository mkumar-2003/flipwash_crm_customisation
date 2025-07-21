import frappe

def create_demo_data():
    fuel_types = ["Petrol", "Diesel", "Electric", "Hybrid"]
    transmission_types = ["Manual", "Automatic", "CVT", "AMT", "DCT"]
    vehicle_conditions = ["New", "Excellent", "Good", "Fair", "Poor", "Damaged"]

    # Insert fuel types
    for fuel in fuel_types:
        if not frappe.db.exists("Fuel Type", {"fuel_type": fuel}):
            doc = frappe.get_doc({
                "doctype": "Fuel Type",
                "fuel_type": fuel
            })
            doc.insert(ignore_permissions=True)

    # Insert transmission types
    for transmission in transmission_types:
        if not frappe.db.exists("Transmission Type", {"transmission_type": transmission}):
            doc = frappe.get_doc({
                "doctype": "Transmission Type",
                "transmission_type": transmission
            })
            doc.insert(ignore_permissions=True)

    # Insert car conditions
    for condition in vehicle_conditions:
        if not frappe.db.exists("Vehicle Condition", {"vehicle_condition": condition}):
            doc = frappe.get_doc({
                "doctype": "Vehicle Condition",
                "vehicle_condition": condition
            })
            doc.insert(ignore_permissions=True)
