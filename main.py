from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

#print(llm.invoke("how can you subscribe our channel"))

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a great video audience"),
    ("user","{input}")
]   
)

chain = prompt | llm 

#print(chain.invoke({"input":"how can you subscribe our channel"}))

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print(chain.invoke({"input":"subscribe our channel"}))