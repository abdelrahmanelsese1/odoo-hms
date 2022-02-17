from odoo import models, fields


class LogHistory(models.Model):
    _name = 'log.history'
    _rec_name = 'description'

    description = fields.Text()
    patient_id = fields.Many2one('hms.patient')
