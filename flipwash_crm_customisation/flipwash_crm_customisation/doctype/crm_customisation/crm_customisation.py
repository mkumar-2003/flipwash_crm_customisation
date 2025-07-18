# Copyright (c) 2025, Abhishek Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta
from erpnext.crm.doctype.lead.lead import Lead


class CRMLeadInherit(Lead):
	def before_save(self):
		if not self.booking_slot:
			return
		booking_dt = datetime.strptime(self.booking_slot, "%Y-%m-%d %H:%M:%S")
		added_time = timedelta(hours=14, minutes=30)
		new_datetime = booking_dt + added_time
		system_now = datetime.now()
		time_diff = system_now - new_datetime
		one_hour = timedelta(hours=1)
		if new_datetime <= system_now:
			frappe.throw(
				"Validation Error: Please do not select a past date or time for the booking slot.")

		if abs(time_diff) <= one_hour:
			frappe.throw(
				"Validation Error: Booking a slot more than 1 hour from the current time is not allowed.")

		#


class CRMCustomisation(Document):
	pass
