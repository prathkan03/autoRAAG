from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(temperature=0.2)

SUMMARY_PROMPT = PromptTemplate(
    input_variables=["title", "abstract"],
    template="""
Summarize this research paper titled: "{title}"
Abstract:
{abstract}

Summary (include main contributions and 2 limitations):
"""
)

def summarize_paper(title, abstract):
    prompt = SUMMARY_PROMPT.format(title=title, abstract=abstract)
    return llm.invoke(prompt)
