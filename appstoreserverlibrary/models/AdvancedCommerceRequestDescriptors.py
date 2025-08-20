# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from attr import define
import attr
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceRequestDescriptors:
    """
    The display name and description of a subscription product.
    
    https://developer.apple.com/documentation/advancedcommerceapi/descriptors
    """
    
    description: str = attr.ib()
    displayName: str = attr.ib()

    def __attrs_post_init__(self):
        self.description = AdvancedCommerceValidationUtils.validate_description(self.description)
        self.displayName = AdvancedCommerceValidationUtils.validate_display_name(self.displayName)