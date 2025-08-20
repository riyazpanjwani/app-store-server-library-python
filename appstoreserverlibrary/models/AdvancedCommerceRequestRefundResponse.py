# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from attrs import define

from .AbstractAdvancedCommerceResponse import AbstractAdvancedCommerceAppResponse

@define
class AdvancedCommerceRequestRefundResponse(AbstractAdvancedCommerceAppResponse):
    """
    The response data for a refund request.
    
    https://developer.apple.com/documentation/advancedcommerceapi/requestrefundresponse
    """
    pass