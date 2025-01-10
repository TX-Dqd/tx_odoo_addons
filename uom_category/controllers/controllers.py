# -*- coding: utf-8 -*-
# from odoo import http


# class TxUomCategory(http.Controller):
#     @http.route('/tx_uom_category/tx_uom_category', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tx_uom_category/tx_uom_category/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tx_uom_category.listing', {
#             'root': '/tx_uom_category/tx_uom_category',
#             'objects': http.request.env['tx_uom_category.tx_uom_category'].search([]),
#         })

#     @http.route('/tx_uom_category/tx_uom_category/objects/<model("tx_uom_category.tx_uom_category"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tx_uom_category.object', {
#             'object': obj
#         })

