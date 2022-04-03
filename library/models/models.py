# -*- coding: utf-8 -*-

from unicodedata import name
from odoo import models, fields, api


class Book(models.Model):
    _name = "library.book"
    _description = "The books table"

    name = fields.Char("Name", required=True)
    author = fields.Char("Author", required=True)
    publisher = fields.Char("Publiser", required=True)
    published_date = fields.Date("Published", required=True)

    series_ids = fields.One2many(
        string="Series", comodel_name="library.book.series", inverse_name="book_id"
    )


class BookSeries(models.Model):

    _name = "library.book.series"
    _description = "Series"

    name = fields.Char("Name")
    book_id = fields.Many2one("Book", "library.book")
