# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional
from attr import define
import attr
from .AbstractAdvancedCommerceItem import AbstractAdvancedCommerceItem


@define
class AdvancedCommerceSubscriptionReactivateItem(AbstractAdvancedCommerceItem):
    """
    The subscription item data your app provides to reactivate an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateitem
    """
    
    autoRenewStatus: Optional[bool] = attr.field(default=None)
    
    def __init__(self, SKU: str, description: str, displayName: str):
        super().__init__(SKU, description, displayName)
    
    def self(self):
        return self