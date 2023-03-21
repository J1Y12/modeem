# -*- coding: utf-8 -*-
# Part of Modeem. See LICENSE file for full copyright and licensing details.

from modeem import fields, models


class MailShortcode(models.Model):
    """ Shortcode
        Canned Responses, allowing the user to defined shortcuts in its message. Should be applied before storing message in database.
        Emoji allowing replacing text with image for visual effect. Should be applied when the message is displayed (only for final rendering).
        These shortcodes are global and are available for every user.
    """

    _name = 'mail.shortcode'
    _description = 'Canned Response / Shortcode'
    source = fields.Char('Shortcut', required=True, index='trigram',
        help="Shortcut that will automatically be substituted with longer content in your messages."
             " Type ':' followed by the name of your shortcut (e.g. :hello) to use in your messages.")
    substitution = fields.Text('Substitution', required=True,
        help="Content that will automatically replace the shortcut of your choosing. This content can still be adapted before sending your message.")
    description = fields.Char('Description')
    message_ids = fields.Many2one('mail.message', string="Messages", store=False)