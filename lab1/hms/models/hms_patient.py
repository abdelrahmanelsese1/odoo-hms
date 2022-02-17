from odoo import models, fields,api
import re
from odoo.exceptions import UserError
from datetime import date

class Patient(models.Model):
    _name = 'hms.patient'
    _rec_name = "first_name"

    first_name = fields.Char()
    last_name = fields.Char()
    email = fields.Char()
    birth_date = fields.Date()
    CR_ratio = fields.Float()
    history = fields.Html()
    blood_type = fields.Selection([("a", "A"), ("b", "B"), ("ab", "AB"), ("o", "O")])
    PCR = fields.Boolean()
    Patient_image = fields.Image()
    address = fields.Text()
    age = fields.Integer(compute='_calc_age')
    state = fields.Selection([("undetermined", "Undetermined"), ("good",  "Good"), ("fair",  "Fair"),
                              ("serious", "Serious")])
    doctor_id = fields.Many2many(comodel_name='hms.doctor')
    department_id = fields.Many2one(comodel_name='hms.department')
    department_capacity = fields.Integer(related='department_id.capacity')
    department_name = fields.Char(related='department_id.department_name')
    doctor_name = fields.Char(related='doctor_id.first_name')
    log_history_ids = fields.One2many('log.history', 'patient_id')
    _sql_constraints = [
        ('Email_unique_constraint', 'UNIQUE(email)', 'This email already exist ')
    ]



    # email validation

    @api.constrains('email')
    def _email_validate(self):
        if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                        self.email):
            raise UserError('Please enter a valid email address')

    # age calculation from birthdate

    @api.depends('birth_date')
    def _calc_age(self):
        for record in self:
            if record.birth_date:
                record.age = date.today().year - record.birth_date.year
            else:
                record.age = 0

    def state_undetermined(self):
        self.state = 'undetermined'

    def state_good(self):
        self.state = 'good'

    def state_fair(self):
        self.state = 'fair'

    def state_serious(self):
        self.state = 'serious'

    @api.onchange('age')
    def _age_onchange(self):
        if self.age<30 and self.age!=0:
            self.PCR = True
            return{
                'warning': {
                    'title': 'Changed', 'message': 'PCR has been changed'
                }
            }

    # create a new log history

    def write(self, vals):
        if 'state' in vals:
            self.env['log.history'].create({
                'description': 'state changed to NEW_STATE',
                'patient_id': self.id,
            })
        super().write(vals)













