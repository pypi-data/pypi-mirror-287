from nomad_media_pip.src.admin.live_channel.get_live_channel import _get_live_channel

def _get_live_channel_status_message(self, AUTH_TOKEN, URL, CHANNEL_ID, DEBUG):
    # Get the live channel
    CHANNEL = _get_live_channel(self, AUTH_TOKEN, URL, CHANNEL_ID, DEBUG)

    # Check if channel was found
    if (CHANNEL):
        # Check if there are status messages
        if (CHANNEL["statusMessages"]):
            # Return the first status message
            return CHANNEL["statusMessage"]

    # There are no status messages
    return ""

