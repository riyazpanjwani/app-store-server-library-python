# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from attr import define
import attr

from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionModifyRemoveItem:
    """
    The data your app provides to remove an item from an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyremoveitem
    """
    
    SKU: str = attr.field()

    def __attrs_post_init__(self):
        self.SKU = AdvancedCommerceValidationUtils.validate_sku(self.SKU)