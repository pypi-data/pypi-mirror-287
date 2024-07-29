from __future__ import annotations

from typing import Literal, Optional

class LayoutOpts:
    """Options for layout configuration.

    Args:
        max_width (Optional[int]): The maximum width of the layout.
        max_height (Optional[int]): The maximum height of the layout.
        horizontal_align (Literal["left", "center", "right"]): The horizontal alignment of the layout.
        vertical_align (Literal["top", "center", "bottom"]): The vertical alignment of the layout.
        line_height_mult (Optional[float]): The line height multiplier of the layout.
        can_break_words (Optional[bool]): Whether words can be broken in the layout, default to
    """

    max_width: Optional[int]
    max_height: Optional[int]
    horizontal_align: Literal["left", "center", "right"]
    vertical_align: Literal["top", "center", "bottom"]
    line_height_mult: Optional[float]
    can_break_words: Optional[bool]

    def __init__(
        self,
        max_width: Optional[int] = ...,
        max_height: Optional[int] = ...,
        horizontal_align: Literal["left", "center", "right"] = ...,
        vertical_align: Literal["top", "center", "bottom"] = ...,
        line_height_mult: Optional[float] = ...,
        can_break_words: Optional[bool] = ...,
    ) -> None: ...
