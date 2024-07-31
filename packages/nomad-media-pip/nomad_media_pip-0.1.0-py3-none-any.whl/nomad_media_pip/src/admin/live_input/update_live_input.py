from nomad_media_pip.src.helpers.send_request import _send_request
from nomad_media_pip.src.helpers.slugify import _slugify
from nomad_media_pip.src.admin.live_input.live_input_statuses import _LIVE_INPUT_STATUSES
from nomad_media_pip.src.admin.live_input.live_input_types import _LIVE_INPUT_TYPES
from nomad_media_pip.src.admin.live_input.get_live_input import _get_live_input
from nomad_media_pip.src.admin.live_input.wait_for_live_input_status import _wait_for_live_input_status

def _update_live_input(self, AUTH_TOKEN, URL, ID, NAME, SOURCE, TYPE, IS_STANDARD,
                       VIDEO_ASSET_ID, DESTINATIONS, SOURCES, DEBUG):
    INPUT_INFO = _get_live_input(self, AUTH_TOKEN, URL, ID, DEBUG)

    API_URL = f"{URL}/api/liveInput/{ID}"

    BODY = INPUT_INFO

    if NAME and NAME != BODY["name"]:
        BODY["name"] = NAME
        BODY["internalName"] = _slugify(NAME)

    if TYPE and _LIVE_INPUT_TYPES[TYPE] != BODY["type"]["id"]:
        BODY["type"] = {"id": _LIVE_INPUT_TYPES[TYPE]}

    # Set the appropriate fields based on the type
    if TYPE == "RTMP_PUSH":
        if SOURCE and SOURCE != BODY.get("sourceCidr"):
            BODY["sourceCidr"] = SOURCE
        if "sources" in BODY:
            del BODY["sources"]
    elif TYPE in ["RTMP_PULL", "RTP_PUSH", "URL_PULL"]:
        if SOURCE and SOURCE != BODY.get("sources"):
            BODY["sources"] = [{"url": SOURCE}]
        if "sourceCidr" in BODY:
            del BODY["sourceCidr"]
    else:
        if "sourceCidr" in BODY:
            del BODY["sourceCidr"]
        if "sources" in BODY:
            del BODY["sources"]

    if IS_STANDARD is not None and IS_STANDARD != BODY.get("isStandard"):
        BODY["isStandard"] = IS_STANDARD

    if VIDEO_ASSET_ID and VIDEO_ASSET_ID != BODY["videoAsset"]["id"]:
        BODY["videoAsset"] = {"id": VIDEO_ASSET_ID}

    if DESTINATIONS and DESTINATIONS != BODY.get("destinations"):
        BODY["destinations"] = DESTINATIONS

    if SOURCES and SOURCES != BODY.get("sources"):
        BODY["sources"] = SOURCES

    INFO = _send_request(self, AUTH_TOKEN, "Update Live Input", API_URL, "PUT", None, BODY, DEBUG)
    _wait_for_live_input_status(self, AUTH_TOKEN, URL, INFO["id"], _LIVE_INPUT_STATUSES["Detached"], 15, 1)
    return INFO