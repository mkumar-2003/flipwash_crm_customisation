import frappe
from datetime import datetime, timedelta

# @frappe.whitelist()
# def notify_upcoming_bookings():
# 	print("SDbsdjvbskjdvbsdkvj")
#
# 	leads = frappe.get_all(
# 		"Lead",
# 		filters={"status": "Opportunity"},
# 		fields=["name", "lead_name", "booking_slot"]
# 	)
# 	print(leads, "kkkkkkkkkkkkkkk")
#
# 	for lead in leads:
# 		print(lead.booking_slot, "ggggggggggggggggggg")
# 		if isinstance(lead.booking_slot, datetime):
# 			booking_dt = lead.booking_slot
# 		else:
# 			booking_dt = datetime.strptime(lead.booking_slot, "%Y-%m-%d %H:%M:%S")
#
# 		added_time = timedelta(hours=14, minutes=30)
# 		new_datetime = booking_dt + added_time
# 		system_now = datetime.now()
# 		time_diff = system_now - new_datetime
# 		one_hour = timedelta(hours=1)
#
# 		booking_date = booking_dt.date()
# 		system_date = datetime.now().date()
# 		if booking_date == system_date:
# 			if abs(time_diff) >= one_hour:
# 				notification = frappe.get_doc({
# 					"doctype": "Notification Log",
# 					"subject": f"📅 Upcoming Booking: {lead.lead_name} at {new_datetime}",
# 					"for_user": "Administrator",
# 					"type": "Alert",
# 					"document_type": "Lead",
# 					"document_name": lead.name,
# 					"from_user": "Administrator",
# 					"email_content": (
# 						f"Reminder: Booking for lead '{lead.lead_name}' "
# 						f"is scheduled for {new_datetime}."
# 					)
# 				})
# 				notification.insert(ignore_permissions=True)
# 				frappe.db.commit()

@frappe.whitelist()
def notify_upcoming_bookings():
	print("Function triggered")

	leads = frappe.get_all(
		"Lead",
		filters={"status": "Opportunity"},
		fields=["name", "lead_name", "booking_slot"]
	)
	print(f"Fetched leads: {leads}")

	for lead in leads:
		print(f"Processing lead: {lead.name} with booking slot: {lead.booking_slot}")

		# Parse booking_slot to datetime
		try:
			if isinstance(lead.booking_slot, datetime):
				booking_dt = lead.booking_slot
			else:
				booking_dt = datetime.strptime(lead.booking_slot, "%Y-%m-%d %H:%M:%S")
		except Exception as e:
			print(f"Error parsing booking_slot for lead {lead.name}: {e}")
			continue

		# Extract date and time from booking_slot
		booking_date = booking_dt.date()
		booking_time = booking_dt.time()

		# Current system date and time
		system_dt = datetime.now()
		system_date = system_dt.date()
		system_time = system_dt.time()

		print(f"Lead: {lead.name}")
		print(f"Booking Date: {booking_date}, Time (24hr): {booking_time}")
		print(f"System Date: {system_date}, Time (24hr): {system_time}")

		if booking_date == system_date and booking_time >= system_time:
			notification = frappe.get_doc({
				"doctype": "Notification Log",
				"subject": f"📅 Upcoming Booking: {lead.lead_name} at {booking_time}",
				"for_user": "Administrator",
				"type": "Alert",
				"document_type": "Lead",
				"document_name": lead.name,
				"from_user": "Administrator",
				"email_content": (
					f"Reminder: Booking for lead '{lead.lead_name}' "
					f"is scheduled for {booking_time}."
				)
			})
			notification.insert(ignore_permissions=True)
			frappe.db.commit()

@frappe.whitelist()
def today_opportunity_booking_slot():
    system_date = datetime.now().date()

    leads = frappe.get_all(
        "Lead",
        filters={"status": "Opportunity"},
        fields=["name", "lead_name", "booking_slot"]
    )

    today_leads = []
    for lead in leads:
        if not lead.booking_slot:
            continue

        # Convert string to datetime if necessary
        if isinstance(lead.booking_slot, str):
            booking_dt = datetime.strptime(lead.booking_slot, "%Y-%m-%d %H:%M:%S")
        else:
            booking_dt = lead.booking_slot

        # Check if booking date is today
        if booking_dt.date() == system_date:
            today_leads.append(lead)

    return {
        "value": len(today_leads),
        "fieldtype": "Int",
        "route": ["List", "Lead", "List", {
            "status": "Opportunity",
            "booking_slot": [">=", f"{system_date} 00:00:00"]
        }],
        "label": "Today's Opportunity Bookings"
    }

