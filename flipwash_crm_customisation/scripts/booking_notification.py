import frappe
from datetime import datetime, timedelta


@frappe.whitelist()
def notify_upcoming_bookings():
	print("SDbsdjvbskjdvbsdkvj")

	leads = frappe.get_all(
		"Lead",
		filters={"status": "Opportunity"},
		fields=["name", "lead_name", "booking_slot"]
	)
	print(leads, "kkkkkkkkkkkkkkk")

	for lead in leads:
		print(lead.booking_slot, "ggggggggggggggggggg")
		if isinstance(lead.booking_slot, datetime):
			booking_dt = lead.booking_slot
		else:
			booking_dt = datetime.strptime(lead.booking_slot, "%Y-%m-%d %H:%M:%S")

		added_time = timedelta(hours=14, minutes=30)
		new_datetime = booking_dt + added_time
		system_now = datetime.now()
		time_diff = system_now - new_datetime
		one_hour = timedelta(hours=1)

		booking_date = booking_dt.date()
		system_date = datetime.now().date()
		if booking_date == system_date:

			if abs(time_diff) >= one_hour:
				notification = frappe.get_doc({
					"doctype": "Notification Log",
					"subject": f"📅 Upcoming Booking: {lead.lead_name} at {new_datetime}",
					"for_user": "Administrator",
					"type": "Alert",
					"document_type": "Lead",
					"document_name": lead.name,
					"from_user": "Administrator",
					"email_content": (
						f"Reminder: Booking for lead '{lead.lead_name}' "
						f"is scheduled for {new_datetime}."
					)
				})
				notification.insert(ignore_permissions=True)
				frappe.db.commit()


@frappe.whitelist()
def today_opportunity_booking_slot():
	leads = frappe.get_all(
		"Lead",
		filters={"status": "Opportunity"},
		fields=["name", "lead_name", "booking_slot"]
	)
	print(leads, "kkkkkkkkkkkkkkk")
	count=0
	for lead in leads:
		if isinstance(lead.booking_slot, datetime):
			booking_dt = lead.booking_slot
		else:
			booking_dt = datetime.strptime(lead.booking_slot, "%Y-%m-%d %H:%M:%S")

		booking_date = booking_dt.date()
		system_date = datetime.now().date()

		if booking_date == system_date:
			count+=1
	return {
		"value": count

	}
