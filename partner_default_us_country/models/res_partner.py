# Copyright 2018-2021 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    country_id = fields.Many2one(
        default=lambda self: self.env.ref('base.us')
    )


    @api.model
    def create(self, vals):
        """
        We need to set the USA as default country while
        creating the auth_signup module.
        In auth_signup module they are adding
        the 'no_reset_password=True' in context.
        If we find that in this create context
        we can set the county id default as USA.
        """
        if 'no_reset_password' in self._context and self._context.get('no_reset_password'):
            vals['country_id'] = self.env.ref('base.us').id
        return super(ResPartner,self).create(vals)
