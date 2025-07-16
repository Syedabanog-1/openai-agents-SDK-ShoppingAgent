# 🛒 Shopping Assistant Agent (Furniture Store)

This project is a *shopping assistant agent* that interacts with a *furniture store API, using the **OpenAI Agents SDK* with the *Gemini 2.0 Flash model* via the LitellmModel. It fetches furniture product details and displays them.
## 🚀 Features

- Uses OpenAI Agent SDK and Gemini model
- Fetches product data from a live furniture store API
- Displays product name, price, category, colors, stock status, and description
- Provides a simple shopping assistant interface
- CLI-ready for testing via __main__
- 
🧠 How It Works
LitellmModel connects to Gemini

function_tool furniture_store() fetches product data

Agent uses this tool in response to user queries

Runner.run_sync() executes the agent and prints the final output

***Key Functional Points:
Feature	Description
✅ Gemini API Integration	Loads the Gemini 2.0 Flash model via API key stored in .env.
✅ Agents SDK Usage	Uses Agent, Runner, and function_tool from OpenAI Agents SDK.
✅ Custom Tool (furniture_store)	A decorated function that fetches product data from the given API URL.
✅ Error Handling	Gracefully handles HTTP request errors and reports issues.
✅ Agent Definition	An agent called "Shopping Agent" is defined with clear instructions and tool usage.
✅ Run Configuration (RunConfig)	Specifies model settings and disables tracing.
✅ Sample Query Execution	Runs the agent with the input: "Show me the list of available furniture products." and prints results.

FUNCTIONAL TOOL:
    
        furniture_store:  -retrieve available data record
        search_product:   -Find desired data 
        add_to_cart:      -Add purchasing items to cart
        checkout_cart:    -Ask payment method and get information of purchased items total cost and  name & quantity 
        request_refund    -Ask reason for refund
        

<img width="1611" height="905" alt="available products with detail" src="https://github.com/user-attachments/assets/7ee001c0-6762-429b-ac18-ccc0bf6fb1c5" />
<img width="1610" height="902" alt="functional code" src="https://github.com/user-attachments/assets/3f796704-a91a-4292-84b4-84d0f65e779a" />
<img width="1610" height="905" alt="product detail with id" src="https://github.com/user-attachments/assets/3ad6979d-d5d4-475d-b887-2e975b088943" />
<img width="1610" height="902" alt="functional code" src="https://github.com/user-attachments/assets/d4b02cf5-fce8-4508-87a4-dcf0f6f48d02" />
<img width="1613" height="905" alt="product list" src="https://github.com/user-attachments/assets/45810044-c6cb-4961-83b9-711b6b8c6f42" />
<img width="1611" height="904" alt="one code-output" src="https://github.com/user-attachments/assets/4234da4a-c7d1-4443-aab7-e24f6cc9252f" />
<img width="1611" height="907" alt="two -output result" src="https://github.com/user-attachments/assets/0e127438-252a-4fc4-b8e6-0e99ae946821" />
<img width="1613" height="904" alt="three output display" src="https://github.com/user-attachments/assets/c91891f6-3458-4034-8282-33666e460b61" />





