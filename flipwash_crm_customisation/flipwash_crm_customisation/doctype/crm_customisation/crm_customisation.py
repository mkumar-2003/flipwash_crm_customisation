# Copyright (c) 2025, Abhishek Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta
from erpnext.crm.doctype.lead.lead import Lead


class CRMLeadInherit(Lead):


	def before_save(self):
		if self.mobile_no:
			if not self.mobile_no.isdigit():
				frappe.throw("Mobile number should contain only digits.")

			if len(self.mobile_no) <= 10:
				frappe.throw("Please enter a valid mobile number with more than 10 digits.")

		if not self.booking_slot:
			return

		booking_dt = datetime.strptime(self.booking_slot, "%Y-%m-%d %H:%M:%S")

		booking_date = booking_dt.date()
		booking_time = booking_dt.time()

		system_now = datetime.now()
		system_time = system_now.time()
		system_date = system_now.date()

		booking_time_dt = datetime.combine(system_date, booking_time)
		system_time_dt = datetime.combine(system_date, system_time)

		time_diff = system_time_dt - booking_time_dt

		total_minutes = int(time_diff.total_seconds() / 60)
		print(total_minutes,"fffffffffffffffff")

		#
		if booking_dt <= system_now:
			frappe.throw(
				"Validation Error: Please do not select a past date or time for the booking slot."
			)
		if booking_date == system_date:
			if abs(total_minutes) <= 60:
				frappe.throw(
					"Validation Error: Booking a slot more than 1 hour from the current time is not allowed."
				)


class CRMCustomisation(Document):
	pass
