# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloExamenAsl(http.Controller):
#     @http.route('/modulo_examen_asl/modulo_examen_asl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_examen_asl/modulo_examen_asl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_examen_asl.listing', {
#             'root': '/modulo_examen_asl/modulo_examen_asl',
#             'objects': http.request.env['modulo_examen_asl.modulo_examen_asl'].search([]),
#         })

#     @http.route('/modulo_examen_asl/modulo_examen_asl/objects/<model("modulo_examen_asl.modulo_examen_asl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_examen_asl.object', {
#             'object': obj
#         })
