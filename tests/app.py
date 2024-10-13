import gradio as gr
import pandas as pd

def read_csv(file):
    if file is None:
        return "Please upload a CSV file."
    
    try:
        # Read the uploaded file into a pandas DataFrame
        df = pd.read_csv(file.name)
        
        # Prepare the output string
        output = f"CSV file successfully read into a DataFrame.\n\n"
        output += f"Number of rows: {df.shape[0]}\n"
        output += f"Number of columns: {df.shape[1]}\n"
        output += f"\nColumn names:\n{', '.join(df.columns)}\n"
        output += f"\nFirst 5 rows:\n{df.head().to_string()}"
        
        return output
    except pd.errors.EmptyDataError:
        return "The uploaded file is empty."
    except pd.errors.ParserError:
        return "Unable to parse the file. Make sure it's a valid CSV file."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Create the Gradio interface
iface = gr.Interface(
    fn=read_csv,
    inputs=gr.File(label="Upload CSV File"),
    outputs=gr.Textbox(label="DataFrame Information", lines=10),
    title="CSV File Uploader and Reader",
    description="Upload a CSV file to read it into a pandas DataFrame and view basic information.",
    theme=gr.themes.Soft()
)

# Launch the app
iface.launch()