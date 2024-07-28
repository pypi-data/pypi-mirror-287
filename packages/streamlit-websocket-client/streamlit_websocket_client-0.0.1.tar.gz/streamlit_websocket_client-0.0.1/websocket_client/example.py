import streamlit as st
from websocket_client import websocket_client


if "ws_url" not in st.session_state:
    st.session_state.ws_url = "<web socket url>"

st.subheader("Component with WebSockets")

message = websocket_client(st.session_state.ws_url, key="ws_client_1")
if message is not None:
    st.write(message)
