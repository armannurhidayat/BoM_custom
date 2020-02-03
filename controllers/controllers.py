# -*- coding: utf-8 -*-
from odoo import http

# class VitAddedDesc(http.Controller):
#     @http.route('/vit_added_desc/vit_added_desc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_added_desc/vit_added_desc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_added_desc.listing', {
#             'root': '/vit_added_desc/vit_added_desc',
#             'objects': http.request.env['vit_added_desc.vit_added_desc'].search([]),
#         })

#     @http.route('/vit_added_desc/vit_added_desc/objects/<model("vit_added_desc.vit_added_desc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_added_desc.object', {
#             'object': obj
#         })