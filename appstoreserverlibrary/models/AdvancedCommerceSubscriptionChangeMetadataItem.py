# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional

from attr import define
import attr

from .AdvancedCommerceEffective import AdvancedCommerceEffective
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionChangeMetadataItem:
    """
    The data your app provides to change the metadata of an item in an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadataitem
    """
    
    effective: AdvancedCommerceEffective = attr.ib()
    """
    A value that indicates when the change takes effect.
    
    https://developer.apple.com/documentation/advancedcommerceapi/effective
    """
    
    SKU: Optional[str] = attr.ib(default=None)
    """
    The SKU identifier for the item. Maximum length: 128 characters.
    """
    
    currentSKU: Optional[str] = attr.ib(default=None)
    """
    The current SKU identifier for the item. Maximum length: 128 characters.
    """
    
    description: Optional[str] = attr.ib(default=None)
    """
    The description of the item. Maximum length: 45 characters.
    """
    
    displayName: Optional[str] = attr.ib(default=None)
    """
    The display name of the item. Maximum length: 30 characters.
    """

    def __attrs_post_init__(self):
        if self.SKU is not None:
            self.SKU = AdvancedCommerceValidationUtils.validate_sku(self.SKU)
        if self.currentSKU is not None:
            self.currentSKU = AdvancedCommerceValidationUtils.validate_sku(self.currentSKU)
        if self.description is not None:
            self.description = AdvancedCommerceValidationUtils.validate_description(self.description)
        if self.displayName is not None:
            self.displayName = AdvancedCommerceValidationUtils.validate_display_name(self.displayName)