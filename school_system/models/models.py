# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Room(models.Model):
    _name = "school.class"

    name = fields.Char("", required=True)
    capacity = fields.Integer("Capacity")
    locacation = fields.Char("Location")


class Subject(models.Model):
    _name = "school.subject"
    name = fields.Char("Name")
    level = fields.Integer("Level", required=True)


class Teachers(models.Model):
    _name = "school.teacher"
    name = fields.Char("Name")

class Students(models.Model):
    _name = "school.student"
    name = fields.Char("Name")


class Parents(models.Model):
    _name = "school.parent"


class TimeTable(models.Model):
    _name = "school.timetable"
