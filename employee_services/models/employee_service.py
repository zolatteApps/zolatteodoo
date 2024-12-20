# -*- coding: utf-8 -*-
from odoo import fields, models, api


class employeeService(models.Model):
    _name = 'employee.service'
    _description = 'employee Service'
    _rec_name = 'name'

    name = fields.Char(string="Service", help='Specify the name of service')
    image_720 = fields.Image(string='Image', max_width=720, max_height=720)
    employee_ids = fields.One2many("hr.employee", "service_id", string="Employee", compute="_compute_employee_ids")

    @api.depends('name')
    def _compute_employee_ids(self):
        for record in self:
            if record.name:
                services = self.env['employee.service.line'].search(
                    [('name', '=', record.id), ('status', '=', 'approved')])
                record.employee_ids = [(6, 0, services.employee_id.ids)]
            else:
                record.employee_ids = [(5, 0, 0)]
