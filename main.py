import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv
sys.path.append('../..')

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

# document loading
# pdf
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("docs/lectures/MachineLearning-Lecture01.pdf")
pages = loader.load()

print(len(pages))
page = pages[0]
print(page.page_content[0:500])
print(page.metadata)


# url
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.tate.org.uk/art/art-terms/d/documentary-photography")
docs = loader.load()
print(docs[0].page_content[:500])


# notion
from langchain_community.document_loaders import NotionDirectoryLoader
loader = NotionDirectoryLoader("docs/notion_db")
docs = loader.load()

print(docs[0].page_content[0:200])
print(docs[0].metadata)