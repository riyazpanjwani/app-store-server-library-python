# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import List, Optional

from attr import define
import attr

from .AdvancedCommerceRequest import AdvancedCommerceRequest
from .AdvancedCommerceSubscriptionChangeMetadataDescriptors import AdvancedCommerceSubscriptionChangeMetadataDescriptors
from .AdvancedCommerceSubscriptionChangeMetadataItem import AdvancedCommerceSubscriptionChangeMetadataItem
from .AdvancedCommerceRequestInfo import AdvancedCommerceRequestInfo
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionChangeMetadataRequest(AdvancedCommerceRequest):
    """
    The request data your app provides to change the metadata of an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadatarequest
    """
    
    descriptors: Optional[AdvancedCommerceSubscriptionChangeMetadataDescriptors] = attr.ib(default=None)
    """
    The data your app provides to change the descriptors of an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadatadescriptors
    """
    
    items: Optional[List[AdvancedCommerceSubscriptionChangeMetadataItem]] = attr.ib(default=None)
    """
    The list of items to change metadata for in the subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadatitem
    """
    
    storefront: Optional[str] = attr.ib(default=None)
    """
    The storefront for the transaction.
    """
    
    taxCode: Optional[str] = attr.ib(default=None)
    """
    The tax code for this product.
    
    https://developer.apple.com/documentation/advancedcommerceapi/taxcode
    """
    
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        if self.taxCode is not None:
            self.taxCode = AdvancedCommerceValidationUtils.validate_tax_code(self.taxCode)