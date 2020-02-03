# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class ProdukJadi(models.Model):
    _name = 'mrp.bom'
    _inherit = 'mrp.bom'

    img = fields.Binary(
        string='Image',
        related='product_tmpl_id.image_medium',
    )

    video = fields.Binary(
        string='Video',
    )

    desc = fields.Text(
        string='Deskripsi'
    )

    date_added = fields.Date(
        string='Tanggal Added',
        default=lambda self:time.strftime("%Y-%m-%d"),
    )

    priority = fields.Selection(
        string='Rating',
        selection=[
	        ('0','0'),
	        ('1','1'),
	        ('2','2'),
	        ('3','3'),
	        ('4','4'),
	        ('5','5'),
        ]
    )


class ProdukJadiLine(models.Model):
    _name = 'mrp.bom.line'
    _inherit = 'mrp.bom.line'

    img = fields.Binary(
        string='Image',
        related='product_id.image_medium',
    )

    desc = fields.Text(
        string='Deskripsi',
    )

    harga = fields.Float(
        string='Harga',
        related='product_id.list_price',
    )