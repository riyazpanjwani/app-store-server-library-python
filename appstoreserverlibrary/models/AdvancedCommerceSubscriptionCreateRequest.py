# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

import re
from typing import List, Optional
from attr import define
import attr
from .AbstractAdvancedCommerceInAppRequest import AbstractAdvancedCommerceInAppRequest
from .AdvancedCommerceDescriptors import AdvancedCommerceDescriptors
from .AdvancedCommerceSubscriptionCreateItem import AdvancedCommerceSubscriptionCreateItem
from .AdvancedCommercePeriod import AdvancedCommercePeriod
from .AdvancedCommerceRequestInfo import AdvancedCommerceRequestInfo
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils


@define
class AdvancedCommerceSubscriptionCreateRequest(AbstractAdvancedCommerceInAppRequest):
    """
    The metadata your app provides when a customer purchases an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreaterequest
    """
    
    currency: str = attr.field()
    descriptors: AdvancedCommerceDescriptors = attr.field()
    items: List[AdvancedCommerceSubscriptionCreateItem] = attr.field()
    period: AdvancedCommercePeriod = attr.field()
    taxCode: str = attr.field()
    previousTransactionId: Optional[str] = attr.field(default=None)
    storefront: Optional[str] = attr.field(default=None)
    
    OPERATION = "CREATE_SUBSCRIPTION"
    VERSION = "1"

    def __init__(self, requestInfo: AdvancedCommerceRequestInfo):
        super().__init__(self.OPERATION, self.VERSION, requestInfo)
    
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        
        if self.currency is not None:
            self.currency = AdvancedCommerceValidationUtils.validate_currency(self.currency)
        if self.taxCode is not None:
            self.taxCode = AdvancedCommerceValidationUtils.validate_tax_code(self.taxCode)
        if self.previousTransactionId is not None:
            self.previousTransactionId = AdvancedCommerceValidationUtils.validate_transaction_id(self.previousTransactionId)
    
    def self(self):
        return self