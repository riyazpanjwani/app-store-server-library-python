# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional

from attr import define

from .AbstractAdvancedCommerceResponse import AbstractAdvancedCommerceAppResponse

@define
class AdvancedCommerceSubscriptionChangeMetadataResponse(AbstractAdvancedCommerceAppResponse):
    """
    The response data for a subscription metadata change request.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadataresponse
    """
    
    def __init__(self, signedRenewalInfo: Optional[str] = None, signedTransactionInfo: Optional[str] = None):
        super().__init__(signedRenewalInfo, signedTransactionInfo)