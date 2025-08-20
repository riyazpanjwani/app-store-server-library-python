# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional

from attr import define
import attr

from .AdvancedCommerceRequest import AdvancedCommerceRequest

@define
class AdvancedCommerceSubscriptionCancelRequest(AdvancedCommerceRequest):
    """
    The request data your app provides to cancel an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncancelrequest
    """
    
    storefront: Optional[str] = attr.ib(default=None)