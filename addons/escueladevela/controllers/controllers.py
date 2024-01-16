# -*- coding: utf-8 -*-
# from odoo import http


# class Escueladevela(http.Controller):
#     @http.route('/escueladevela/escueladevela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escueladevela/escueladevela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escueladevela.listing', {
#             'root': '/escueladevela/escueladevela',
#             'objects': http.request.env['escueladevela.escueladevela'].search([]),
#         })

#     @http.route('/escueladevela/escueladevela/objects/<model("escueladevela.escueladevela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escueladevela.object', {
#             'object': obj
#         })
