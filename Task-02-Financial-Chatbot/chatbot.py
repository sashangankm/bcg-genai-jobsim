import streamlit as st
import json
from openai import OpenAI
from prompts import SYSTEM_PROMPT

# Initialize OpenAI Client (Requires API key in an .env file or Streamlit secrets)
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def load_financial_data(filepath):
    """Loads the cleaned JSON data from Task 1."""
    with open(filepath, 'r') as file:
        return json.load(file)

st.title("📊 BCG GenAI Financial Chatbot")
st.write("Ask me questions about the company's financial performance!")

# Load the data we extracted in Task 1
try:
    # Adjust path if needed depending on where you run it
    context_data = load_financial_data("../Task-01-Data-Extraction/extracted_metrics.json")
    st.sidebar.success("Financial data loaded successfully.")
    st.sidebar.json(context_data)
except FileNotFoundError:
    st.sidebar.error("Could not find extracted_metrics.json. Please run Task 1 first.")
    context_data = {}

user_question = st.text_input("Enter your financial query:")

if st.button("Analyze"):
    if user_question and context_data:
        # Construct the prompt with the financial context
        context_string = f"Here is the financial data: {json.dumps(context_data)}. "
        full_prompt = context_string + "User Query: " + user_question
        
        st.info("Analyzing data...")
        
        # NOTE: Uncomment the code below when you have your OpenAI API key set up!
        """
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": full_prompt}
            ]
        )
        st.success(response.choices[0].message.content)
        """
        
        # Placeholder response for testing without an API key
        st.success(f"(Mock Response) Based on the data, the Total Revenue is ${context_data.get('Total Revenue (in millions)')} million, and the Net Income is ${context_data.get('Net Income (in millions)')} million. This indicates strong profitability.")
    else:
        st.warning("Please enter a question and ensure data is loaded.")
