from odoo import api, fields, models


class EccConversionInsight(models.Model):
    _name = 'ecc.conversion.insight'
    _description = 'Conversion Insights'
    _inherit = ['mail.thread']
    _order = 'id desc'

    name = fields.Char(string='Reference', required=True, default='New', tracking=True)
    period = fields.Char(string='Period', help='e.g. 2026-01, Q1-2026', tracking=True)
    insight_type = fields.Selection(
        [
            ('traffic', 'Traffic'),
            ('product', 'Product'),
            ('checkout', 'Checkout'),
            ('payment', 'Payment'),
            ('shipping', 'Shipping'),
        ],
        string='Insight Type',
        default='traffic',
        tracking=True,
    )
    metric_value = fields.Float(string='Metric Value')
    ai_analysis = fields.Text(string='AI Analysis')
    recommendation = fields.Text(string='Recommendation')
    impact_level = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        string='Impact Level',
        default='medium',
        tracking=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('ecc.conversion.insight') or 'New'
        return super().create(vals_list)
