
from odoo import api, fields, models, api, _
from datetime import datetime
from odoo.exceptions import AccessError, UserError, ValidationError

class CrmInherit(models.Model):
    _inherit = "crm.lead"
    user_id = fields.Many2one('res.users', string="User")
    title = fields.Many2one(
        string='Title',
        comodel_name='survey.survey',
        ondelete='restrict',
    )
    state = fields.Many2one(string="Survey Stage", comodel_name='survey.survey')
    
    participation_line_ids = fields.One2many('survey.user_input', 'partner_id', 
                                    string='Participations', 
                                    related='partner_id.participation_line_ids')
    
    # def _compute_survey(self):
    #     result = []
    #     partner_id = self.env['crm.lead'].browse(self.partner_id)
    #     for rec in self.survey_line_ids:
    #         if rec.survey_line_ids.partner_id == self.partner_id:
    #             result.append(partner_id)
    #     return result

    survey_line_ids = fields.One2many('survey.survey', 'partner_id',
                             string='Surveys',
                             related='partner_id.survey_line_ids')
    
class ResPartner(models.Model):
    
    _inherit = 'res.partner'

    participation_line_ids = fields.One2many('survey.user_input', 'partner_id', string='Participations')
    survey_line_ids = fields.One2many('survey.survey', 'partner_id',
                             string='Surveys')

class SurveyInherit(models.Model):
    _inherit = "survey.survey"

    survey_id = fields.Many2one('crm.lead', string='Survey', ondelete='cascade') 
    partner_id = fields.Many2many('res.partner', string='Partners', relation='survey_partner_rel')


class SurveyUserInputInherit(models.Model):
    _inherit = "survey.user_input"

    agent_id = fields.Many2one(string='Agent', comodel_name='res.users', default=lambda self: self.env.user)





  