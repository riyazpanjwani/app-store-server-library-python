# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from abc import ABC
from typing import Optional

from attr import define
import attr

from .AdvancedCommerceRequestInfo import AdvancedCommerceRequestInfo

@define
class AdvancedCommerceRequest(ABC):
    """
    Abstract base class for Advanced Commerce requests.
    """
    
    request_info: AdvancedCommerceRequestInfo = attr.ib()