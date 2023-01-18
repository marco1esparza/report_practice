# Copyright 2017-2021, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def print_journal_report(self):
        return self.env.ref('report_account_move_sitibt.print_account_move_report').report_action(self)
