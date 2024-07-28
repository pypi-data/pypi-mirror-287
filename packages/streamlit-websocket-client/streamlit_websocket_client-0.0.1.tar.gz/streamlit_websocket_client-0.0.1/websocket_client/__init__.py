import os
from typing import Any
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "websocket_client",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component(
        "websocket_client",
        path=build_dir,
    )


def websocket_client(ws_url: str, key=None) -> Any:
    component_value = _component_func(
        ws_url=ws_url,
        key=key,
        default=None,
    )
    return component_value
