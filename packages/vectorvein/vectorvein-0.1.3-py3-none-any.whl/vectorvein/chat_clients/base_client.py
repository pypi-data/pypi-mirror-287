# @Author: Bi Ying
# @Date:   2024-07-26 14:48:55
from abc import ABC, abstractmethod

from ..settings import settings
from ..types import defaults as defs
from ..types.enums import ContextLengthControlType, BackendType


class BaseChatClient(ABC):
    DEFAULT_MODEL: str | None = None
    BACKEND_NAME: BackendType | None = None

    def __init__(
        self,
        model: str = "",
        stream: bool = True,
        temperature: float = 0.7,
        context_length_control: ContextLengthControlType = defs.CONTEXT_LENGTH_CONTROL,
        random_endpoint: bool = True,
        endpoint_id: str = "",
        **kwargs,
    ):
        self.model = model or self.DEFAULT_MODEL
        self.stream = stream
        self.temperature = temperature
        self.context_length_control = context_length_control
        self.random_endpoint = random_endpoint
        self.endpoint_id = endpoint_id

        self.backend_settings = settings.get_backend(self.BACKEND_NAME)

        if endpoint_id:
            self.endpoint_id = endpoint_id
            self.random_endpoint = False
            self.endpoint = settings.get_endpoint(self.endpoint_id)

    @abstractmethod
    def create_completion(
        self,
        messages: list,
        model: str | None = None,
        stream: bool = True,
        temperature: float = 0.7,
        max_tokens: int = 2000,
        tools: list | None = None,
        tool_choice: str | None = None,
    ):
        pass


class BaseAsyncChatClient(ABC):
    DEFAULT_MODEL: str | None = None
    BACKEND_NAME: BackendType | None = None

    def __init__(
        self,
        model: str = "",
        stream: bool = True,
        temperature: float = 0.7,
        context_length_control: ContextLengthControlType = defs.CONTEXT_LENGTH_CONTROL,
        random_endpoint: bool = True,
        endpoint_id: str = "",
        **kwargs,
    ):
        self.model = model or self.DEFAULT_MODEL
        self.stream = stream
        self.temperature = temperature
        self.context_length_control = context_length_control
        self.random_endpoint = random_endpoint
        self.endpoint_id = endpoint_id

        self.backend_settings = settings.get_backend(self.BACKEND_NAME)

        if endpoint_id:
            self.endpoint_id = endpoint_id
            self.random_endpoint = False
            self.endpoint = settings.get_endpoint(self.endpoint_id)

    @abstractmethod
    async def create_completion(
        self,
        messages: list,
        model: str | None = None,
        stream: bool = True,
        temperature: float = 0.7,
        max_tokens: int = 2000,
        tools: list | None = None,
        tool_choice: str | None = None,
    ):
        pass
