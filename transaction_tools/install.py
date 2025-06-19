# apps/transaction_tools/transaction_tools/install.py
import frappe
import json
import os

def after_install():
    path = os.path.join(
        frappe.get_app_path("transaction_tools"),
        "workspace", "transaction_deletion", "transaction_deletion.json"
    )

    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
            if not frappe.db.exists("Workspace", data["name"]):
                frappe.get_doc(data).insert(ignore_permissions=True)
                frappe.db.commit()
