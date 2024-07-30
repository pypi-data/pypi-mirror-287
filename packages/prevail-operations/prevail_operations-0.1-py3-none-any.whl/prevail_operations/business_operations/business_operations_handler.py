import datetime
import traceback
import xml.dom.minidom
from collections import defaultdict

from api_handlers.flxpoint_api_endpoints import FlxpointAPIEndpoints
from api_handlers.flxpoint_api_handler import FlxpointAPIClient
from api_handlers.topdawg_api_endpoints import TopdawgAPIEndpoints
from api_handlers.topdawg_api_handler import TopdawgAPIClient
from data_processing.data_processing import DataProcessor
from error_handling.error_handling import APIError, ErrorHandler
from non_api_handlers.csv_handler import WriteCSV
from non_api_handlers.email_handler import SendEmail


class BusinessOperations:
    def __init__():
        return

    def runKinDailyShippingReport(debug_enabled, test_email, receiver_emails):

        ## Variables
        ### Configurable API Variables
        base_url = "https://api.flxpoint.com"
        access_token = "O96u4NAoBPZXSJeooMNYG5AsJzcSSTW0c4bJE0khpedDlKhiJYsXnOKwa40yJ5TuSU7F114Jiuf3dHPdXPuHfypmwSUkiin0aSGJ"
        status = "Open"
        includeTags = "true"
        filteredTags = [
            "True Backorder",
            "Restricted Item to State",
            "Backorder-Customer Emailed",
        ]

        ### Configurable Email Variables
        sender_email = "systems_PV@prevailven.com"
        subject = "Prevail Daily Order Report"
        password = "G#7472xy^565007ag"
        body = "\nPrevail Daily Order Report"
        port = 587

        ### Configurable General Variables
        csvFile = "DailyOrderReport.csv"

        ### Non-Configurable Variables
        page = 1
        per_page = 100
        tod = datetime.datetime.now()
        d = datetime.timedelta(days=90)
        start_date = tod - d
        start_date = start_date.strftime("%Y-%m-%d") + "T00:00:00.000Z"
        skus = []
        api_client = FlxpointAPIClient(
            base_url,
            access_token,
            page,
            per_page,
            start_date,
            skus,
            status,
            includeTags,
        )

        # Grab all open orders
        try:
            more_data = True
            orders_endpoint = FlxpointAPIEndpoints.GET_ORDERS_ENDPOINT
            flxpoint_api = api_client.get_orders(orders_endpoint).json()
            orders_data = []

            for order in flxpoint_api:
                formatted_order = DataProcessor.format_fp_order_data_for_kinsey_report(
                    order
                )
                orders_data.append(formatted_order)

            while more_data:
                page += 1
                FlxpointAPIClient.page = page
                flxpoint_api = api_client.get_orders(orders_endpoint).json()
                if not flxpoint_api:
                    more_data = False
                for order in flxpoint_api:
                    formatted_order = (
                        DataProcessor.format_fp_order_data_for_kinsey_report(order)
                    )
                    orders_data.append(formatted_order)

            # print(orders_data)

        except APIError as e:
            print(f"API error occurred: {str(e)}")
            ErrorHandler.log_error(str(e))

        except Exception as e:
            ### Handle other unexpected exceptions
            print(f"An unexpected error occurred: {str(e)}")
            print(traceback.format_exc())
            ErrorHandler.log_error(str(e))

        # Grab product data
        try:
            products = []
            products_data = []

            # create list of skus
            for order in orders_data:
                products.append(order.get("sku"))

            data = {"skus": ",".join(str(product) for product in products)}
            # print(data)

            # get product data
            products_endpoint = FlxpointAPIEndpoints.GET_PRODUCT_VARIANTS_ENDPOINT
            flxpoint_api = api_client.get_product_variants(
                products_endpoint, data
            ).json()

            # clean product data
            for product in flxpoint_api:
                formatted_product = (
                    DataProcessor.format_fp_product_data_for_kinsey_report(product)
                )
                products_data.append(formatted_product)

            # print(products_data)

        except APIError as e:
            print(f"API error occurred: {str(e)}")
            ErrorHandler.log_error(str(e))

        except Exception as e:
            ### Handle other unexpected exceptions
            print(f"An unexpected error occurred: {str(e)}")
            print(traceback.format_exc())
            ErrorHandler.log_error(str(e))

        # Match order data with product data
        d = defaultdict(dict)
        for item in orders_data + products_data:
            d[item["sku"]].update(item)
        list(d.values())
        # print(d)

        # Filter to Kinsey's orders
        csvData = []
        for order in d:
            if not order.startswith("FER") | order.startswith("TTD"):
                # print(d[order])
                csvOrder = d[order]
                orderValues = csvOrder.values()
                print(str(orderValues))
                if not any(x in str(orderValues) for x in filteredTags):
                    y = list(orderValues)
                    y.pop(7)
                    csvData.append(list(y))

        print(csvData)

        # Format in csv
        csvHeaders = [
            "Channel Name",
            "Order #",
            "Ship To Name",
            "SKU",
            "Quantity",
            "Ordered On",
            "Shipping Method",
            "Title",
        ]

        WriteCSV(csvFile, csvHeaders, csvData).write_csv()

        # Email to email list at 1:50pm
        if debug_enabled == True:
            receiver_emails = test_email

        SendEmail.send_email(
            sender_email, receiver_emails, subject, body, csvFile, port, password
        )

        # Send alert if email failed
        return

    def runTDOrdersReport(debug_enabled, test_email, receiver_emails):

        ## Variables
        csvFile = "TDOrders.csv"
        base_url = "https://topdawg.com"
        access_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZjUzZjFlOTcyZWY0YWYyMjYxZGNiMDQ1YTI4NzY2MTJjNWZjM2Y1YWZjMjQyZjI4YWVmMWQzOTQ1N2FiYmFlZWIwMTU2MDg1MWU3MGE1ODEiLCJpYXQiOjE2ODA1Mzg4NTYuMjAxMDY1LCJuYmYiOjE2ODA1Mzg4NTYuMjAxMDcsImV4cCI6MTk5NjE1ODA1Ni4xOTEzODIsInN1YiI6IjIwMjA3Iiwic2NvcGVzIjpbIlNoaXBwaW5nQ29zdEVzdGltYXRvciIsIlJlc2VsbGVyT3JkZXJzIiwiUmVzZWxsZXJQYXJjZWxzIiwiUmVzZWxsZXJDdXN0b21lcnMiLCJSZXNlbGxlclBheW1lbnRzIiwiUmVzZWxsZXJQcm9kdWN0cyJdfQ.P197hyFI0-EkKMEISbykquL_AECaiAdsYSYl_OAssS4FXiKLfkDO6zYMcBvtlqIWjNFEYMHbHXSTHuJXjP8h5Zp2gB4ShqcJnmS-G9_UOBNwbYodsyqP9FrBq0ywRL5ejx72U9SZmOA2TGhP5Mr82IYOj9J19_82bYNVs2A8pm5fPbsMAJUfJF1rcd_A_S_pVDUbViLi3YvHGGpTmIy0CLQCxjPtPxGOb0PweEdYa4Le97h1-VLR9MMugNpdb9KBHzYIqm2FzqYwbcK73ff_zaGeLITOmoPukVxMvbt3xHkGUujvDq7bRpf9VdtF58_qbioFash8CWUFH0_1HdgPHt9edSEHXLbQfOrXS3eqvHCRN0nJ1isbEQsCV3_Xv91HGCQ2jiJYMVhlwwqB-dVzjinlRCVNwOCXG4hmLaIGzOfuFv8kITzNY1XxGtjY0MK62JbFn67iQT2b5d1YaLP-C255fkYvc7p7j70yVTGzox4v4-jaR7GAX3stIMAU9Nl7Kwc-KViA88wbzytOZH0zh0vOc5CApKczyS0VdtArgKFFYvSx7ew4YXdcwK8Idh4n9CiNikNFntAArb9fmOXfIZ3mAA6KrK-w-bsKilRsB_TBWwuYVZu7Q-rdy8MybwXv8VuQDJhOrxcV2vW4z67ay-wOhmLjDUs9yCyMx3igM6Y"
        page = "1"
        per_page = "1000"

        tod = datetime.datetime.now()
        d = datetime.timedelta(days=90)
        start_date = tod - d
        start_date = start_date.strftime("%Y-%m-%d") + "T00:00:00.000Z"
        api_client = TopdawgAPIClient(
            base_url, access_token, page, per_page, start_date
        )

        ### Configurable Email Variables
        sender_email = "systems_PV@prevailven.com"
        subject = "TopDawg Weekly Order Report"
        password = "G#7472xy^565007ag"
        body = "\nTopDawg Weekly Order Report"
        port = 587

        ## Import TopDawg Order Data
        try:
            orders_endpoint = TopdawgAPIEndpoints.GET_ORDERS_ENDPOINT
            topdawg_api = api_client.get_orders(orders_endpoint).json()
            orders_data = topdawg_api["orders"]
            for page in range(2, topdawg_api["pagination"]["total_pages"] + 1):
                TopdawgAPIClient.page = page
                topdawg_api = api_client.get_orders(orders_endpoint).json()
                orders_data.extend(topdawg_api["orders"])

            csvData = []
            header = [
                "order_id",
                "created_at",
                "customer_name",
                "sku",
                "cost",
                "shipping",
            ]
            if orders_data:
                for order in orders_data:
                    formatted_order = DataProcessor.format_td_order_data(order)
                    csvData.append(formatted_order)

                WriteCSV(csvFile, header, csvData).write_csv()
            else:
                print("No order data.")

        except APIError as e:
            print(f"API error occurred: {str(e)}")
            ErrorHandler.log_error(str(e))

        except Exception as e:
            ### Handle other unexpected exceptions
            print(f"An unexpected error occurred: {str(e)}")
            ErrorHandler.log_error(str(e))

        # Get orders from FP
        # Add FP order numbers to csv

        # Email to email list at 1:50pm
        if debug_enabled == True:
            receiver_emails = test_email

        SendEmail.send_email(
            sender_email, receiver_emails, subject, body, csvFile, port, password
        )
        return

    def runAddAmazonReturnsToFP():
        ## Variables
        base_url = "https://api.flxpoint.com"
        access_token = "O96u4NAoBPZXSJeooMNYG5AsJzcSSTW0c4bJE0khpedDlKhiJYsXnOKwa40yJ5TuSU7F114Jiuf3dHPdXPuHfypmwSUkiin0aSGJ"
        page = 1
        per_page = 100
        tod = datetime.datetime.now()
        d = datetime.timedelta(days=90)
        start_date = tod - d
        start_date = start_date.strftime("%Y-%m-%d") + "T00:00:00.000Z"
        skus = []
        status = ""
        includeTags = ""
        api_client = FlxpointAPIClient(
            base_url,
            access_token,
            page,
            per_page,
            start_date,
            skus,
            status,
            includeTags,
        )

        ## Import XML Data
        xml_doc = xml.dom.minidom.parse("returnsreport.xml")
        returnsData = xml_doc.getElementsByTagName("return_details")

        ## Get all FP orders
        try:
            more_data = True
            orders_endpoint = FlxpointAPIEndpoints.GET_ORDERS_ENDPOINT
            flxpoint_api = api_client.get_orders(orders_endpoint).json()
            orders_numbers = {}

            for order in flxpoint_api:
                formatted_order_number = DataProcessor.format_fp_order_number(order)
                orders_numbers.update(formatted_order_number)

            while more_data:
                page += 1
                FlxpointAPIClient.page = page
                flxpoint_api = api_client.get_orders(orders_endpoint).json()
                if not flxpoint_api:
                    more_data = False
                for order in flxpoint_api:
                    formatted_order_number = DataProcessor.format_fp_order_number(order)
                    orders_numbers.update(formatted_order_number)

            print(orders_numbers)

        except APIError as e:
            print(f"API error occurred: {str(e)}")
            ErrorHandler.log_error(str(e))

        except Exception as e:
            ### Handle other unexpected exceptions
            print(f"An unexpected error occurred: {str(e)}")
            print(traceback.format_exc())
            ErrorHandler.log_error(str(e))

        returnsAddedCount = 0

        for return_details in returnsData:

            try:

                ## Process XML Data
                formatted_return = DataProcessor.format_return_data(return_details)
                # print(formatted_return)

                ## Open order
                ### Get order ID from Order Number ###
                orderID = orders_numbers[formatted_return.get("orderNumber")]
                # print(orderID)

                update_order_status_endpoint = (
                    FlxpointAPIEndpoints.UPDATE_ORDER_STATUS_ENDPOINT
                )
                order_status_response = api_client.update_order_status(
                    update_order_status_endpoint, orderID
                )

                ## Send to Flxpoint
                returns_endpoint = FlxpointAPIEndpoints.RETURNS_ENDPOINT
                response = api_client.create_return(returns_endpoint, formatted_return)

                ## Close returnless refunds in FP
                if (
                    return_details.getElementsByTagName("resolution")[0]
                    .childNodes[0]
                    .data
                    == "ReturnlessRefund"
                ):
                    # print(response)
                    update_return_status_endpoint = (
                        FlxpointAPIEndpoints.UPDATE_RETURN_ENDPOINT
                    )
                    data = {"returnStatus": "closed"}
                    return_data = response.get("return")
                    # print(return_data)
                    return_id = return_data.get("id")
                    # print(return_id)
                    return_status_response = api_client.update_return_status(
                        update_return_status_endpoint, return_id, data
                    )
                    # print(return_status_response)

                if response and response.get("warning") == "":
                    print(
                        "New return created successfully for order: "
                        + formatted_return.get("orderNumber")
                    )
                    returnsAddedCount += 1
                else:
                    print(
                        "Failed to create a new return for order: "
                        + formatted_return.get("orderNumber")
                        + ". Check response for details."
                    )
                    print(response)

            except APIError as e:
                print(f"API error occurred: {str(e)}")
                ErrorHandler.log_error(str(e))

            except Exception as e:
                ### Handle other unexpected exceptions
                print(f"An unexpected error occurred: {str(e)}")
                print(traceback.format_exc())
                ErrorHandler.log_error(str(e))

        print("Successfully created " + str(returnsAddedCount) + " returns.")
        return
