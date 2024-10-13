import gradio as gr
import pandas as pd
import os
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

file_formats = {
    "csv": pd.read_csv,
    "xls": pd.read_excel,
    "xlsx": pd.read_excel,
    "xlsm": pd.read_excel,
    "xlsb": pd.read_excel,
    "feather": pd.read_feather
}

def load_data(file):
    if file is None:
        return None
    try:
        file_extension = os.path.splitext(file.name)[1][1:].lower()
        if file_extension in file_formats:
            return file_formats[file_extension](file.name)
        else:
            return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def chat_with_data(message, history, file, api_key):
    if file is None:
        return "Please upload a file first.", history
    if not api_key:
        return "Please enter your OpenAI API key.", history
    
    df = load_data(file)
    if df is None:
        return "Unsupported file format or error loading file. Please upload a CSV, Excel, or Feather file.", history
    
    llm = OpenAI(api_token=api_key)
    sdf = SmartDataframe(df, config={
        "llm": llm,
        "enable_cache": False,
        "conversational": True,
    })
    
    try:
        response = sdf.chat(message)
        history.append((message, str(response)))
        return "", history
    except Exception as e:
        return f"Error processing your request: {str(e)}", history

def clear_history():
    return []

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🐼 PandasAI: Chat with Your Data")
    
    with gr.Row():
        with gr.Column(scale=2):
            file_upload = gr.File(
                label="Upload Data File",
                # file_types=["csv", "xls", "xlsx", "xlsm", "xlsb", "feather"]
            )
            api_key_input = gr.Textbox(
                type="password", 
                label="OpenAI API Key", 
                placeholder="Paste your OpenAI API key here (sk-...)",
                show_label=True
            )
        
        with gr.Column(scale=1):
            gr.Markdown(
                """
                ## How to Use
                1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) 🔑
                2. Upload a data file (CSV, Excel, or Feather) 📄
                3. Ask questions about your data 💬
                
                ## About
                PandasAI App allows you to have a conversation with your data using AI. 
                Ask questions and get insights from your spreadsheets and databases!

                [GitHub Repository](https://github.com/gventuri/pandas-ai) | [Report Issues](https://github.com/gventuri/pandas-ai/issues)
                
                Created by [DR. AMJAD RAZA](https://www.linkedin.com/in/amjadraza/)
                """
            )
    
    chatbot = gr.Chatbot(label="Conversation", height=400)
    msg = gr.Textbox(label="Your Question", placeholder="Ask something about your data...")
    clear = gr.Button("Clear Conversation")
    
    msg.submit(chat_with_data, inputs=[msg, chatbot, file_upload, api_key_input], outputs=[msg, chatbot])
    clear.click(clear_history, outputs=[chatbot])

    gr.Markdown(
        """
        ### Supported File Formats
        - CSV (.csv)
        - Excel (.xls, .xlsx, .xlsm, .xlsb)
        - Feather (.feather)
        
        Note: Make sure your file is in one of these formats for successful upload and processing.
        """
    )

app.launch()