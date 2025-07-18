import frappe
from frappe.model.document import Document
from datetime import datetime

class FuelType(Document):
	pass
    # def validate(self):
    #     system_now = datetime.now()
    #     system_date = system_now.date()
    #     system_time_24 = system_now.strftime("%H:%M")
	#
    #     # Correct way to display all values in one message
    #     frappe.msgprint(f"System Date: {system_date} ------------ System Time (24hr): {system_time_24}")
