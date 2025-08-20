# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional
from attr import define
import attr
from .AdvancedCommerceRequestOffer import AdvancedCommerceRequestOffer
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils


@define
class AdvancedCommerceSubscriptionCreateItem:
    """
    The data that describes a subscription item.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreateitem
    """
    
    description: str = attr.field()
    displayName: str = attr.field()
    price: int = attr.field()
    SKU: str = attr.field()
    offer: Optional[AdvancedCommerceRequestOffer] = attr.field(default=None)

    def __attrs_post_init__(self):
        self.description = AdvancedCommerceValidationUtils.validate_description(self.description)
        self.displayName = AdvancedCommerceValidationUtils.validate_display_name(self.displayName)
        self.price = AdvancedCommerceValidationUtils.validate_price(self.price)
        self.SKU = AdvancedCommerceValidationUtils.validate_sku(self.SKU)