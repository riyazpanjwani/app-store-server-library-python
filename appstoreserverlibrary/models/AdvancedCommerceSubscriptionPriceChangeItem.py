# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional

from attr import define
import attr

from .AbstractAdvancedCommerceItem import AbstractAdvancedCommerceItem
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionPriceChangeItem(AbstractAdvancedCommerceItem):
    """
    The data your app provides to change the price of an item in an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangeitem
    """
    
    price: Optional[int] = attr.ib(default=None)
    
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        if self.price is not None:
            self.price = AdvancedCommerceValidationUtils.validate_price(self.price)
    
    def self(self):
        """Return self for method chaining."""
        return self