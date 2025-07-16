import requests
from typing import Dict, List
from dotenv import find_dotenv, get_key

# ✅ OpenAI Agents SDK imports
from agents import Agent, Runner, function_tool, set_tracing_disabled, RunConfig
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

# ✅ Run Configuration
config = RunConfig(
    model=model,
    model_provider=model,
    tracing_disabled=True
)

# ✅ In-memory cart
cart: List[Dict] = []

# ✅ Get All Products
@function_tool
def furniture_store() -> Dict:
    """
    Fetch product data from furniture store API.
    """
    url = "https://hackathon-apis.vercel.app/api/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()
        return {"status": "success", "data": products}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

# ✅ Search Product
@function_tool
def search_product(query: str) -> Dict:
    """
    Search for products by name, category, or color.
    """
    url = "https://hackathon-apis.vercel.app/api/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()

        filtered = [
            p for p in products
            if query.lower() in p["name"].lower()
            or query.lower() in p["category"].lower()
            or query.lower() in p["color"].lower()
        ]
        return {"status": "success", "results": filtered}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

# ✅ Add to Cart
@function_tool
def add_to_cart(product_id: str, quantity: int = 1) -> Dict:
    url = "https://hackathon-apis.vercel.app/api/products"
    try:
        response = requests.get(url)
        products = response.json()
        product = next((item for item in products if item["_id"] == product_id), None)

        if not product:
            return {"status": "error", "message": "Product not found."}

        cart.append({"product": product, "quantity": quantity})
        return {"status": "success", "message": f"{product['name']} added to cart."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ✅ Checkout Cart
@function_tool
def checkout_cart(payment_method: str = "credit_card") -> Dict:
    if not cart:
        return {"status": "error", "message": "Your cart is empty."}

    total = sum(item["product"]["price"] * item["quantity"] for item in cart)
    details = [
        {
            "name": item["product"]["name"],
            "quantity": item["quantity"],
            "price_each": item["product"]["price"],
            "total_price": item["product"]["price"] * item["quantity"]
        }
        for item in cart
    ]
    cart.clear()
    return {
        "status": "success",
        "message": "Checkout complete.",
        "total_amount": total,
        "payment_method": payment_method,
        "purchased_items": details
    }

# ✅ Request Refund
@function_tool
def request_refund(product_name: str, reason: str) -> Dict:
    return {
        "status": "success",
        "message": f"Refund request for '{product_name}' submitted. Reason: {reason}"
    }

# ✅ Define the Agent
agent = Agent(
    name="Shopping Agent",
    instructions="""
    You are a smart shopping assistant. You can:
    - show available products
    - search for products
    - add items to cart
    - perform checkout with total price and payment method
    - submit refund requests
    """,
    model=model,
    tools=[
        furniture_store,
        search_product,
        add_to_cart,
        checkout_cart,
        request_refund
    ]
)

# ✅ Run Agent Interactively
if __name__ == "__main__":
    while True:
        query = input("\n🤖 Ask your Shopping Assistant something (or type 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            break
        result = Runner.run_sync(agent, input=query, run_config=config)
        print(f"\n📝 Response:\n{result.final_output}")
