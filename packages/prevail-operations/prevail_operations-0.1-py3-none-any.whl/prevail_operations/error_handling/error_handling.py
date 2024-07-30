## Manages error handling and exception classes for various scenarios.
## Contains functions or classes to log errors and responses for debugging purposes.


class APIError(Exception):
    pass


class ErrorHandler:
    @staticmethod
    def log_error(error_message):
        print(f"Error logged: {error_message}")

    @staticmethod
    def handle_api_exception(response):
        if response.status_code >= 400:
            error_message = f"API Error: {response.status_code} - {response.text}"
            ErrorHandler.log_error(error_message)
            raise APIError(error_message)
