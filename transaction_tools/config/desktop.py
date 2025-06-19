# apps/transaction_tools/transaction_tools/config/desktop.py
from frappe import _

def get_data():
    return [
        {
            "module_name": "Transaction Tools",
            "type": "module",
            "label": _("Transaction Tools"),
            "color": "#1abc9c",
            "icon": "octicon octicon-trashcan",  # or any preferred icon
            "link": "workspace/transaction-deletion",  # 👈 custom workspace
            "category": "Modules",
        }
    ]
