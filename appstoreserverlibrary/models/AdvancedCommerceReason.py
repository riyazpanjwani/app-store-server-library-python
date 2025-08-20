# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from enum import Enum

from .LibraryUtility import AppStoreServerLibraryEnumMeta

class AdvancedCommerceReason(str, Enum, metaclass=AppStoreServerLibraryEnumMeta):
    """
    A string value that indicates the reason for an advanced commerce operation.
    
    https://developer.apple.com/documentation/advancedcommerceapi/reason
    """
    UPGRADE = "UPGRADE"
    DOWNGRADE = "DOWNGRADE"
    APPLY_OFFER = "APPLY_OFFER"