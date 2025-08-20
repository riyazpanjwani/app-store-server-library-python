# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional

from attr import define
import attr

from .AdvancedCommerceRefundReason import AdvancedCommerceRefundReason
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils
@define
class AdvancedCommerceRequestRefundItem:
    """
    The data your app provides to request a refund for an item.
    
    https://developer.apple.com/documentation/advancedcommerceapi/requestrefunditem
    """
    
    SKU: str = attr.ib()
    """
    The SKU identifier for the item to refund.
    """
    
    refundReason: AdvancedCommerceRefundReason = attr.ib()
    """
    The reason for the refund.
    
    https://developer.apple.com/documentation/advancedcommerceapi/refundreason
    """
    
    refundType: str = attr.ib()
    """
    The type of refund. Possible values: FULL, PRORATED, CUSTOM.
    """
    
    revoke: bool = attr.ib()
    """
    A Boolean value that indicates whether to revoke the item.
    """
    
    refundAmount: Optional[int] = attr.ib(default=None)
    """
    A refund amount, in milliunits of the currency.
    """

    def __attrs_post_init__(self):
        self.SKU = AdvancedCommerceValidationUtils.validate_sku(self.SKU)
        if self.refundAmount is not None:
            self.refundAmount = AdvancedCommerceValidationUtils.validate_price(self.refundAmount)