from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home
from odoo.addons.portal.controllers.portal import CustomerPortal, pager

class Home(Home):
    # pass
    def _login_redirect(self, uid, redirect=None):
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('feescollection.group_manager'):
            return '/web/'
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_user'):
            return'/web/'
        if  request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_portal'):
            return '/index/'
        return super(StudentDetails , self)._login_redirect(uid, redirect=redirect)

class StudentDetails(CustomerPortal):

    @http.route(['/index/'], type='http', auth="public", website=True)
    def user_reg(self, page=1, date_begin=None, date_end=None, sortby=None, **post):
        if request.httprequest.method == "POST":
            print(">>>>>>>>>>>>>", request.params)
        record = request.env['student.student'].sudo().search([("res_user","=",request.env.user.id)])
        return request.render('feescollection.index_1', {
            "record": record,
        })

    @http.route(['/my/test'], type='http', auth="public", website=True)
    def user_registration(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        if request.httprequest.method == "POST":
            if request.params.get('user_type') == "8":
                request.env["res.users"].sudo().create({
                    'login': request.params.get("txt_uname"),
                    'password': request.params.get('txt_password'),
                    'name': request.params.get("txt_uname"),
                    'groups_id': [(6, 0, [request.env.ref('base.group_portal').id])],
                })
            if request.params.get('user_type') == "1":

                partner = request.env['res.partner'].sudo().create({
                    'name': request.params.get("txt_uname"),
                    "email": request.params.get("txt_uname"),
                })

                currency = request.env['res.company'].browse(
                    request.params.get("state_id"))

                company = request.env['res.company'].sudo().create({
                    "name": request.params.get("txt_uname"),
                    "partner_id": partner.id,
                    "currency_id": currency.id,
                })

                request.env["res.users"].sudo().create({
                    'login': request.params.get("txt_uname"),
                    'password': request.params.get('txt_password'),
                    'name': request.params.get('txt_uname'),
                    'company_id': company.id,
                    'company_ids': [(4, company.id)],
                    'groups_id': [(6, 0, [request.env.ref('feescollection.manager_user').id])],
                })

            return request.redirect("/web/login")

        rec = request.env['res.currency'].sudo().search([])
        # pager = portal_pager(
        #     url="/my/tasks",
        #     url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby,
        #               # 'filterby': filterby, 'search_in': search_in, 'search': search},
        #               },
        #     # total=task_count,
        #     page=page,
        #     step=self._items_per_page)
        values = {}
        values.update({
            'date': date_begin,
            # 'date_end': date_end,
            # 'grouped_tasks': grouped_tasks,
            'page_name': 'task',
            # 'archive_groups': archive_groups,
            'default_url': '/my/tasks',
            'pager': pager,
            # 'searchbar_sortings': searchbar_sortings,
            # 'searchbar_groupby': searchbar_groupby,
            # 'searchbar_inputs': searchbar_inputs,
            # 'search_in': search_in,
            'sortby': sortby,
            # 'groupby': groupby,
            # 'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            # 'filterby': filterby
        })
        return request.render("feescollection.user_register", {"rec": rec,
                                                                   "values": values})


    @http.route(['/menu_item/'], type='http', auth="public", website=True)
    def new_try(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        return request.render('feescollection.menu_item')

    @http.route(['/payment/'], type='http', auth="public", website=True)
    def new_try(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        print(request.params,"\n\n\n")
        return request.render('feescollection.user_register')
