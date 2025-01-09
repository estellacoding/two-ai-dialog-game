# llm_checker.py
import streamlit as st

# 根據模型名稱動態檢查並返回對應的 API 金鑰
def get_api_key(model_name):
    model_lower = model_name.lower()
    if "gpt" in model_lower:
        return st.session_state["api_keys"]["GPT"]
    
    elif "claude" in model_lower:
        return st.session_state["api_keys"]["CLAUDE"]
    
    elif "gemini" in model_lower:
        return st.session_state["api_keys"]["GEMINI"]
    
    elif "mistral" in model_lower:
        return st.session_state["api_keys"]["MISTRAL"]
    
    elif "grok" in model_lower:
        return st.session_state["api_keys"]["GROK"]
    
    else:
        return None