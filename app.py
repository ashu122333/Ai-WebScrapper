import streamlit as st
from scrape import scrape_web, split_dom_content
from llm import parser

st.title("AI-WebScraper")
url_input=st.text_input("Enter the website's LINK to scrape.")
scan_button=st.button("Scrape the Page")


if scan_button:
    info=scrape_web(url_input)
    st.text("Scraped website's contents!!!")
    st.session_state.dom_content=info
    with st.expander("View DOM Content"):
        st.text_area("DOM content", info,height=300)


if "dom_content" in st.session_state:
    parse_description=st.text_area("Describe what you want to get from the scraped data?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content, wait a moment...")
            dom_chunks=split_dom_content(st.session_state.dom_content)
            # print(dom_chunks)
            # print(parse_description)
            parsed_result=parser(dom_chunks,parse_description)
            # print("description is:",parse_description)
            st.write(parsed_result)
