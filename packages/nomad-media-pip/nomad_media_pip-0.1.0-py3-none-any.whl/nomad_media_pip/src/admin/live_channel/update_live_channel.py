from nomad_media_pip.src.helpers.send_request import _send_request
from nomad_media_pip.src.helpers.slugify import _slugify
from nomad_media_pip.src.admin.live_channel.live_channel_statuses import _LIVE_CHANNEL_STATUSES
from nomad_media_pip.src.admin.live_channel.get_security_groups import _get_security_groups
from nomad_media_pip.src.admin.live_channel.wait_for_live_channel_status import _wait_for_live_channel_status
from nomad_media_pip.src.admin.live_channel.live_channel_types import _LIVE_CHANNEL_TYPES
from nomad_media_pip.src.admin.live_channel.get_live_channel import _get_live_channel

def _update_live_channel(self, AUTH_TOKEN, URL, ID, NAME, THUMBNAIL_IMAGE_ID, ARCHIVE_FOLDER_ASSET_ID, 
                        ENABLE_HIGH_AVAILABILITY, ENABLE_LIVE_CLIPPING, IS_SECURE_OUTPUT, 
                        OUTPUT_SCREENSHOTS, TYPE, EXTERNAL_URL, SECURITY_GROUPS, DEBUG):
    
    LIVE_CHANNEL_INFO = _get_live_channel(self, AUTH_TOKEN, URL, ID, DEBUG)

    API_URL = f"{URL}/api/liveChannel"

    # Build the payload BODY
    BODY = LIVE_CHANNEL_INFO

    # Build the payload body
    BODY = LIVE_CHANNEL_INFO

    if NAME and NAME != BODY.get('name'):
        BODY['name'] = NAME
        BODY['routeName'] = _slugify(NAME)

    if THUMBNAIL_IMAGE_ID and THUMBNAIL_IMAGE_ID != BODY.get('thumbnailImage'):
        BODY['thumbnailImage'] = {'id': THUMBNAIL_IMAGE_ID}

    if ARCHIVE_FOLDER_ASSET_ID and ARCHIVE_FOLDER_ASSET_ID != BODY.get('archiveFolderAsset', {}).get('id'):
        BODY['archiveFolderAsset'] = {'id': ARCHIVE_FOLDER_ASSET_ID}

    if ENABLE_HIGH_AVAILABILITY is not None and ENABLE_HIGH_AVAILABILITY != BODY.get('enableHighAvailability'):
        BODY['enableHighAvailability'] = ENABLE_HIGH_AVAILABILITY

    if ENABLE_LIVE_CLIPPING is not None and ENABLE_LIVE_CLIPPING != BODY.get('enableLiveClipping'):
        BODY['enableLiveClipping'] = ENABLE_LIVE_CLIPPING

    if IS_SECURE_OUTPUT is not None and IS_SECURE_OUTPUT != BODY.get('isSecureOutput'):
        BODY['isSecureOutput'] = IS_SECURE_OUTPUT

    if OUTPUT_SCREENSHOTS is not None and OUTPUT_SCREENSHOTS != BODY.get('outputScreenshots'):
        BODY['outputScreenshots'] = OUTPUT_SCREENSHOTS

    if TYPE and _LIVE_CHANNEL_STATUSES.get(TYPE) != BODY.get('type', {}).get('id'):
        BODY['type'] = {'id': _LIVE_CHANNEL_TYPES.get(TYPE)}

    # Set the appropriate fields based on the channel type
    if TYPE == "External":
        if EXTERNAL_URL and EXTERNAL_URL != BODY.get('externalUrl'):
            BODY['externalUrl'] = EXTERNAL_URL
    else:
        if EXTERNAL_URL and BODY.get('externalUrl'):
            del BODY['externalUrl']

    if SECURITY_GROUPS:
        NOMAD_SECURITY_GROUPS = _get_security_groups(self, AUTH_TOKEN, URL, DEBUG)

        FILTERED_SECURITY_GROUPS = [
            {'description': group['description'], 'id': group['id']}
            for group in NOMAD_SECURITY_GROUPS
            if group['description'] in SECURITY_GROUPS
        ]

        if FILTERED_SECURITY_GROUPS != BODY.get('securityGroups'):
            BODY['securityGroups'] = FILTERED_SECURITY_GROUPS


    INFO = _send_request(self, AUTH_TOKEN, "Update Live Channel", API_URL, "PUT", None, BODY, DEBUG)
    _wait_for_live_channel_status(self, AUTH_TOKEN, URL, INFO["id"], _LIVE_CHANNEL_STATUSES["Idle"], 120, 2, DEBUG)
    return INFO