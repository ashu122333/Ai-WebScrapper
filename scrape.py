from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import os

load_dotenv()
os.getenv("GROQ_API_KEY")

def scrape_web(website):
    loader=WebBaseLoader(website)
    page_data=loader.load().pop().page_content
    soup=bs(page_data,"html.parser")
    clean_content=soup.get_text(separator="\n")
    clean_content="\n".join(line.strip() for line in clean_content.splitlines() if line.strip())
    # print(clean_content)
    return clean_content



def split_dom_content(dom_content,max_lenght=6000):
    return [
        dom_content[i:i+max_lenght] for i in range(0,len(dom_content),max_lenght)
    ]
