import re
from io import BytesIO
from typing import Any, Dict, List
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import pandas as pd
import streamlit as st

def clear_submit():
    """
    Clear the Submit Button State
    Returns:

    """
    st.session_state["submit"] = False


def run_pandasai_openaiapi(df, prompt, verbose=False):
    """
    A function to run the Query on given Pandas Dataframe
    Args:
        df: Pandas dataframe
        prompt: Query / Prompt related to data
        verbose: A parameter to show the intermediate code generation

    Returns: Response / Results

    """

    llm = OpenAI(api_token=st.session_state.get("OPENAI_API_KEY"))
    pandas_ai = PandasAI(llm, verbose=verbose)
    response = pandas_ai.run(df, prompt=prompt)

    return response


st.cache_data()
def parse_csv(file: BytesIO) -> str:
    """
    A function to read the csv File
    Args:
        file: File Location

    Returns: Pandas dataframe

    """
    df = pd.read_csv(file)

    return df


