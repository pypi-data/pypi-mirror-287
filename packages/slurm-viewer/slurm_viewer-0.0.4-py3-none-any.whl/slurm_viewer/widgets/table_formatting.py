from __future__ import annotations

from typing import Any

from rich.style import Style
from rich.text import Text

from slurm_viewer.data.models import State, Node


def format_func(value: Any, style: Style) -> Text:
    if isinstance(value, float):
        return Text(f'{value:.2f}', style=style, justify='right')

    return Text(str(value), style=style, justify='right')


UNAVAILABLE_NODES = {State.DRAIN, State.DOWN, State.MAINTENANCE, State.REBOOT_REQUESTED, State.PLANNED}
AVAILABLE_NODES = {State.MIXED, State.IDLE}


def style_func(name: str, node: Node) -> Style:
    # value = getattr(node, name)

    if name == 'node_name':
        return Style(bold=True, italic=True)

    if name == 'state':
        states = node.states
        if not UNAVAILABLE_NODES.isdisjoint(states):
            # Nodes not accepting new jobs until reboot
            return Style(bgcolor='red')
        if not AVAILABLE_NODES.isdisjoint(states):
            # Nodes with available resources
            return Style(bgcolor='dark_green')
        if State.ALLOCATED in states:
            # Nodes with NO available resources
            return Style(bgcolor='orange_red1')

    return Style()


def format_value(_node: Node, key: str) -> Text:
    value = getattr(_node, key)
    style = style_func(key, _node)

    if value is None:
        return format_func('', style=style)

    if isinstance(value, list):
        return format_func(','.join(value), style=style)

    return format_func(value, style=style)
