# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Room(models.Model):
    _name = "school.class"

    name = fields.Char("", required=True)
    capacity = fields.Integer("Capacity")
    locacation = fields.Char("Location")

    student_ids = fields.One2many(
        comodel_name="school.student", inverse_name="room_id", string="Students"
    )

    @api.onchange("student_ids", "capacity")
    def check_capacity(self):
        num_students = len(self.student_ids.ids)
        if num_students > self.capacity:
            raise ValidationError("Cannot add Students more than capacity")


class Subject(models.Model):
    _name = "school.subject"
    name = fields.Char("Name")
    level = fields.Integer("Level", required=True)


class Partner(models.Model):
    _inherit = "res.partner"

    is_student = fields.Boolean("Student ?", default=False)


class Teachers(models.Model):
    _name = "school.teacher"
    name = fields.Char("Name")


class Students(models.Model):
    _name = "school.student"

    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one(
        "res.partner", "Partner", delegate=True, ondelete="cascade", required=True
    )

    room_id = fields.Many2one(comodel_name="school.class", string="Class")

    dob = fields.Date(string="D.O.B")

    age = fields.Integer(string="Age", compute="_compute_age", store=True)

    @api.depends("dob")
    def _compute_age(self):
        for student in self:
            date_of_now = datetime.datetime.now().date().year

            if student.dob:
                student.age = date_of_now - student.dob.year
            else:
                student.age = 0


class Parents(models.Model):
    _name = "school.parent"

    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one(
        "res.partner", "Partner", delegate=True, ondelete="cascade", required=True
    )


class TimeTable(models.Model):
    _name = "school.timetable"
