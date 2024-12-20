# -*- coding: utf-8 -*-
from odoo import models, api, fields, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    service_id = fields.One2many('employee.service.line', 'employee_id')
