# Copyright (c) 2023 Apple Inc. Licensed under MIT License.

from attr import define
from .AbstractAdvancedCommerceItem import AbstractAdvancedCommerceItem


@define
class AdvancedCommerceSubscriptionMigrateItem(AbstractAdvancedCommerceItem):
    """
    An item for subscription migration in Advanced Commerce API.
    
    https://developer.apple.com/documentation/appstoreserverapi/advanced_commerce_api
    """
    
    def self(self):
        return self