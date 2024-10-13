# flake8: noqa
import streamlit as st


def faq():
    st.markdown(
        """
# FAQ
## How does Pandasai App work?
When you upload a cleaned CSV, it is converted into pandas dataframe. 
Using OpenAI API, A python code is generated and run as per submitted query or 
prompt.


## Is my data safe?
Yes, your data is safe. Pandasai APp does not store your documents or
questions or API Key. All uploaded data is deleted after you close the browser tab.

## What are the costs associated to using Openai API?
Yes, there is cost associated when using Openai API. Please read the Pricing when signing up.

## Does this App Supports Plots?
This is Work In Progress.Yes, Plots will be supported in future.

## Are the answers 100% accurate?
No, the answers are not 100% accurate. Pandasai App uses the Openai API which tries to match answers close to 100%.
As you are aware, this is still work in progress.

## Support of Other APIs e.g Azure, HuggingFace, Dolly or Bard?
This tool will be expanded to allow use of other LLMs API providers.

## Support of Other APIs e.g Azure, HuggingFace, Dolly or Bard?
This tool will be expanded to allow use of other LLMs API providers.

"""
    )
