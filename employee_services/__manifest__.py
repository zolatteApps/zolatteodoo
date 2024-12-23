# -*- coding: utf-8 -*-

{
    'name': 'Employee Services',
    'author': 'Zolatte',
    'category': 'Tools',
    'version': '17.0.0.0',
    'website': 'https://zolatte.com/',
    'depends': ["hr"],
    'data': [
        "security/ir.model.access.csv",
        "views/employee_service_views.xml",
        "views/hr_employee_views.xml",
    ],
    'license': 'LGPL-3',
    "images": ["static/description/banner.jpg"],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}
