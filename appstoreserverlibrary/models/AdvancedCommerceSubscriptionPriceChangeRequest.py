# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import List, Optional
from attr import define
import attr
from .AdvancedCommerceRequest import AdvancedCommerceRequest
from .AdvancedCommerceSubscriptionPriceChangeItem import AdvancedCommerceSubscriptionPriceChangeItem
from .AdvancedCommerceRequestInfo import AdvancedCommerceRequestInfo
from AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionPriceChangeRequest(AdvancedCommerceRequest):
    """
    The request data your app provides to change the price of items in an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangerequest
    """
    
    items: List[AdvancedCommerceSubscriptionPriceChangeItem] = attr.field()
    currency: Optional[str] = attr.field(default=None)
    storefront: Optional[str] = attr.field(default=None)
    
    def __init__(self, requestInfo: AdvancedCommerceRequestInfo, items: List[AdvancedCommerceSubscriptionPriceChangeItem]):
        super().__init__(requestInfo)
        self.items = items
        if self.currency is not None:
            self.currency = AdvancedCommerceValidationUtils.validate_currency(self.currency)
    
    def self(self):
        return self