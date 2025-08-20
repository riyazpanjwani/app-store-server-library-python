# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import List, Optional
from attr import define
import attr
from .AbstractAdvancedCommerceInAppRequest import AbstractAdvancedCommerceInAppRequest
from .AdvancedCommerceSubscriptionModifyAddItem import AdvancedCommerceSubscriptionModifyAddItem
from .AdvancedCommerceSubscriptionModifyChangeItem import AdvancedCommerceSubscriptionModifyChangeItem
from .AdvancedCommerceSubscriptionModifyDescriptors import AdvancedCommerceSubscriptionModifyDescriptors
from .AdvancedCommerceSubscriptionModifyPeriodChange import AdvancedCommerceSubscriptionModifyPeriodChange
from .AdvancedCommerceSubscriptionModifyRemoveItem import AdvancedCommerceSubscriptionModifyRemoveItem
from .AdvancedCommerceRequestInfo import AdvancedCommerceRequestInfo
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionModifyInAppRequest(AbstractAdvancedCommerceInAppRequest):
    """
    The request data your app provides to make changes to an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyinapprequest
    """
    
    transactionId: str = attr.field()
    retainBillingCycle: bool = attr.field()
    addItems: Optional[List[AdvancedCommerceSubscriptionModifyAddItem]] = attr.field(default=None)
    changeItems: Optional[List[AdvancedCommerceSubscriptionModifyChangeItem]] = attr.field(default=None)
    currency: Optional[str] = attr.field(default=None)
    descriptors: Optional[AdvancedCommerceSubscriptionModifyDescriptors] = attr.field(default=None)
    periodChange: Optional[AdvancedCommerceSubscriptionModifyPeriodChange] = attr.field(default=None)
    removeItems: Optional[List[AdvancedCommerceSubscriptionModifyRemoveItem]] = attr.field(default=None)
    storefront: Optional[str] = attr.field(default=None)
    taxCode: Optional[str] = attr.field(default=None)
    
    OPERATION = "MODIFY_SUBSCRIPTION"
    VERSION = "1"
    
    def __init__(self, requestInfo: AdvancedCommerceRequestInfo, transactionId: str, retainBillingCycle: bool):
        super().__init__(self.OPERATION, self.VERSION, requestInfo)
        self.transactionId = transactionId
        self.retainBillingCycle = retainBillingCycle
    
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        
        self.transactionId = AdvancedCommerceValidationUtils.validate_transaction_id(self.transactionId)
        if self.taxCode is not None:
            self.taxCode = AdvancedCommerceValidationUtils.validate_tax_code(self.taxCode)
        if self.currency is not None:
            self.currency = AdvancedCommerceValidationUtils.validate_currency(self.currency)
    
    def self(self):
        return self