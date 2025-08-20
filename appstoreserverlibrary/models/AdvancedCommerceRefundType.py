# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

from enum import Enum

from .LibraryUtility import AppStoreServerLibraryEnumMeta

class AdvancedCommerceRefundType(str, Enum, metaclass=AppStoreServerLibraryEnumMeta):
    """
    The type of refund.
    """
    FULL = "FULL"
    PRORATED = "PRORATED"