from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import boto3
import os
import streamlit as st

os.environ["AWS_PROFILE"] = "cobot"

#bedrock client

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2"
)

modelID = "anthropic.claude-v2:1"

llm = Bedrock(
    model_id=modelID,
    client=bedrock_client,
    model_kwargs={"max_tokens_to_sample": 2000,"temperature":0.9}
)

def my_chatbot(language,freeform_text):
    prompt = PromptTemplate(
        input_variables=["language", "freeform_text"],
        template="You are a chatbot. You are in {language}.\n\n{freeform_text}"
    )

    bedrock_chain = LLMChain(llm=llm, prompt=prompt)

    response=bedrock_chain({'language':language, 'freeform_text':freeform_text})
    return response

# print(my_chatbot("english","which country is most advanced in technology?"))

st.title("💬 Co-Bot")

language = st.sidebar.selectbox("Language", ["english", "spanish"])

if language:
    freeform_text = st.sidebar.text_area(label="what is your question?",
    max_chars=100)

if freeform_text:
    response = my_chatbot(language,freeform_text)
    st.write(response['text'])