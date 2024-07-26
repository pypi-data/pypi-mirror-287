import dataclasses

import httpx
from httpx import Response

from message_to_request.enums import MessageType


@dataclasses.dataclass
class Sender:
    url: str

    def send(
        self,
        text: str,
        message_type: MessageType = MessageType.INFO,
    ) -> Response:
        data = {
            "text": text,
            "message_type": message_type.value,
        }
        return httpx.post(f"{self.url}", json=data)
