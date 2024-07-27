import os
from typing import Any

import streamlit.components.v1 as components
from streamlit import _main
from streamlit_markdown.st_hack import st_hack_component


_RELEASE = True
COMPONENT_NAME = "streamlit_typst"

# use the build instead of development if release is true
if _RELEASE:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/out")

    _typst_view = components.declare_component(COMPONENT_NAME, path=build_dir)
else:
    _typst_view = components.declare_component(
        COMPONENT_NAME,
        url="http://localhost:3000/component/streamlit_typst.streamlit_typst",
    )


def st_typst(
    content: str,
    background_color: str = "#343541",
    format: str = "json",
    key=None,
    **kwargs,
):
    """
    Creates a new instance of streamlit-diff-viewer component

    Parameters
    ----------
    content: str
        The content
    Returns: None
    """
    return _typst_view(content=content, fill=background_color, format=format, key=key, **kwargs)


def st_hack_typst(
    content: str,
    background_color: str = "#343541",
    format: str = "json",
    key=None,
    default: Any = None,
    **kwargs,
):
    """hack streamlt to prevent re-rendering or throw DuplicateWidgetID

    Args and Returns:
        same as st_typst
    """
    kwargs["content"] = content
    kwargs["fill"] = background_color
    kwargs["format"] = format
    return st_hack_component(_main, _typst_view, key, default, **kwargs)
