# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from attrs import define

from .AbstractAdvancedCommerceResponse import AbstractAdvancedCommerceAppResponse

@define
class AdvancedCommerceSubscriptionCancelResponse(AbstractAdvancedCommerceAppResponse):
    """
    The response data for a subscription cancellation request.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncancelresponse
    """
    pass