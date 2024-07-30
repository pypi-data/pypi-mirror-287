# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import List

from llama_toolchain.inference.api import Message
from llama_toolchain.safety.shields import ShieldBase, ShieldRunnerMixin

from .builtin import BaseTool


class SafeTool(BaseTool, ShieldRunnerMixin):
    """A tool that makes other tools safety enabled"""

    def __init__(
        self,
        tool: BaseTool,
        input_shields: List[ShieldBase] = None,
        output_shields: List[ShieldBase] = None,
    ):
        self._tool = tool
        ShieldRunnerMixin.__init__(
            self, input_shields=input_shields, output_shields=output_shields
        )

    def get_name(self) -> str:
        # return the name of the wrapped tool
        return self._tool.get_name()

    async def run(self, messages: List[Message]) -> List[Message]:
        if self.input_shields:
            await self.run_shields(messages, self.input_shields)
        # run the underlying tool
        res = await self._tool.run(messages)
        if self.output_shields:
            await self.run_shields(messages, self.output_shields)

        return res


def with_safety(
    tool: BaseTool,
    input_shields: List[ShieldBase] = None,
    output_shields: List[ShieldBase] = None,
) -> SafeTool:
    return SafeTool(
        tool,
        input_shields=input_shields,
        output_shields=output_shields,
    )
