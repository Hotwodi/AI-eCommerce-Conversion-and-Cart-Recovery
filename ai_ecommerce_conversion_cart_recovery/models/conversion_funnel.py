from odoo import api, fields, models


class EccConversionFunnel(models.Model):
    _name = 'ecc.conversion.funnel'
    _description = 'Conversion Funnel Analytics'
    _inherit = ['mail.thread']
    _order = 'id desc'

    name = fields.Char(string='Reference', required=True, default='New', tracking=True)
    period = fields.Char(string='Period', help='e.g. 2026-01, Q1-2026', tracking=True)
    visitors = fields.Integer(string='Visitors', default=0)
    product_views = fields.Integer(string='Product Views', default=0)
    add_to_cart = fields.Integer(string='Add to Cart', default=0)
    checkout_started = fields.Integer(string='Checkout Started', default=0)
    orders_completed = fields.Integer(string='Orders Completed', default=0)
    conversion_rate = fields.Float(
        string='Conversion Rate (%)',
        compute='_compute_conversion_rate',
        store=True,
    )
    ai_drop_off_stage = fields.Selection(
        [
            ('visitors', 'Visitors'),
            ('product_views', 'Product Views'),
            ('add_to_cart', 'Add to Cart'),
            ('checkout_started', 'Checkout Started'),
        ],
        string='AI Drop-off Stage',
        help='AI-detected stage with the highest drop-off',
    )
    ai_recommendation = fields.Text(string='AI Recommendation')

    @api.depends('visitors', 'orders_completed')
    def _compute_conversion_rate(self):
        for rec in self:
            if rec.visitors and rec.visitors > 0:
                rec.conversion_rate = (rec.orders_completed / rec.visitors) * 100.0
            else:
                rec.conversion_rate = 0.0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('ecc.conversion.funnel') or 'New'
        return super().create(vals_list)
