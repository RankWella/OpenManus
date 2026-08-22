import streamlit as st
import asyncio
from app.agent.manus import Manus

st.set_page_config(page_title="OpenManus Web UI", layout="wide")
st.title("🤖 OpenManus Web Agent")

prompt = st.text_input("Enter your task for OpenManus:", placeholder="e.g., Search for top AI frameworks.")

if st.button("Run Agent") and prompt:
st.info("Executing task...")

async def run_manus():
    agent = Manus()
    await agent.run(prompt)

with st.spinner("OpenManus is running..."):
    asyncio.run(run_manus())

st.success("Task completed!")

