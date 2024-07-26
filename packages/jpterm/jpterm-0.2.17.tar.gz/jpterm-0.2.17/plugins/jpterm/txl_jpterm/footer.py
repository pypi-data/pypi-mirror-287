from __future__ import annotations

from collections import defaultdict
from typing import ClassVar

import rich.repr
from rich.console import RenderableType
from rich.text import Text
from textual import events
from textual.reactive import Reactive
from textual.widget import Widget

from txl.base import Footer as AbstractFooter


class FooterMeta(type(AbstractFooter), type(Widget)):
    pass


@rich.repr.auto
class Footer(AbstractFooter, Widget, metaclass=FooterMeta):
    """A simple footer widget which docks itself to the bottom of the parent container."""

    COMPONENT_CLASSES: ClassVar[set[str]] = {
        "footer--description",
        "footer--key",
        "footer--highlight",
        "footer--highlight-key",
    }
    """
    | Class | Description |
    | :- | :- |
    | `footer--description` | Targets the descriptions of the key bindings. |
    | `footer--highlight` | Targets the highlighted key binding. |
    | `footer--highlight-key` | Targets the key portion of the highlighted key binding. |
    | `footer--key` | Targets the key portions of the key bindings. |
    """

    DEFAULT_CSS = """
    Footer {
        background: $accent;
        color: $text;
        dock: bottom;
        height: 1;
    }
    Footer > .footer--highlight {
        background: $accent-darken-1;
    }

    Footer > .footer--highlight-key {
        background: $secondary;
        text-style: bold;
    }

    Footer > .footer--key {
        text-style: bold;
        background: $accent-darken-2;
    }
    """

    highlight_key: Reactive[str | None] = Reactive(None)

    def __init__(self) -> None:
        super().__init__()
        self._key_text: Text | None = None
        self.auto_links = False

    async def watch_highlight_key(self, value) -> None:
        """If highlight key changes we need to regenerate the text."""
        self._key_text = None
        self.refresh()

    def on_mount(self) -> None:
        self.watch(self.screen, "focused", self._focus_changed)

    def _focus_changed(self, focused: Widget | None) -> None:
        self._key_text = None
        self.refresh()

    async def on_mouse_move(self, event: events.MouseMove) -> None:
        """Store any key we are moving over."""
        self.highlight_key = event.style.meta.get("key")

    async def on_leave(self, event: events.Leave) -> None:
        """Clear any highlight when the mouse leaves the widget"""
        self.highlight_key = None

    def __rich_repr__(self) -> rich.repr.Result:
        yield from super().__rich_repr__()

    def make_key_text(self) -> Text:
        """Create text containing all the keys."""
        base_style = self.rich_style
        text = Text(
            style=self.rich_style,
            no_wrap=True,
            overflow="ellipsis",
            justify="left",
            end="",
        )
        highlight_style = self.get_component_rich_style("footer--highlight")
        highlight_key_style = self.get_component_rich_style("footer--highlight-key")
        key_style = self.get_component_rich_style("footer--key")

        bindings = [
            active_binding.binding
            for active_binding in self.app.active_bindings.values()
            if active_binding.binding.show
        ]

        action_to_bindings = defaultdict(list)
        for binding in bindings:
            action_to_bindings[binding.action].append(binding)

        for action, bindings in action_to_bindings.items():
            binding = bindings[0]
            if binding.key_display is None:
                key_display = self.app.get_key_display(binding.key)
                if key_display is None:
                    key_display = binding.key.upper()
            else:
                key_display = binding.key_display
            hovered = self.highlight_key == binding.key
            key_text = Text.assemble(
                (f" {key_display} ", highlight_key_style if hovered else key_style),
                (
                    f" {binding.description} ",
                    highlight_style if hovered else base_style,
                ),
                meta={
                    "@click": f"app.check_bindings('{binding.key}')",
                    "key": binding.key,
                },
            )
            text.append_text(key_text)
        return text

    def _on_styles_updated(self) -> None:
        self._key_text = None
        self.refresh()

    def post_render(self, renderable):
        return renderable

    def render(self) -> RenderableType:
        if self._key_text is None:
            self._key_text = self.make_key_text()
        return self._key_text
