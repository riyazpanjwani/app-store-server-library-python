# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from attr import define
import attr
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils


@define
class AbstractAdvancedCommerceItem(ABC):
    """
    Abstract base class for Advanced Commerce items.
    """
    
    SKU: str = attr.field()
    description: str = attr.field()
    displayName: str = attr.field()
    unknownFields: Optional[Dict[str, Any]] = attr.field(default=None)
    
    def __attrs_post_init__(self):
        if self.SKU is not None:
            self.SKU = AdvancedCommerceValidationUtils.validate_sku(self.SKU)
        if self.description is not None:
            self.description = AdvancedCommerceValidationUtils.validate_description(self.description)
        if self.displayName is not None:
            self.displayName = AdvancedCommerceValidationUtils.validate_display_name(self.displayName)
    
    @abstractmethod
    def self(self):
        """Return self for method chaining."""
        pass