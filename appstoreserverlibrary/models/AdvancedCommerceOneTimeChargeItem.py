# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional

from attr import define
import attr

from .AbstractAdvancedCommerceItem import AbstractAdvancedCommerceItem
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceOneTimeChargeItem(AbstractAdvancedCommerceItem):
    """
    The details of a one-time charge product, including its display name, price, SKU, and metadata.
    
    https://developer.apple.com/documentation/advancedcommerceapi/onetimechargeitem
    """
    
    price: Optional[int] = attr.ib()
    
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.price = AdvancedCommerceValidationUtils.validate_price(self.price)