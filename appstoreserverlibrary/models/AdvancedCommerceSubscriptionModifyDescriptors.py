# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional
from attr import define
import attr
from .AdvancedCommerceEffective import AdvancedCommerceEffective
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceSubscriptionModifyDescriptors:
    """
    The data your app provides to change the description and display name of an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifydescriptors
    """
    
    effective: AdvancedCommerceEffective = attr.field()
    description: Optional[str] = attr.field(default=None)
    displayName: Optional[str] = attr.field(default=None)

    def __attrs_post_init__(self):
        if self.description is not None:
            self.description = AdvancedCommerceValidationUtils.validate_description(self.description)
        if self.displayName is not None:
            self.displayName = AdvancedCommerceValidationUtils.validate_display_name(self.displayName)