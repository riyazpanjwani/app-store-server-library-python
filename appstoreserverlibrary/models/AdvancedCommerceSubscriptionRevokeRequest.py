# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional
from attr import define
import attr
from .AdvancedCommerceRequest import AdvancedCommerceRequest
from .AdvancedCommerceRefundReason import AdvancedCommerceRefundReason
from .AdvancedCommerceRefundType import AdvancedCommerceRefundType

@define
class AdvancedCommerceSubscriptionRevokeRequest(AdvancedCommerceRequest):
    """
    The request data your app provides to revoke an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/subscriptionrevokerequest
    """
    
    refundReason: AdvancedCommerceRefundReason = attr.field()
    """
    The reason for the refund.
    
    https://developer.apple.com/documentation/advancedcommerceapi/refundreason
    """
    
    refundRiskingPreference: bool = attr.field()
    """
    A Boolean value that indicates the refund risking preference.
    
    https://developer.apple.com/documentation/advancedcommerceapi/refundriskingpreference
    """
    
    refundType: Optional[AdvancedCommerceRefundType] = attr.field(default=None)
    """
    The type of refund.
    
    https://developer.apple.com/documentation/advancedcommerceapi/refundtype
    """
    
    storefront: Optional[str] = attr.field(default=None)
    """
    The storefront for the transaction.
    
    https://developer.apple.com/documentation/advancedcommerceapi/storefront
    """