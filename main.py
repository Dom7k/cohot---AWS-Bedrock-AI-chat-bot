from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import boto3
import os
import streamlit as st