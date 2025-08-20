# Copyright (c) 2025 Apple Inc. Licensed under MIT License.

import uuid
from typing import Optional

class AdvancedCommerceValidationUtils:
    MAXIMUM_DESCRIPTION_LENGTH = 45
    MAXIMUM_DISPLAY_NAME_LENGTH = 30
    MAXIMUM_SKU_LENGTH = 128

    """
    Utility class for validating Advanced Commerce API parameters.
    """
    
    @staticmethod
    def validate_currency(currency: Optional[str]) -> Optional[str]:
        """
        Validate currency code.
        
        Args:
            currency: The currency code to validate
            
        Returns:
            The validated currency code
            
        Raises:
            ValueError: If currency is invalid
        """
        if currency is None:
            raise ValueError("Currency cannot be None")
        if not isinstance(currency, str):
            raise ValueError("Currency must be a string")
        if len(currency) != 3:
            raise ValueError("Currency must be a 3-character ISO code")
        return currency.upper()
    
    @staticmethod
    def validate_tax_code(tax_code: Optional[str]) -> Optional[str]:
        """
        Validate tax code.
        
        Args:
            tax_code: The tax code to validate
            
        Returns:
            The validated tax code
            
        Raises:
            ValueError: If tax code is invalid
        """
        if tax_code is None:
            raise ValueError("Tax code cannot be None")
        if not isinstance(tax_code, str):
            raise ValueError("Tax code must be a string")
        if not tax_code.strip():
            raise ValueError("Tax code cannot be empty")
        return tax_code
    
    @staticmethod
    def validate_uuid(uuid_value: Optional[str]) -> Optional[str]:
        """
        Validate UUID string.
        
        Args:
            uuid_value: The UUID string to validate
            
        Returns:
            The validated UUID string
            
        Raises:
            ValueError: If UUID is invalid
        """
        if uuid_value is None:
            raise ValueError("UUID cannot be None")
        if not isinstance(uuid_value, str):
            raise ValueError("UUID must be a string")
        try:
            # Validate by parsing as UUID
            uuid.UUID(uuid_value)
            return uuid_value
        except ValueError:
            raise ValueError("Value must be a valid UUID string")
    
    @staticmethod
    def validate_price(price: Optional[int]) -> Optional[int]:
        """
        Validate price value.
        
        Args:
            price: The price to validate
            
        Returns:
            The validated price
            
        Raises:
            ValueError: If price is invalid
        """
        if price is None:
            raise ValueError("Price cannot be None")
        if not isinstance(price, int):
            raise ValueError("Price must be an integer")
        if price < 0:
            raise ValueError("Price cannot be negative")
        return price
    
    @staticmethod
    def validate_transaction_id(transaction_id: Optional[str]) -> Optional[str]:
        """
        Validate transaction ID.
        
        Args:
            transaction_id: The transaction ID to validate
            
        Returns:
            The validated transaction ID
            
        Raises:
            ValueError: If transaction ID is invalid
        """
        if transaction_id is None:
            raise ValueError("Transaction ID cannot be None")
        if not isinstance(transaction_id, str):
            raise ValueError("Transaction ID must be a string")
        if not transaction_id.strip():
            raise ValueError("Transaction ID cannot be empty")
        return transaction_id
    
    @staticmethod
    def validate_description(description: Optional[str]) -> Optional[str]:
        """
        Validate description field.
        
        Args:
            description: The description to validate
            
        Returns:
            The validated description
            
        Raises:
            ValueError: If description is invalid
        """
        if description is None:
            return None
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        if len(description) > AdvancedCommerceValidationUtils.MAXIMUM_DESCRIPTION_LENGTH:
            raise ValueError(f"Description length ({len(description)}) exceeds maximum allowed ({AdvancedCommerceValidationUtils.MAXIMUM_DESCRIPTION_LENGTH})")
        return description
    
    @staticmethod
    def validate_display_name(display_name: Optional[str]) -> Optional[str]:
        """
        Validate display name field.
        
        Args:
            display_name: The display name to validate
            
        Returns:
            The validated display name
            
        Raises:
            ValueError: If display name is invalid
        """
        if display_name is None:
            return None
        if not isinstance(display_name, str):
            raise ValueError("Display name must be a string")
        if len(display_name) > AdvancedCommerceValidationUtils.MAXIMUM_DISPLAY_NAME_LENGTH:
            raise ValueError(f"Display name length ({len(display_name)}) exceeds maximum allowed ({AdvancedCommerceValidationUtils.MAXIMUM_DISPLAY_NAME_LENGTH})")
        return display_name
    
    @staticmethod
    def validate_sku(sku: Optional[str]) -> Optional[str]:
        """
        Validate SKU field.
        
        Args:
            sku: The SKU to validate
            
        Returns:
            The validated SKU
            
        Raises:
            ValueError: If SKU is invalid
        """
        if sku is None:
            return None
        if not isinstance(sku, str):
            raise ValueError("SKU must be a string")
        if len(sku) > AdvancedCommerceValidationUtils.MAXIMUM_SKU_LENGTH:
            raise ValueError(f"SKU length ({len(sku)}) exceeds maximum allowed ({AdvancedCommerceValidationUtils.MAXIMUM_SKU_LENGTH})")
        return sku
    
    @staticmethod
    def validate_target_product_id(target_product_id: Optional[str]) -> Optional[str]:
        """
        Validate target product ID field.
        
        Args:
            target_product_id: The target product ID to validate
            
        Returns:
            The validated target product ID
            
        Raises:
            ValueError: If target product ID is invalid
        """
        if target_product_id is None:
            return None
        if not isinstance(target_product_id, str):
            raise ValueError("Target Product ID must be a string")
        if not target_product_id.strip():
            raise ValueError("Target Product ID cannot be empty")
        return target_product_id