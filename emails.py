from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature = 0,
    groq_api_key = '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',
    model_name = "llama-3.1-70b-versatile"
)
response = llm.invoke("The first person to land on moon")
print(response.content)