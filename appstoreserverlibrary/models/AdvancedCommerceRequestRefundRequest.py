# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import List, Optional

from attr import define
import attr

from .AdvancedCommerceRequest import AdvancedCommerceRequest
from .AdvancedCommerceRequestRefundItem import AdvancedCommerceRequestRefundItem
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceRequestRefundRequest(AdvancedCommerceRequest):
    """
    The request data your app provides to request refunds for items.
    
    https://developer.apple.com/documentation/advancedcommerceapi/requestrefundrequest
    """
    
    items: List[AdvancedCommerceRequestRefundItem] = attr.ib()
    """
    The list of items to request refunds for.
    
    https://developer.apple.com/documentation/advancedcommerceapi/requestrefunditem
    """
    
    refundRiskingPreference: bool = attr.ib()
    """
    A Boolean value that indicates the refund risking preference.
    
    https://developer.apple.com/documentation/advancedcommerceapi/refundriskingpreference
    """
    
    currency: Optional[str] = attr.ib(default=None)
    """
    The currency of the refund amount.
    
    https://developer.apple.com/documentation/advancedcommerceapi/currency
    """
    
    storefront: Optional[str] = attr.ib(default=None)
    """
    The storefront for the transaction.
    
    https://developer.apple.com/documentation/advancedcommerceapi/storefront
    """
    
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        if self.currency is not None:
            self.currency = AdvancedCommerceValidationUtils.validate_currency(self.currency)