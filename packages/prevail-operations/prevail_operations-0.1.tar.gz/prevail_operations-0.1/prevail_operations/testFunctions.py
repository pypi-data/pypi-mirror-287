from business_operations.business_operations_handler import BusinessOperations

debug_enabled = True
test_email = "agraham@prevailven.com"
receiver_emails = []

BusinessOperations.runKinDailyShippingReport(debug_enabled, test_email, receiver_emails)
# BusinessOperations.runTDOrdersReport(debug_enabled, test_email, receiver_emails)
# BusinessOperations.runAddAmazonReturnsToFP()
