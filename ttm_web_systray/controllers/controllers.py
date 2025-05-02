# -*- coding: utf-8 -*-
# from odoo import http


# class TtmWebSystray(http.Controller):
#     @http.route('/ttm_web_systray/ttm_web_systray', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ttm_web_systray/ttm_web_systray/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ttm_web_systray.listing', {
#             'root': '/ttm_web_systray/ttm_web_systray',
#             'objects': http.request.env['ttm_web_systray.ttm_web_systray'].search([]),
#         })

#     @http.route('/ttm_web_systray/ttm_web_systray/objects/<model("ttm_web_systray.ttm_web_systray"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ttm_web_systray.object', {
#             'object': obj
#         })

