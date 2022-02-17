from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError


class CrmInherit(models.Model):
    _inherit = "res.partner"
    related_patient_id = fields.Many2one('hms.patient')

    @api.constrains('related_patient_id')
    def _patient_email_validate(self):
        if self.email == self.related_patient_id.email:
            raise ValidationError("email already exits in Patient Model, Please Choose another One")

    def unlink(self):
        if self.related_patient_id:
            raise UserError("this customer is linked to a patient , so you can not delete it")
        return super().unlink()
