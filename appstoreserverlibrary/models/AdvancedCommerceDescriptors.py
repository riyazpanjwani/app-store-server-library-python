# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Dict, Any, Optional

from attr import define
import attr
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceDescriptors:
    """
    The description and display name of the subscription to migrate to that you manage.
    """
    
    description: Optional[str] = attr.ib(default=None)
    displayName: Optional[str] = attr.ib(default=None)
    unknown_fields: Optional[Dict[str, Any]] = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.description is not None:
            self.description = AdvancedCommerceValidationUtils.validate_description(self.description)
        if self.displayName is not None:
            self.displayName = AdvancedCommerceValidationUtils.validate_display_name(self.displayName)