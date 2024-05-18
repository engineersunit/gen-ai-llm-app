from langchain_community.llms import OCIGenAI

endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"

llm = OCIGenAI(
    model_id="cohere.command",
    service_endpoint=endpoint,
    compartment_id="test_compartment_sunitghosh",
    model_kwargs={"max_tokens": 256}
)

response = llm.invoke("Who is Sunit Ghosh?", temperature=0.5)
print("Fixed Text Response => " + response)
