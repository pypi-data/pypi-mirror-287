import json
from enum import Enum
from pathlib import Path
from typing import List, Optional
import mimetypes

from relari.core.exceptions import APIError
from relari.core.types import HTTPMethod


class SyntheticDataClient:
    def __init__(self, client) -> None:
        self._client = client

    @staticmethod
    def guess_mime_type(filename):
        mime_type, _ = mimetypes.guess_type(filename)
        if mime_type is None:
            mime_type = "application/octet-stream"
        return mime_type

    def new(
        self,
        project_id: str,
        samples: int,
        files: List[Path],
        name: Optional[str]=None,
    ):
        endpoint = f"projects/{project_id}/synth/rag/"
        payload = [
            ("files", (file.name, open(file, "rb"), "application/octet-stream"))
            for file in files
        ]
        res = self._client._request(
            endpoint,
            HTTPMethod.POST,
            params={"name": name, "samples": samples},
            files=payload,
        )
        # Ensuring files are closed after the request
        for _, file_info in payload:
            _, file_handle, _ = file_info
            file_handle.close()
        # Check response status and raise error if needed
        if res.status_code != 200:
            raise APIError(message="Failed to create synthetic data", response=res)
        return res.json()
