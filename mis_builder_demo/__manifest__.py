# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MIS Builder Demo",
    "summary": """
        Demo addon for MIS Builder""",
    "version": "10.0.3.1.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/mis-builder",
    "depends": ["mis_builder_budget", "purchase"],
    "data": [
        "security/mis_committed_purchase.xml",
        "views/mis_committed_purchase.xml",
        "data/mis_report_style.xml",
        "data/mis_report.xml",
        "data/mis_budget.xml",
        "data/mis_report_instance.xml",
    ],
    "uninstall_hook": "uninstall_hook",
    "installable": True,
    "maintainers": ["sbidoul"],
    "development_status": "Alpha",
}
