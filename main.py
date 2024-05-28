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
