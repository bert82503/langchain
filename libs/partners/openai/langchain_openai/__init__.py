from langchain_openai.chat_models import (
    AzureChatOpenAI,
    ChatOpenAI,
)
from langchain_openai.embeddings import (
    AzureOpenAIEmbeddings,
    OpenAIEmbeddings,
)
from langchain_openai.llms import AzureOpenAI, OpenAI

# 开放人工智能模型
# LLM, Large Language Model, 大语言模型
# OpenAI, GPT, Generative Pre-trained Transformer
# ChatOpenAI, ChatGPT
__all__ = [
    "OpenAI",
    "ChatOpenAI",
    "OpenAIEmbeddings",
    "AzureOpenAI",
    "AzureChatOpenAI",
    "AzureOpenAIEmbeddings",
]
