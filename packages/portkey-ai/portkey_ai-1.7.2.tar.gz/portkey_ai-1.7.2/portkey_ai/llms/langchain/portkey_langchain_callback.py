from datetime import datetime
import time
from typing import Any, Dict, List, Optional
from portkey_ai.api_resources.apis.logger import Logger

try:
    from langchain_core.callbacks import BaseCallbackHandler
except ImportError:
    raise ImportError("Please pip install langchain-core to use PortkeyLangchain")


class PortkeyLangchain(BaseCallbackHandler):
    def __init__(
        self,
        api_key: str,
    ) -> None:
        super().__init__()
        self.startTimestamp: float = 0
        self.endTimestamp: float = 0

        self.api_key = api_key

        self.portkey_logger = Logger(api_key=api_key)

        self.log_object: Dict[str, Any] = {}
        self.prompt_records: Any = []

        self.request: Any = {}
        self.response: Any = {}

        # self.responseHeaders: Dict[str, Any] = {}
        self.responseBody: Any = None
        self.responseStatus: int = 0

        self.streamingMode: bool = False

        if not api_key:
            raise ValueError("Please provide an API key to use PortkeyCallbackHandler")

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        for prompt in prompts:
            messages = prompt.split("\n")
            for message in messages:
                role, content = message.split(":", 1)
                self.prompt_records.append(
                    {"role": role.lower(), "content": content.strip()}
                )

        self.startTimestamp = float(datetime.now().timestamp())

        self.streamingMode = kwargs.get("invocation_params", False).get("stream", False)

        self.request["method"] = "POST"
        self.request["url"] = serialized.get("kwargs", "").get(
            "base_url", "chat/completions"
        )
        self.request["provider"] = serialized["id"][2]
        self.request["headers"] = serialized.get("kwargs", {}).get(
            "default_headers", {}
        )
        self.request["headers"].update({"provider": serialized["id"][2]})
        self.request["body"] = {"messages": self.prompt_records}
        self.request["body"].update({**kwargs.get("invocation_params", {})})

    def on_chain_start(
        self,
        serialized: Dict[str, Any],
        inputs: Dict[str, Any],
        **kwargs: Any,
    ) -> None:
        """Run when chain starts running."""

    def on_llm_end(self, response: Any, **kwargs: Any) -> None:
        self.endTimestamp = float(datetime.now().timestamp())
        responseTime = self.endTimestamp - self.startTimestamp

        usage = (response.llm_output or {}).get("token_usage", "")  # type: ignore[union-attr]

        self.response["status"] = (
            200 if self.responseStatus == 0 else self.responseStatus
        )
        self.response["body"] = {
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": response.generations[0][0].text,
                    },
                    "logprobs": response.generations[0][0].generation_info.get("logprobs", ""),  # type: ignore[union-attr] # noqa: E501
                    "finish_reason": response.generations[0][0].generation_info.get("finish_reason", ""),  # type: ignore[union-attr] # noqa: E501
                }
            ]
        }
        self.response["body"].update({"usage": usage})
        self.response["body"].update({"id": str(kwargs.get("run_id", ""))})
        self.response["body"].update({"created": int(time.time())})
        self.response["body"].update({"model": (response.llm_output or {}).get("model_name", "")})  # type: ignore[union-attr] # noqa: E501
        self.response["body"].update({"system_fingerprint": (response.llm_output or {}).get("system_fingerprint", "")})  # type: ignore[union-attr] # noqa: E501
        self.response["time"] = int(responseTime * 1000)
        self.response["headers"] = {}
        self.response["streamingMode"] = self.streamingMode

        self.log_object.update(
            {
                "request": self.request,
                "response": self.response,
            }
        )

        self.portkey_logger.log(log_object=self.log_object)

    def on_chain_end(
        self,
        outputs: Dict[str, Any],
        **kwargs: Any,
    ) -> None:
        """Run when chain ends running."""
        pass

    def on_chain_error(self, error: BaseException, **kwargs: Any) -> None:
        self.responseBody = error
        self.responseStatus = error.status_code  # type: ignore[attr-defined]
        """Do nothing."""
        pass

    def on_llm_error(self, error: BaseException, **kwargs: Any) -> None:
        self.responseBody = error
        self.responseStatus = error.status_code  # type: ignore[attr-defined]
        """Do nothing."""
        pass

    def on_tool_error(self, error: BaseException, **kwargs: Any) -> None:
        self.responseBody = error
        self.responseStatus = error.status_code  # type: ignore[attr-defined]
        pass

    def on_text(self, text: str, **kwargs: Any) -> None:
        pass

    def on_agent_finish(self, finish: Any, **kwargs: Any) -> None:
        pass

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        self.streamingMode = True
        """Do nothing."""
        pass

    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        input_str: str,
        **kwargs: Any,
    ) -> None:
        pass

    def on_agent_action(self, action: Any, **kwargs: Any) -> Any:
        """Do nothing."""
        pass

    def on_tool_end(
        self,
        output: Any,
        observation_prefix: Optional[str] = None,
        llm_prefix: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        pass
