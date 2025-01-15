from langchain_community.llms import HuggingFaceHub
from src.pipeline import query_pubmed, extract_biotech_steps
from langchain.agents import initialize_agent, Tool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Hugging Face Model
def get_model():
    api_key = os.getenv('HUGGINGFACE_API_TOKEN')
    if not api_key:
        raise ValueError("Hugging Face API token not found. Set it in the .env file.")
    return HuggingFaceHub(repo_id="mistral-2b", model_kwargs={"temperature": 0.7}, token=api_key)

# Define tools
pubmed_tool = Tool(
    name="PubMed Query",
    func=query_pubmed,
    description="Fetches articles from PubMed based on a query."
)

biotech_tool = Tool(
    name="Biotech Step Extractor",
    func=extract_biotech_steps,
    description="Extracts biotech pipeline steps from text."
)

# Initialize the agent
def initialize_biotech_agent():
    llm = get_model()
    tools = [pubmed_tool, biotech_tool]
    return initialize_agent(tools, llm, agent="zero-shot-react-description")

if __name__ == "__main__":
    agent = initialize_biotech_agent()
    query = "CRISPR technology in biotech"
    result = agent.run(query)
    print(result)
