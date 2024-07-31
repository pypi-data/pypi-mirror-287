from nomad_media_pip.src.admin.live_channel.get_live_channel_status import _get_live_channel_status
from nomad_media_pip.src.admin.live_channel.get_live_channel_status_message import _get_live_channel_status_message

import time

def _wait_for_live_channel_status(self, AUTH_TOKEN, URL, CHANNEL_ID, STATUS_TO_WAIT_FOR, TIMEOUT = 30, POLL_INTERVAL = 2, DEBUG = False):
    # Set the starting time
    STARTING_TIME = time.time()

    # Elapsed time in seconds
    ELAPSED_TIME = 0

    while (ELAPSED_TIME < TIMEOUT):
        # Get the Live Channel status
        CHANNEL_STATUS = _get_live_channel_status(self, AUTH_TOKEN, URL, CHANNEL_ID, DEBUG)

        # If channel is in STATUS_TO_WAIT_FOR return
        if (CHANNEL_STATUS == STATUS_TO_WAIT_FOR):
            # Give feedback to the console
            print(f"Live Channel [{CHANNEL_ID}] transitioned to status {STATUS_TO_WAIT_FOR}")
            
            return True


        # Give feedback to the console
        print(f"Live Channel [{CHANNEL_ID}] current status is {CHANNEL_STATUS}")

        # Check for Error status
        if (CHANNEL_STATUS == "Error"):
            # Get the error message
            CHANNEL_STATUS_MESSAGE = _get_live_channel_status_message(self, AUTH_TOKEN, URL, CHANNEL_ID, DEBUG)

            # Can't continue if Live Channel is in error status
            raise Exception(f"Live Channel [{CHANNEL_ID}] is in [Error] status: {CHANNEL_STATUS_MESSAGE}")


        # Calculate elapsed time in seconds
        ELAPSED_TIME = (time.time() - STARTING_TIME)

        # Give feedback to the console
        print(f"Waiting for Live Channel [{CHANNEL_ID}] to transition to status {STATUS_TO_WAIT_FOR} ... {str(round(ELAPSED_TIME))} {str(TIMEOUT)}")

        # Check for timeout
        if (ELAPSED_TIME > TIMEOUT):
            break


        # Wait poll interval
        time.sleep(POLL_INTERVAL)


    raise Exception(f"Waiting for Live Channel [{CHANNEL_ID}] to transition to status {STATUS_TO_WAIT_FOR} timed out")

