# =========== Copyright 2024 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2024 @ CAMEL-AI.org. All Rights Reserved. ===========
from abc import ABC, abstractmethod
from typing import Any

from .models import Action, BackendOutput, MessageType


class BackendModel(ABC):
    def __init__(
        self,
        model: str,
        parameters: dict[str, Any] = dict(),
        history_messages_len: int = 0,
    ) -> None:
        self.model = model
        self.parameters = parameters
        self.history_messages_len = history_messages_len

        assert self.history_messages_len >= 0

        self.reset("You are a helpfu assistant.", None)

    @abstractmethod
    def chat(self, contents: list[tuple[str, MessageType]]) -> BackendOutput:
        ...

    @abstractmethod
    def reset(
        self,
        system_message: str,
        action_space: list[Action] | None,
    ):
        ...

    @abstractmethod
    def get_token_usage(self):
        ...
