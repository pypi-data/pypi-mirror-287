from nomad_media_pip.src.helpers.send_request import _send_request

import json

def _transcribe_asset(self, AUTH_TOKEN, URL, ASSET_ID, TRANSCRIPT_ID, TRANSCRIPT, DEBUG):

    API_URL = f"{URL}/api/admin/asset/{ASSET_ID}/transcribe/{TRANSCRIPT_ID}"

    return _send_request(self, AUTH_TOKEN, "Transcribe asset", API_URL, "POST", None, TRANSCRIPT, DEBUG)