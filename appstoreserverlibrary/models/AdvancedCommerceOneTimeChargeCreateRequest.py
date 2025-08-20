# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Optional

from attr import define
import attr

from .AbstractAdvancedCommerceInAppRequest import AbstractAdvancedCommerceInAppRequest
from .AdvancedCommerceOneTimeChargeItem import AdvancedCommerceOneTimeChargeItem
from .AdvancedCommerceRequestInfo import AdvancedCommerceRequestInfo
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceOneTimeChargeCreateRequest(AbstractAdvancedCommerceInAppRequest):
    """
    The request data your app provides when a customer purchases a one-time-charge product.
    
    https://developer.apple.com/documentation/advancedcommerceapi/onetimechargecreaterequest
    """
    
    OPERATION = "CREATE_ONE_TIME_CHARGE"
    VERSION = "1"
    
    currency: str = attr.ib()
    item: AdvancedCommerceOneTimeChargeItem = attr.ib()
    tax_code: str = attr.ib()
    storefront: Optional[str] = attr.ib(default=None)

    def __init__(self, requestInfo: AdvancedCommerceRequestInfo):
        super().__init__(self.OPERATION, self.VERSION, requestInfo)
    
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        
        if self.currency is not None:
            self.currency = AdvancedCommerceValidationUtils.validate_currency(self.currency)
        if self.tax_code is not None:
            self.tax_code = AdvancedCommerceValidationUtils.validate_tax_code(self.tax_code)
    
    def self(self):
        return self