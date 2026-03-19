import streamlit as st
from ingestion import create_vector_db
from retriever import get_retriever
from classifier import classify_intent
from rag_pipeline import create_rag_chain
from guardrails import validate_output

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="AI Career Digital Twin", layout="wide")

st.title("🤖 AI Career Digital Twin 2025")
st.caption("Your personalized AI career mentor")

# ---------------------------
# Initialize (Run once)
# ---------------------------
@st.cache_resource
def init_system():
    create_vector_db()
    retriever = get_retriever()
    rag_chain = create_rag_chain(retriever)
    return rag_chain

rag_chain = init_system()

# ---------------------------
# Chat History
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# User Input
# ---------------------------
user_input = st.chat_input("Ask your career question...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # ---------------------------
    # AI Processing
    # ---------------------------
    intent = classify_intent(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = rag_chain(user_input)

            answer = result["result"]
            sources = result["source_documents"]

            validated = validate_output(answer, sources)

            response_text = f"""
**🧭 Intent:** {intent}  

{validated.answer}  

**Confidence:** {round(validated.confidence, 2)}
"""

            st.markdown(response_text)

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response_text
    })