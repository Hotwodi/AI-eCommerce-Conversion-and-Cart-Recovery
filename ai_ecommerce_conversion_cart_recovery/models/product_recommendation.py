from odoo import api, fields, models


class EccProductRecommendation(models.Model):
    _name = 'ecc.product.recommendation'
    _description = 'AI Product Recommendations'
    _inherit = ['mail.thread']
    _order = 'ai_score desc'

    name = fields.Char(string='Reference', required=True, default='New', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=True)
    product_id = fields.Many2one('product.product', string='Product', tracking=True)
    recommendation_type = fields.Selection(
        [
            ('related', 'Related'),
            ('cross_sell', 'Cross-Sell'),
            ('up_sell', 'Up-Sell'),
            ('personalized', 'Personalized'),
        ],
        string='Recommendation Type',
        default='personalized',
        tracking=True,
    )
    ai_score = fields.Float(
        string='AI Score',
        help='AI confidence score (0-100) for this recommendation',
    )
    click_rate = fields.Float(string='Click Rate (%)', default=0.0)
    conversion_rate = fields.Float(string='Conversion Rate (%)', default=0.0)
    active = fields.Boolean(string='Active', default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('ecc.product.recommendation') or 'New'
        return super().create(vals_list)
