import json
import logging
from typing import Optional, Union

import requests

from aistudio_cognition.km.genai.models.genai_settings import GenAI
from aistudio_cognition.models.response_status import ResponseStatus

logger = logging.getLogger(__name__)


class AIStudioKMGenAI:
    def __init__(
        self,
        km_details: Union[dict, GenAI],
        project_name: str = "",
        connection_name: str = "",
    ) -> None:
        if isinstance(km_details, dict):
            self.km_genai = GenAI.from_dict(km_details)
        elif isinstance(km_details, GenAI):
            self.km_genai = km_details
        else:
            raise TypeError(
                "Method argument km_details should either be a dictionary or a GenAI object!"
            )

        self.project_name = project_name
        self.connection_name = connection_name
        response = self._validate_genai_details()
        if not response["success"]:
            error_message = ""
            if self.connection_name:
                error_message = f"Connection : {self.connection_name}, "
            error_message += (
                f"Project : {self.project_name}, Error : {response['message']}"
            )
            raise ValueError(error_message)

    def _validate_genai_details(self) -> ResponseStatus:
        if not self.km_genai.url:
            return ResponseStatus(
                success=False,
                message="KM Service not configured for this project version",
            )
        if not self.km_genai.km_project_id:
            return ResponseStatus(
                success=False,
                message="KM Project ID not configured for this project version",
            )
        if not self.km_genai.km_project_secret:
            return ResponseStatus(
                success=False,
                message="KM Project Secret not configured for this project version",
            )
        return ResponseStatus(success=True)

    def genai_query(
        self,
        query: str,
        stream: Optional[bool],
        history: Optional[list],
        filters: Optional[list],
        **kwargs,
    ) -> ResponseStatus:
        # TODO: Make an http call (chat completion) to the KM Service
        # Do we want to pass history dict?!
        headers = {
            "Project-Id": self.km_genai.km_project_id,
            "Project-Secret": self.km_genai.km_project_secret,
        }
        try:
            if not stream:
                url = f"{self.km_genai.url}/api/query"
                logger.info("Send request to KM Service url: %s", url)
                logger.info("with headers: %s", headers)
                # TODO: build the payload, as needed by km service
                # append history
                # create user query dict
                # add filters
                # add the kwargs as well
                payload = {**kwargs}

                # logger.info("Payload: %s", payload)
                km_response = requests.post(
                    self.km_qnamaker.endpoint, headers=headers, data=json.dumps(payload)
                )
                logger.info("Response received from QnA Maker: %s", km_response.text)
                logger.info("Response Status Code: %s", km_response.status_code)
        except ConnectionError as exc:
            logger.exception(exc)
            return ResponseStatus(
                success=False,
                message="Unable to establish a connection with the QnA Maker Service.",
            )
        try:
            response = json.loads(km_response.text)
        except json.JSONDecodeError as exc:
            logger.exception(exc)
            return ResponseStatus(
                success=False,
                message="Improper response received. "
                + "Please check if the Hostname and Knowledgebase Id are rightly configured.",
            )
        if "error" in response and "message" in response.get("error"):
            return ResponseStatus(
                success=False, message=response.get("error").get("message")
            )
