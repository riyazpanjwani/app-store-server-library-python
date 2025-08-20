# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from attr import define
import attr

from .AdvancedCommerceOfferPeriod import AdvancedCommerceOfferPeriod
from .AdvancedCommerceOfferReason import AdvancedCommerceOfferReason
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils
@define
class AdvancedCommerceRequestOffer:
    """
    A discount offer for an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/offer
    """
    
    period: AdvancedCommerceOfferPeriod = attr.ib()
    period_count: int = attr.ib()
    price: int = attr.ib()
    reason: AdvancedCommerceOfferReason = attr.ib()

    def __attrs_post_init__(self):
        self.price = AdvancedCommerceValidationUtils.validate_price(self.price)