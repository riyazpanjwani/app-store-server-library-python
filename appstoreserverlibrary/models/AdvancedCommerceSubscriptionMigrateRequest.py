# Copyright (c) 2023 Apple Inc. Licensed under MIT License.

from typing import List, Optional
from attr import define
import attr
from .AdvancedCommerceRequest import AdvancedCommerceRequest
from .AdvancedCommerceDescriptors import AdvancedCommerceDescriptors
from .AdvancedCommerceSubscriptionMigrateItem import AdvancedCommerceSubscriptionMigrateItem
from .AdvancedCommerceSubscriptionMigrateRenewalItem import AdvancedCommerceSubscriptionMigrateRenewalItem
from .AdvancedCommerceRequestInfo import AdvancedCommerceRequestInfo
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionMigrateRequest(AdvancedCommerceRequest):
    """
    The subscription details you provide to migrate a subscription from In-App Purchase to the Advanced Commerce API.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmigraterequest
    """
    
    descriptors: AdvancedCommerceDescriptors = attr.field()
    items: List[AdvancedCommerceSubscriptionMigrateItem] = attr.field()
    targetProductId: str = attr.field()
    taxCode: str = attr.field()
    renewalItems: Optional[List[AdvancedCommerceSubscriptionMigrateRenewalItem]] = attr.field(default=None)
    storefront: Optional[str] = attr.field(default=None)
    
    def __init__(self, requestInfo: AdvancedCommerceRequestInfo, items: List[AdvancedCommerceSubscriptionMigrateItem],
                 targetProductId: str, descriptors: AdvancedCommerceDescriptors, taxCode: str):
        super().__init__(requestInfo)
        self.items = items
        self.targetProductId = AdvancedCommerceValidationUtils.validate_target_product_id(targetProductId)
        self.descriptors = descriptors
        self.taxCode = AdvancedCommerceValidationUtils.validate_tax_code(taxCode)
    
    def self(self):
        return self