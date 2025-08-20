# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from abc import ABC, abstractmethod
from typing import Optional
from attr import define
import attr
from .AdvancedCommerceRequest import AdvancedCommerceRequest
from .AdvancedCommerceRequestInfo import AdvancedCommerceRequestInfo


@define
class AbstractAdvancedCommerceInAppRequest(AdvancedCommerceRequest, ABC):
    """
    Abstract base class for Advanced Commerce in-app requests.
    """
    
    operation: str = attr.field()
    version: str = attr.field()
    
    def __init__(self, operation: str, version: str, requestInfo: AdvancedCommerceRequestInfo):
        super().__init__(requestInfo)
        self.operation = operation
        self.version = version
    
    @abstractmethod
    def self(self):
        """Return self for method chaining."""
        pass