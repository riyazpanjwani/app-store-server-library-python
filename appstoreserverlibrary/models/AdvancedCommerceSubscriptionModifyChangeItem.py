# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional
from attr import define
import attr
from .AdvancedCommerceEffective import AdvancedCommerceEffective
from .AdvancedCommerceRequestOffer import AdvancedCommerceRequestOffer
from .AdvancedCommerceReason import AdvancedCommerceReason
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionModifyChangeItem:
    """
    The data your app provides to change items when it makes changes to an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifychangeitem
    """
    
    currentSKU: str = attr.field()
    description: str = attr.field()
    displayName: str = attr.field()
    effective: AdvancedCommerceEffective = attr.field()
    price: int = attr.field()
    reason: AdvancedCommerceReason = attr.field()
    SKU: str = attr.field()
    offer: Optional[AdvancedCommerceRequestOffer] = attr.field(default=None)
    proratedPrice: Optional[int] = attr.field(default=None)

    def __attrs_post_init__(self):
        self.description = AdvancedCommerceValidationUtils.validate_description(self.description)
        self.displayName = AdvancedCommerceValidationUtils.validate_display_name(self.displayName)
        self.price = AdvancedCommerceValidationUtils.validate_price(self.price)
        self.SKU = AdvancedCommerceValidationUtils.validate_sku(self.SKU)
        self.currentSKU = AdvancedCommerceValidationUtils.validate_sku(self.currentSKU)
        
        if self.proratedPrice is not None:
            self.proratedPrice = AdvancedCommerceValidationUtils.validate_price(self.proratedPrice)