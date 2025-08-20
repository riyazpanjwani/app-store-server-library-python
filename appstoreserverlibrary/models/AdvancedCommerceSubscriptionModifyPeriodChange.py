# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional
from attr import define
import attr
from .AdvancedCommerceEffective import AdvancedCommerceEffective
from .AdvancedCommercePeriod import AdvancedCommercePeriod


@define
class AdvancedCommerceSubscriptionModifyPeriodChange:
    """
    The data your app provides to change the billing period of an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyperiodchange
    """
    
    effective: Optional[AdvancedCommerceEffective] = attr.field(default=None)
    period: Optional[AdvancedCommercePeriod] = attr.field(default=None)