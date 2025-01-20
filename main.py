from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

print(llm.invoke("how can langsmith help with testing?"))

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm 

chain.invoke({"input": "how can langsmith help with testing?"})

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print(chain.invoke({"input": "how can langsmith help with testing?"}))



