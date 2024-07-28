# streamlit-custom-component

Streamlit component that allows you to subscribe WebSocket.

## Installation instructions

```sh
pip install streamlit-ws-client
```

## Usage instructions

```python
import streamlit as st
from ws_client import ws_client


def get_ws_url():
    return ""


if "ws_url" not in st.session_state:
    st.session_state.ws_url = get_ws_url()

st.subheader("Component with WebSockets")

message = ws_client(st.session_state.ws_url, key="ws_client_1")
if message is not None:
    st.write(message)
```