# -*- coding: utf-8 -*-
from odoo import models, api, fields, _


class HrEmployeeService(models.Model):
    _name = 'employee.service.line'

    name = fields.Many2one('employee.service', 'Service')
    status = fields.Selection([('approved', 'Approved'), ('rejected', 'Rejected')], 'Status', readonly=True,
                              default=False)
    employee_id = fields.Many2one('hr.employee')

    def approve_service(self):
        for rec in self:
            rec.status = 'approved'

    def reject_service(self):
        for rec in self:
            rec.status = 'rejected'
