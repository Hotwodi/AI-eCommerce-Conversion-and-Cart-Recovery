from odoo import api, fields, models


class EccAbandonedCart(models.Model):
    _name = 'ecc.abandoned.cart'
    _description = 'Abandoned Cart Tracking'
    _inherit = ['mail.thread']
    _order = 'abandoned_date desc'

    name = fields.Char(string='Cart Reference', required=True, default='New', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=True)
    cart_total = fields.Monetary(string='Cart Total', currency_field='currency_id', tracking=True)
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
    cart_items_count = fields.Integer(string='Items Count', default=0)
    abandoned_date = fields.Datetime(string='Abandoned Date', default=fields.Datetime.now, tracking=True)
    recovery_email_sent = fields.Boolean(string='Recovery Email Sent', default=False)
    recovery_email_date = fields.Datetime(string='Recovery Email Date')
    recovered = fields.Boolean(string='Recovered', default=False)
    recovered_date = fields.Datetime(string='Recovered Date')
    ai_recovery_probability = fields.Float(
        string='AI Recovery Probability',
        help='AI-estimated probability (0-100) that this cart will be recovered',
    )
    state = fields.Selection(
        [
            ('abandoned', 'Abandoned'),
            ('email_sent', 'Email Sent'),
            ('recovered', 'Recovered'),
            ('lost', 'Lost'),
        ],
        string='State',
        default='abandoned',
        tracking=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('ecc.abandoned.cart') or 'New'
        return super().create(vals_list)

    def action_send_recovery_email(self):
        for rec in self:
            rec.write({
                'recovery_email_sent': True,
                'recovery_email_date': fields.Datetime.now(),
                'state': 'email_sent',
            })

    def action_mark_recovered(self):
        for rec in self:
            rec.write({
                'recovered': True,
                'recovered_date': fields.Datetime.now(),
                'state': 'recovered',
            })

    def action_mark_lost(self):
        for rec in self:
            rec.write({'state': 'lost'})
