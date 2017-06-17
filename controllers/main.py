# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import json

from odoo import http
from odoo.http import request
from odoo.tools import html_escape as escape


class BaiduMap(http.Controller):
    '''
    This class generates on-the-fly partner maps that can be reused in every
    website page. To do so, just use an ``<iframe ...>`` whose ``src``
    attribute points to ``/google_map`` (this controller generates a complete
    HTML5 page).

    URL query parameters:
    - ``partner_ids``: a comma-separated list of ids (partners to be shown)
    - ``partner_url``: the base-url to display the partner
        (eg: if ``partner_url`` is ``/partners/``, when the user will click on
        a partner on the map, it will be redirected to <myodoo>.com/partners/<id>)

    In order to resize the map, simply resize the ``iframe`` with CSS
    directives ``width`` and ``height``.
    '''

    @http.route(['/baidu_map'], type='http', auth="public", website=True)
    def baidu_map(self, *arg, **post):
        testValue = post.get('testValue', '')
        print("testvalue--------->%s" % testValue)
        values = {
            'partner_url': 'partner_url',
            'partner_data': 'partner_data',
            'testValue': testValue,
        }
        return request.render("baidu_map.baidu_map", values)
