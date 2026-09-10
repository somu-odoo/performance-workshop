from odoo import models, _
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        payment_before_delivery = self.env.ref(
            'sale_perf_killer.payment_term_before_delivery',
            raise_if_not_found=False,
        )
        for picking in self:
            sale = picking.sale_id
            if not sale:
                continue
            if sale.payment_term_id != payment_before_delivery:
                continue
            if not sale._is_fully_paid():
                raise ValidationError(
                    _(
                        "Delivery %(picking)s cannot be validated: "
                        "sale order %(order)s is set to 'Payment Before Delivery' "
                        "but has not been paid in full.\n"
                        "Please ensure the order is fully invoiced and paid "
                        "before processing the delivery.",
                        picking=picking.name,
                        order=sale.name,
                    )
                )
        return super().button_validate()
