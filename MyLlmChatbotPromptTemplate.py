from langchain_community.llms import OCIGenAI
from langchain_core.prompts import PromptTemplate

endpoint = "https://generativeai.us-chicago-1.oci.oraclecloud.com"
llm = OCIGenAI(model_id="cohere.command",
               service_endpoint=endpoint,
               comparent_id="test_sunitghosh",
               model_kwargs={"max_tokens": 256})
genai_dev_template = """
You are a chatbot gossiping with GenAI Python Developer(Sunit)
Sunit: {genai_dev_ask} {langchain_term}
:"""
genai_dev_prompt = PromptTemplate(input_variables=["genai_dev_ask",
                                                   "langchain_term"],
                                  template=genai_dev_template)

chain = genai_dev_prompt | llm
response = chain.invoke(
    {"genai_dev_ask": "Write python script for using ",
     "langchain_term": "PromptTemplate"})
print("LangChain PromptTemplate Response =>", response)

# Debug lines
'''
genai_dev_prompt_val = genai_dev_prompt.invoke(
    {"genai_dev_ask": "Write python script for using ",
     "langchain_term": "PromptTemplate"})
print("Prompt String is ->")
print(genai_dev_prompt_val.to_string())
'''
