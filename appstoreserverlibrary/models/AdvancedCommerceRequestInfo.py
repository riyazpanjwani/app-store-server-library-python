# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

import uuid
from typing import Optional

from attr import define
import attr

from .AdvancedCommerceValidationUtils import AdvancedCommerceValidationUtils

@define
class AdvancedCommerceRequestInfo:
    """
    The metadata to include in server requests.
    
    https://developer.apple.com/documentation/advancedcommerceapi/requestinfo
    """
    
    requestReferenceId: uuid.UUID = attr.ib()
    """
    A UUID that you provide to uniquely identify each request. If the request times out, you can use the same requestReferenceId value to retry the request. Otherwise, provide a unique value.
    """
    
    appAccountToken: Optional[uuid.UUID] = attr.ib(default=None)
    """
    A UUID that represents an app account token, to associate with the transaction in the request.
    
    https://developer.apple.com/documentation/appstoreserverapi/appaccounttoken
    """
    
    consistencyToken: Optional[str] = attr.ib(default=None)
    """
    The value of the advancedCommerceConsistencyToken that you receive in the JWSRenewalInfo renewal information for a subscription. Don't generate this value.
    
    https://developer.apple.com/documentation/advancedcommerceapi/advancedCommerceConsistencyToken
    """
    
    def __attrs_post_init__(self):
        self.requestReferenceId = AdvancedCommerceValidationUtils.validate_uuid(self.requestReferenceId)
        if self.appAccountToken is not None:
            self.appAccountToken = AdvancedCommerceValidationUtils.validate_uuid(self.appAccountToken)