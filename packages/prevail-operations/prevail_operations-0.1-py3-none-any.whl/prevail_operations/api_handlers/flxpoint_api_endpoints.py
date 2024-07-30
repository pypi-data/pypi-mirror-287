class FlxpointAPIEndpoints:
    ## Define constants for different API endpoints
    RETURNS_ENDPOINT = "returns"
    INVENTORY_UPDATE_ENDPOINT = "inventory/variants?modifyCost=updateNonNull&modifyMsrp=updateNonNull&modifyMap=updateNonNull&modifyQuantity=updateNonNull&modifyShippingCost=updateNonNull&modifyDropShipFee=updateNonNull&modifyInventoryListPrice=updateNonNull&modifyAllowBackorders=updateNonNull"
    GET_ORDERS_ENDPOINT = "orders"
    UPDATE_ORDER_STATUS_ENDPOINT = "orders/"
    UPDATE_RETURN_ENDPOINT = "returns/"
    GET_PRODUCT_VARIANTS_ENDPOINT = "product/variants"
    UPDATE_PRODUCT_VARIANTS = "product/products/variant"
    UPDATE_SOURCE_VARIANTS = "inventory/variants"
