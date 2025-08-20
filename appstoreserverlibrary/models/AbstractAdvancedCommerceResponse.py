# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional
from attr import define
import attr


@define
class AbstractAdvancedCommerceAppResponse:
    """
    Abstract base class for Advanced Commerce responses.
    """
    
    signedRenewalInfo: Optional[str] = attr.field(default=None)
    signedTransactionInfo: Optional[str] = attr.field(default=None)