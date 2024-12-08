import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
# import chromadb.utils.embedding_functions as embedding_functions

load_dotenv()


llm=ChatGroq(
    # model="llama-3.2-90b-text-preview",
    model="llama-3.1-70b-versatile",       #can choice any model from Groq website, Its FREEEE!!
    api_key=os.getenv("GROQ_API_KEY"),     # Provide a groq api Key from groq website
    temperature=0)


prompt_template=PromptTemplate.from_template('''
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
''')




def parser(dom_chunks,parse_description):
    chain=prompt_template | llm
    parsed_results=""
    print(f"Number of DOM chunks: {len(dom_chunks)}")
    for i , chunk in enumerate(dom_chunks,start=1):
        response=chain.invoke(input={"dom_content":chunk,"parse_description":parse_description})
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        print(dom_chunks)
        parsed_results=parsed_results+"\n"+response.content
    # print("\n".join(parsed_results))    
    # return "\n".join(parsed_results) 

    return parsed_results
