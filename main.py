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


# # youtube
# from langchain_community.document_loaders.generic import GenericLoader, FileSystemBlobLoader
# from langchain_community.document_loaders.parsers import OpenAIWhisperParser    # youtube audio to text format
# from langchain_community.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
#
# url="https://www.youtube.com/watch?v=jGwO_UgTS7I"
# save_dir="docs/youtube/"
# loader = GenericLoader(
#     YoutubeAudioLoader([url],save_dir),  # fetch from youtube
#     #FileSystemBlobLoader(save_dir, glob="*.m4a"),   #fetch locally
#     OpenAIWhisperParser()
# )
# docs = loader.load()
# print(docs)
# print(docs[0].page_content[0:500])


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



# document splitting
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter

# 스플리팅 예시
# i. RecursiveCharacterTextSpllitter vs. CharacterTextSplitter 비교 예시
chunk_size = 26
chunk_overlap = 4

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)
c_splitter = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

# Recursive Spllitting Details
# ii. 일반적인 텍스트에 주로 사용되는 RecursiveCharacterTextSplitter 예시
some_text = """When writing documents, writers will use document structure to group content. \
This can convey to the reader, which idea's are related. For example, closely related ideas \
are in sentances. Similar ideas are in paragraphs. Paragraphs form a document. \n\n  \
Paragraphs are often delimited with a carriage return or two carriage returns. \
Carriage returns are the "backslash n" you see embedded in this string. \
Sentences have a period at the end, but also, have a space.\
and words are separated by space."""

print(len(some_text))

c_splitter = CharacterTextSplitter(
    chunk_size=450,
    chunk_overlap=0,
    separator = ' '
)
r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=450,
    chunk_overlap=0,
    separators=["\n\n", "\n", " ", ""]
    # 기본 seperator들. 두줄, 한줄, 공백, (공간x, 즉 char by char) 순서로 스플릿이 진행.
)

print(c_splitter.split_text(some_text))
print(r_splitter.split_text(some_text))



# iii. 온점(.)을 seperator로 추가하고 chunk_size를 조금 줄인 예시
r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=0,
    separators=["\n\n", "\n", "\. ", " ", ""]
)
print(r_splitter.split_text(some_text))

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=0,
    separators=["\n\n", "\n", "(?<=\. )", " ", ""]
)
print(r_splitter.split_text(some_text))


from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
pages = loader.load()


from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=150,
    length_function=len
)


"""
pip install python-dotenv
pip install langchain
pip install -U langchain-community
pip install pypdf 

openai --version
pip install --upgrade pip
pip install openai

pip install yt_dlp
pip install pydub

pip install beautifulsoup4



"""

< script
src = "//t1.daumcdn.net/tistory_admin/lib/jquery/jquery-3.5.1.min.js"
integrity = "sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
crossorigin = "anonymous" > < / script >
< !-- <![endif] -->
< script
src = "https://polyfill.io/v3/polyfill.min.js?features=es6" > < / script >
< script
id = "MathJax-script" async src = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" > < / script >



ㅇㅇ
< script
type = "text/x-mathjax-config" >
MathJax.Hub.Config({
    tex2jax: {inlineMath: [['$', '$'], ['\\(', '\\)']]}
});
< / script >
< script
src = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" > < / script >








<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']]
    }
  };
  </script>
  <script type="text/javascript" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>

  <!-- 티스토리 수식 적용 --!>