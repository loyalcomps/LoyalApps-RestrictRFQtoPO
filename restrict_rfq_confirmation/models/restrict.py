# -*- coding: utf-8 -*-
#############################################################################
#
#    Loyal IT Solutions Pvt Ltd
#
#    Copyright (C) 2023-TODAY Loyal IT Solutions Pvt Ltd(<https://www.loyalitsolutions.com>).
#    Author: Loyal IT Solutions Pvt Ltd
#
#    You can modify it under the terms of the
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#

#   The coding is built and distributed among Odoo community in order to help
#    Odoo providers and users, but WITHOUT ANY WARRANTY.
#
#   For the copy of GNU PUBLIC LICENSE, please see
#   <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import models, fields, api
from odoo.exceptions import UserError

class ResUsers(models.Model):
    _inherit = 'res.users'
    # For adding a check box in user settings
    can_confirm_purchase = fields.Boolean('Can Confirm Purchase')


#The below code checks the user has access or not. If not, it will restrict
class PurchaseOrderConfirmation(models.Model):
    _inherit = 'purchase.order'

    def _check_access(self):
        if not self.env.user.can_confirm_purchase:
            raise UserError("You are not authorized to confirm purchase orders.")

    def button_confirm(self):
        self._check_access()
        return super(PurchaseOrderConfirmation, self).button_confirm()