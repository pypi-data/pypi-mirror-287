def _api_exception_handler(RESPONSE, MESSAGE):
    # Set a async default error message
    ERROR = "Unknown error occurred"

    # Check if we have a response object and error message
    if (RESPONSE == None):
        # If not response then throw async default error or message
        if (MESSAGE == None or len(MESSAGE.strip()) == 0):
            raise Exception(ERROR)
        else:
            raise Exception(MESSAGE)
        
    if RESPONSE.text != "":
        # Response BODY is text
        error = RESPONSE.text

        # Throw error if valid
        if (error and len(error.strip()) > 0):
            RESPONSE_JSON = RESPONSE.json()
            raise Exception(f"{RESPONSE.status_code} {RESPONSE_JSON.get("message") if RESPONSE.json().get("message") else ""}")

    else:
        # Throw message and response status
        raise Exception(f"STATUS: {RESPONSE.status_code}")


