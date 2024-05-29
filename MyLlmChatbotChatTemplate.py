from langchain_community.llms import OCIGenAI
from langchain_core.prompts import ChatPromptTemplate

endpoint = "https://hostname.oci.oraclecloud.com"
llm = OCIGenAI(model_id="cohere.command",
               service_endpoint=endpoint,
               comparent_id="test_sunitghosh",
               model_kwargs={"max_tokens": 256})

genai_dev_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a langchain teaching chatbot"),
        ("ai", "I will teach langchain to human"),
        ("human", "{input}"),
    ]
)

chain = genai_dev_prompt | llm
response = chain.invoke(
    {"input": "How to use class ChatPromptTemplate?"})
print("Chatbot Response - > " + response)
