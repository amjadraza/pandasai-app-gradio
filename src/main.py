import gradio as gr
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

def load_data(file):
    if file is None:
        return None
    try:
        return pd.read_csv(file.name)
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def read_csv(file):
    if file is None:
        return "Please upload a CSV file."
    
    try:
        # Read the uploaded file into a pandas DataFrame
        df = pd.read_csv(file.name)       
        return df
    except pd.errors.EmptyDataError:
        return "The uploaded file is empty."
    except pd.errors.ParserError:
        return "Unable to parse the file. Make sure it's a valid CSV file."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def chat_with_data(message, history, file, api_key):
    if file is None:
        return "Please upload a CSV file first.", history
    if not api_key:
        return "Please enter your OpenAI API key.", history
    
    # df = load_data(file)
    df = read_csv(file)
    if df is None:
        return "Error loading file. Please upload a valid CSV file.", history
    
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
    gr.Markdown("# 🐼 PandasAI: Chat with Your CSV Data")
    
    with gr.Row():
        with gr.Column(scale=2):
            file_upload = gr.File(
                label="Upload CSV File",
            )
            api_key_input = gr.Textbox(
                type="password", 
                label="OpenAI API Key", 
                placeholder="Paste your OpenAI API key here (sk-...)"
            )
        
        with gr.Column(scale=1):
            gr.Markdown(
                """
                ## How to Use
                1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) 🔑
                2. Upload a CSV file 📄
                3. Ask questions about your data 💬
                
                ## About
                PandasAI App allows you to have a conversation with your CSV data using AI. 
                Ask questions and get insights from your spreadsheets!

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
        ### Supported File Format
        - CSV (.csv)
        
        Note: Make sure your file is in CSV format for successful upload and processing.
        """
    )

app.launch()