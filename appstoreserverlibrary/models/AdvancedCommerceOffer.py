# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from typing import Dict, Any, Optional

from attr import define
import attr

from .LibraryUtility import AttrsRawValueAware, AppStoreServerLibraryEnumMeta
from .AdvancedCommerceOfferPeriod import AdvancedCommerceOfferPeriod
from .AdvancedCommerceOfferReason import AdvancedCommerceOfferReason
from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceOffer(AttrsRawValueAware):
    """
    A discount offer for an auto-renewable subscription.
    
    https://developer.apple.com/documentation/advancedcommerceapi/offer
    """
    
    period: Optional[AdvancedCommerceOfferPeriod] = AdvancedCommerceOfferPeriod.create_main_attr("period")
    raw_period: Optional[str] = AdvancedCommerceOfferPeriod.create_raw_attr("rawPeriod")
    
    period_count: Optional[int] = attr.ib(default=None)
    price: Optional[int] = attr.ib(default=None)
    
    reason: Optional[AdvancedCommerceOfferReason] = AdvancedCommerceOfferReason.create_main_attr("reason")
    raw_reason: Optional[str] = AdvancedCommerceOfferReason.create_raw_attr("rawReason")
    
    unknown_fields: Optional[Dict[str, Any]] = attr.ib(default=None)
    
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        if self.price is not None:
            self.price = AdvancedCommerceValidationUtils.validate_price(self.price)