# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import List, Optional
from attr import define
import attr
from .AbstractAdvancedCommerceInAppRequest import AbstractAdvancedCommerceInAppRequest
from .AdvancedCommerceSubscriptionReactivateItem import AdvancedCommerceSubscriptionReactivateItem
from .AdvancedCommerceRequestInfo import AdvancedCommerceRequestInfo
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionReactivateInAppRequest(AbstractAdvancedCommerceInAppRequest):
    """
    The request data your app provides to reactivate an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest
    """
    
    transactionId: str = attr.field()
    items: Optional[List['AdvancedCommerceSubscriptionReactivateItem']] = attr.field(default=None)
    storefront: Optional[str] = attr.field(default=None)
    
    OPERATION = "REACTIVATE_SUBSCRIPTION"
    VERSION = "1"
    
    def __init__(self, requestInfo: AdvancedCommerceRequestInfo, transactionId: str):
        super().__init__(self.OPERATION, self.VERSION, requestInfo)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.transactionId = AdvancedCommerceValidationUtils.validate_transaction_id(self.transactionId)

    def self(self):
        return self