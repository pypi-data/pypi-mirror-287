from __future__ import annotations

from typing import Optional, Tuple, Type, cast

from ..adapter import StringAdapter
from ..interface import verb_required_block
from ..interpreter import Context
from ..interface.block import Block


__all__: Tuple[str, ...] = ("AssignmentBlock",)


class AssignmentBlock(cast(Type[Block], verb_required_block(False, parameter=True))):
    """
    Variables are useful for choosing a value and referencing it later in a tag.
    Variables can be referenced using brackets as any other block.

    **Usage:** ``{=(<name>):<value>}``

    **Aliases:** ``assign, let, var``

    **Payload:** value

    **Parameter:** name

    **Examples:** ::

        {=(prefix):!}
        The prefix here is `{prefix}`.
        # The prefix here is `!`.

        {assign(day):Monday}
        {if({day}==Wednesday):It's Wednesday my dudes!|The day is {day}.}
        # The day is Monday.
    """

    ACCEPTED_NAMES: Tuple[str, ...] = ("=", "assign", "let", "var")

    def process(self, ctx: Context) -> Optional[str]:
        if ctx.verb.parameter is None:
            return None
        ctx.response.variables[ctx.verb.parameter] = StringAdapter(str(ctx.verb.payload))
        return ""
