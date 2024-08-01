import time
from typing import Any, Dict, List, Optional
from portkey_ai.api_resources.apis.logger import Logger
from datetime import datetime

try:
    from llama_index.core.callbacks.base_handler import (
        BaseCallbackHandler as LlamaIndexBaseCallbackHandler,
    )
    from llama_index.core.utilities.token_counting import TokenCounter
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Please install llama-index to use Portkey Callback Handler"
    )
except ImportError:
    raise ImportError("Please pip install llama-index to use Portkey Callback Handler")


class PortkeyLlamaindex(LlamaIndexBaseCallbackHandler):
    startTimestamp: int = 0
    endTimestamp: float = 0

    def __init__(
        self,
        api_key: str,
    ) -> None:
        super().__init__(
            event_starts_to_ignore=[],
            event_ends_to_ignore=[],
        )

        self.api_key = api_key

        self.portkey_logger = Logger(api_key=api_key)

        self._token_counter = TokenCounter()
        self.completion_tokens = 0
        self.prompt_tokens = 0
        self.token_llm = 0

        self.log_object: Dict[str, Any] = {}
        self.prompt_records: Any = []

        self.request: Any = {}
        self.response: Any = {}

        self.responseTime: int = 0
        self.streamingMode: bool = False

        if not api_key:
            raise ValueError("Please provide an API key to use PortkeyCallbackHandler")

    def on_event_start(  # type: ignore[return]
        self,
        event_type: Any,
        payload: Optional[Dict[str, Any]] = None,
        event_id: str = "",
        parent_id: str = "",
        **kwargs: Any,
    ) -> str:
        """Run when an event starts and return id of event."""

        if event_type == "llm":
            self.llm_event_start(payload)

    def on_event_end(
        self,
        event_type: Any,
        payload: Optional[Dict[str, Any]] = None,
        event_id: str = "",
        **kwargs: Any,
    ) -> None:
        """Run when an event ends."""

        if event_type == "llm":
            self.llm_event_stop(payload, event_id)

    def start_trace(self, trace_id: Optional[str] = None) -> None:
        """Run when an overall trace is launched."""
        self.startTimestamp = int(datetime.now().timestamp())

    def end_trace(
        self,
        trace_id: Optional[str] = None,
        trace_map: Optional[Dict[str, List[str]]] = None,
    ) -> None:
        """Run when an overall trace is exited."""

    def llm_event_start(self, payload: Any) -> None:
        if "messages" in payload:
            chunks = payload.get("messages", {})
            self.prompt_tokens = self._token_counter.estimate_tokens_in_messages(chunks)
            messages = payload.get("messages", {})
            self.prompt_records = [
                {"role": m.role.value, "content": m.content} for m in messages
            ]
        self.request["method"] = "POST"
        self.request["url"] = payload.get("serialized", {}).get(
            "api_base", "chat/completions"
        )
        self.request["provider"] = payload.get("serialized", {}).get("class_name", "")
        self.request["headers"] = {}
        self.request["body"] = {"messages": self.prompt_records}
        self.request["body"].update(
            {"model": payload.get("serialized", {}).get("model", "")}
        )
        self.request["body"].update(
            {"temperature": payload.get("serialized", {}).get("temperature", "")}
        )

        return None

    def llm_event_stop(self, payload: Any, event_id) -> None:
        self.endTimestamp = float(datetime.now().timestamp())
        responseTime = self.endTimestamp - self.startTimestamp

        data = payload.get("response", {})

        chunks = payload.get("messages", {})
        self.completion_tokens = self._token_counter.estimate_tokens_in_messages(chunks)
        self.token_llm = self.prompt_tokens + self.completion_tokens
        self.response["status"] = 200
        self.response["body"] = {
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": data.message.role.value,
                        "content": data.message.content,
                    },
                    "logprobs": data.logprobs,
                    "finish_reason": "done",
                }
            ]
        }
        self.response["body"].update(
            {
                "usage": {
                    "prompt_tokens": self.prompt_tokens,
                    "completion_tokens": self.completion_tokens,
                    "total_tokens": self.token_llm,
                }
            }
        )
        self.response["body"].update({"id": event_id})
        self.response["body"].update({"created": int(time.time())})
        self.response["body"].update({"model": data.raw.get("model", "")})
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

        return None
