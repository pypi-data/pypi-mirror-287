## Handles data manipulation and formatting before sending or after receiving from the API.
## Contains functions or classes for data mapping, transformation, and validation.
import json


class DataProcessor:
    def __init__(self, shipping_multiplier):
        self.shipping_multiplier = shipping_multiplier

    @staticmethod
    def format_return_data(returns):
        if returns.getElementsByTagName("amazon_rma_id"):
            amazon_rma_id = (
                returns.getElementsByTagName("amazon_rma_id")[0].childNodes[0].data
            )
        else:
            amazon_rma_id = ""

        formatted_return = {
            "orderNumber": returns.getElementsByTagName("order_id")[0]
            .childNodes[0]
            .data,
            "returnNumber": amazon_rma_id,
            "items": [
                {
                    "sku": returns.getElementsByTagName("merchant_sku")[0]
                    .childNodes[0]
                    .data,
                    "returnQuantity": int(
                        returns.getElementsByTagName("return_quantity")[0]
                        .childNodes[0]
                        .data
                    ),
                    "returnReason": returns.getElementsByTagName("return_reason_code")[
                        0
                    ]
                    .childNodes[0]
                    .data,
                    "returnCondition": "New",
                    "refundedAmount": float(
                        returns.getElementsByTagName("refund_amount")[0]
                        .childNodes[0]
                        .data
                    ),
                }
            ],
        }

        return formatted_return

    @staticmethod
    def format_fp_order_number(order):
        formatted_order = {
            order.get("referenceNumber"): order.get("id"),
        }
        return formatted_order

    @staticmethod
    def format_td_order_data(order):
        customer = order.get("customer")
        if customer["first_name"] is not None and customer["last_name"] is not None:
            customer_name = customer["first_name"] + " " + customer["last_name"]
        else:
            customer_name = ""

        y = lambda z: 0 if z is None else len(z)
        if y(order.get("transactions")) > 0:
            for transaction in order.get("transactions"):
                for key in transaction:
                    if key == "tdid":
                        for i in range(len(transaction)):
                            sku = "TTD" + transaction["tdid"]
                            cost = transaction["price"]
        else:
            sku = ""
            cost = ""

        preformatted_order = {
            "order_id": order.get("order_id"),
            "created": order.get("created_at"),
            "customer_name": customer_name,
            "sku": sku,
            "cost": cost,
            "shipping": order.get("shipping"),
        }

        formatted_order = list(preformatted_order.values())
        return formatted_order

    def format_td_product_data(self, product):
        sku = "TTD" + product["tdid"]
        cost = product["cost"]
        map = product["price_map"]
        quantity = product["quantity_available"]
        msrp = product["msrp"]
        shipping_estimate = product["shipping_estimate"]
        if shipping_estimate:
            shipping_estimate = json.loads(shipping_estimate)
            shipping_cost = float(shipping_estimate["min"]) * float(
                self.shipping_multiplier
            )
        else:
            shipping_cost = ""

        formatted_product = {
            "sku": sku,
            "cost": float(cost),
            "msrp": float(msrp),
            "map": float(map),
            "quantity": int(quantity),
            "shippingCost": shipping_cost,
        }

        return formatted_product

    @staticmethod
    def format_td_product_sku(product):
        formatted_order = {
            "TTD" + product.get("tdid"),
        }
        return formatted_order

    @staticmethod
    def format_fp_kopg(product):
        cost = round(float(product[1]), 2)
        quantity = int(float(product[2]))

        """ formatted_product = {
            "priceOverwrite": {"costOverwritten": True},
            "quantityOverwrite": {
                "quantityOverwritten": True,
                "isLockedByOrderVolumeProtection": False,
            },
            "sku": product[0],
            "cost": cost,
            "quantity": quantity,
            "archived": False,
        } """

        formatted_product = [
            {
                "sku": product[0],
                "cost": cost,
                "map": 0,
                "quantity": quantity,
                "shippingCost": 4.11,
                "archived": False,
            }
        ]
        return formatted_product

    @staticmethod
    def format_shipping(product):
        formatted_product = {
            "sku": product[0],
            "shippingCost": product[1],
            "archived": False,
        }

        return formatted_product

    @staticmethod
    def create_batches(data, batch_size):
        for i in range(0, len(data), batch_size):
            yield data[i : i + batch_size]

    def get_channel_name(id):
        match id:
            case 440189:
                return "PS Gunbroker"
            case 633173:
                return "KO eBay"
            case 646722:
                return "Prime Assortment"
            case 644488:
                return "Guns United"
            case 637981:
                return "Pyramid Air"
            case 635153:
                return "Walmart"
            case 77892:
                return "eBay"
            case 70072:
                return "Amazon"
            case 78660:
                return "Bowhunters Superstore"
            case _:
                return "ID Not In List"

    @staticmethod
    def format_fp_order_data_for_kinsey_report(order):
        if (
            order.get("shippingText") == "Ground Advantage Under 1"
            or order.get("shippingText") == "Ground Advantage Over 1"
        ):
            shippingText = "Ground Advantage"
        else:
            shippingText = order.get("shippingText")

        formatted_order = {
            "channel": DataProcessor.get_channel_name(order.get("channelId")),
            "orderId": order.get("id"),
            "customerName": order.get("shippingAddress").get("name"),
            "sku": order.get("orderItems")[0].get("sku"),
            "quantity": order.get("orderItems")[0].get("quantity"),
            "orderedAt": order.get("orderedAt"),
            "shippingText": shippingText,
            "tags": order.get("tags"),
        }
        return formatted_order

    @staticmethod
    def format_fp_product_data_for_kinsey_report(product):
        formatted_product = {
            "title": product.get("title"),
            "sku": product.get("sku"),
        }
        return formatted_product
