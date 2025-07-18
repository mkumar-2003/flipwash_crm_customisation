# import frappe
# import json
#
# @frappe.whitelist(allow_guest=True)
# def save_data():
# 	try:
# 		if not frappe.db.exists("DocType", "Lead"):
# 			return {
# 				"status": "error",
# 				"message": "Lead DocType does not exist."
# 			}
#
# 		data = frappe.request.get_data(as_text=True)
# 		if not data:
# 			return {
# 				"status": "error",
# 				"message": "No data received."
# 			}
#
# 		data_json = json.loads(data)
#
# 		# Extract and sanitize input
# 		name = str(data_json.get("name", "")).strip()
# 		name_parts = name.split()
# 		first_name = name_parts[0] if name_parts else ""
# 		last_name = name_parts[-1] if len(name_parts) > 1 else ""
# 		middle_name = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""
#
# 		phone = str(data_json.get("phone", "")).strip()
# 		email = data_json.get("email", "")
# 		address_1 = data_json.get("address_1", "")
# 		city = data_json.get("city", "")
# 		province = data_json.get("province", "")
# 		country = data_json.get("country", "")
# 		vehicle_company = data_json.get("vehicle_company", "")
# 		company_branch = data_json.get("company_branch", "")
# 		booking_slot = data_json.get("booking_slot", "")
# 		plate_number = str(data_json.get("plate_number", "")).strip()
# 		vehicle_colour = data_json.get("vehicle_colour", "")
# 		vehicle_type = data_json.get("vehicle_type", "")
#
# 		if not phone or not plate_number:
# 			return {
# 				"status": "error",
# 				"message": "Phone and Plate Number are required."
# 			}
#
# 		# Check if lead already exists
# 		search_data = frappe.db.exists("Lead", {"plate_number": plate_number, "phone": phone})
# 		if search_data:
# 			return {
# 				"status": "exists",
# 				"message": f"Lead already exists with this plate number: {plate_number} and phone: {phone}."
# 			}
#
# 		# Create Lead
# 		lead = frappe.new_doc("Lead")
# 		lead.first_name = first_name
# 		lead.middle_name = middle_name
# 		lead.last_name = last_name
# 		lead.email_id = email
# 		lead.mobile_no = phone
# 		lead.phone = phone
# 		lead.company = company_branch
# 		lead.plate_number = plate_number
# 		lead.vehicle_colour = vehicle_colour
# 		lead.vehicle_type = vehicle_type
# 		lead.booking_slot = booking_slot
#
# 		# Create Vehicle Company if not exists
# 		if vehicle_company:
# 			vehicle_company_search = frappe.db.exists("Vehicle Company", {"vehicle_company": vehicle_company})
# 			if not vehicle_company_search:
# 				new_vehicle_company = frappe.new_doc("Vehicle Company")
# 				new_vehicle_company.vehicle_company = vehicle_company
# 				lead.vehicle_company = vehicle_company
# 				new_vehicle_company.insert(ignore_permissions=True)
# 				frappe.db.commit()
#
# 		lead.insert(ignore_permissions=True)
# 		frappe.db.commit()
#
# 		# Create Address linked to the Lead
# 		address = frappe.new_doc("Address")
# 		address.address_title = name or first_name
# 		address.address_line1 = address_1
# 		address.city = city
# 		address.state = province
# 		address.country = country
# 		address.append("links", {
# 			"link_doctype": "Lead",
# 			"link_name": lead.name
# 		})
# 		address.insert(ignore_permissions=True)
# 		frappe.db.commit()
#
# 		return {
# 			"status": "success",
# 			"message": f"Lead and Address created for {name}",
# 			"lead": lead.name,
# 			"address": address.name,
# 			"phone": lead.phone,
# 			"plate_number": lead.plate_number
# 		}
#
# 	except Exception as e:
# 		frappe.log_error(title="Lead Creation Failed", message=frappe.get_traceback())
# 		return {
# 			"status": "error",
# 			"message": f"Error occurred: {str(e)}"
# 		}


import frappe
import json

@frappe.whitelist(allow_guest=True)
def save_data():
	try:
		if not frappe.db.exists("DocType", "Lead"):
			return {
				"status": "error",
				"message": "Lead DocType does not exist."
			}

		data = frappe.request.get_data(as_text=True)
		if not data:
			return {
				"status": "error",
				"message": "No data received."
			}

		data_json = json.loads(data)

		# Extract and sanitize input
		name = str(data_json.get("name", "")).strip()
		name_parts = name.split()
		first_name = name_parts[0] if name_parts else ""
		last_name = name_parts[-1] if len(name_parts) > 1 else ""
		middle_name = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""

		phone = str(data_json.get("phone", "")).strip()
		email = data_json.get("email", "")
		address_1 = data_json.get("address_1", "")
		city = data_json.get("city", "")
		province = data_json.get("province", "")
		country = data_json.get("country", "")
		vehicle_company = data_json.get("vehicle_company", "")
		company_branch = data_json.get("company_branch", "")
		booking_slot = data_json.get("booking_slot", "")
		plate_number = str(data_json.get("plate_number", "")).strip()
		vehicle_colour = data_json.get("vehicle_colour", "")
		vehicle_type = data_json.get("vehicle_type", "")

		if not phone or not plate_number:
			return {
				"status": "error",
				"message": "Phone and Plate Number are required."
			}

		# Check if lead already exists
		search_data = frappe.db.exists("Lead", {"plate_number": plate_number, "phone": phone})
		if search_data:
			return {
				"status": "exists",
				"message": f"Lead already exists with this plate number: {plate_number} and phone: {phone}."
			}

		# Create Lead
		lead = frappe.new_doc("Lead")
		lead.first_name = first_name
		lead.middle_name = middle_name
		lead.last_name = last_name
		lead.email_id = email
		lead.mobile_no = phone
		lead.phone = phone
		lead.company = company_branch
		lead.plate_number = plate_number
		lead.vehicle_colour = vehicle_colour
		lead.vehicle_type = vehicle_type
		lead.booking_slot = booking_slot

		# Create Vehicle Company if not exists
		if vehicle_company:
			vehicle_company_search = frappe.db.exists("Vehicle Company", {"vehicle_company": vehicle_company})
			if not vehicle_company_search:
				new_vehicle_company = frappe.new_doc("Vehicle Company")
				new_vehicle_company.vehicle_company = vehicle_company
				lead.vehicle_company = vehicle_company
				new_vehicle_company.insert(ignore_permissions=True)
				frappe.db.commit()

		lead.insert(ignore_permissions=True)
		frappe.db.commit()

		# Send booking confirmation email
		if email:
			frappe.sendmail(
				recipients=email,
				subject="Booking Confirmation",
				message=f"""
					<p>Dear {first_name},</p>
					<p>Thank you for your booking. We have successfully received your details.</p>
					<p><strong>Booking Details:</strong></p>
					<ul>
						<li>Plate Number: {plate_number}</li>
						<li>Vehicle Type: {vehicle_type}</li>
						<li>Vehicle Colour: {vehicle_colour}</li>
						<li>Booking Slot: {booking_slot}</li>
					</ul>
					<p>If you have any questions, feel free to contact us.</p>
					<p>Best regards,<br>Your Company Team</p>
				""",
				reference_doctype="Lead",
				reference_name=lead.name
			)

		# Create Address linked to the Lead
		address = frappe.new_doc("Address")
		address.address_title = name or first_name
		address.address_line1 = address_1
		address.city = city
		address.state = province
		address.country = country
		address.append("links", {
			"link_doctype": "Lead",
			"link_name": lead.name
		})
		address.insert(ignore_permissions=True)
		frappe.db.commit()

		return {
			"status": "success",
			"message": f"Lead and Address created for {name}",
			"lead": lead.name,
			"address": address.name,
			"phone": lead.phone,
			"plate_number": lead.plate_number
		}

	except Exception as e:
		frappe.log_error(title="Lead Creation Failed", message=frappe.get_traceback())
		return {
			"status": "error",
			"message": f"Error occurred: {str(e)}"
		}

