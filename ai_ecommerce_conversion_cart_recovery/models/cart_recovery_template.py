from odoo import api, fields, models


class EccCartRecoveryTemplate(models.Model):
    _name = 'ecc.cart.recovery.template'
    _description = 'Cart Recovery Email Templates'
    _inherit = ['mail.thread']
    _order = 'delay_hours'

    name = fields.Char(string='Template Name', required=True, tracking=True)
    template_type = fields.Selection(
        [
            ('first_reminder', 'First Reminder'),
            ('second_reminder', 'Second Reminder'),
            ('discount_offer', 'Discount Offer'),
            ('urgency', 'Urgency'),
        ],
        string='Template Type',
        default='first_reminder',
        tracking=True,
    )
    subject = fields.Char(string='Subject', required=True)
    body_html = fields.Html(string='Body', sanitize=True)
    delay_hours = fields.Integer(
        string='Delay (Hours)',
        default=24,
        help='Hours after abandonment before this email is sent',
    )
    discount_code = fields.Char(string='Discount Code')
    active = fields.Boolean(string='Active', default=True)
    sent_count = fields.Integer(string='Sent Count', default=0, readonly=True)
    recovered_count = fields.Integer(string='Recovered Count', default=0, readonly=True)
