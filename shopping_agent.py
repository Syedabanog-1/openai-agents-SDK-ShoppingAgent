import requests
from typing import Dict
from dotenv import find_dotenv, get_key

# ✅ OpenAI Agents SDK imports
from agents import Agent, Runner, function_tool, set_tracing_disabled , RunConfig
from agents.extensions.models.litellm_model import LitellmModel

# ✅ Disable tracing (optional)
set_tracing_disabled(True)

# ✅ Load Gemini API Key from .env
GEMINI_API_KEY = get_key(find_dotenv(), "GOOGLE_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY is not set in your .env file.")

# ✅ Define the model using Gemini
model = LitellmModel(
    model="gemini/gemini-2.0-flash",
    api_key=GEMINI_API_KEY
)

# ✅ Define Run Configuration
config = RunConfig(
    model=model,
    model_provider=model,
    tracing_disabled=True
)

# ✅ Tool to fetch products
@function_tool
def furniture_store() -> Dict:
    """
    Fetch product data from furniture store API.
    """
    url = "https://giaic-hackathon-template-08.vercel.app/api/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()
        return {"status": "success", "data": products}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}
    
agent = Agent(
    name="Shopping Agent",
    instructions="""
    You are a shopping assistant. Use the 'furniture_store' tool to fetch product data.
    Show each product with name, price, category, colors, stock, and description.
    Present using rich formate
    """,
    model=model,
    tools=[furniture_store]
)
# ✅ Run the agent with a sample query
if __name__ == "__main__":
    result = Runner.run_sync(
        agent,
        input="Show me the list of available furniture products.",
        run_config=config
    )
    print(result.final_output)
