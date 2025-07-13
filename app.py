import streamlit as st
import os
from groq import Groq
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Dev Mind AI - Your Programming Companion",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    /* Main styling */
    .main-header {
        text-align: center;
        padding: 1.5rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        color: white !important;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
        color: white !important;
    }
    
    /* Sidebar styling */
    .sidebar-content {
        background: linear-gradient(135deg, #2c2c2c 0%, #1e1e1e 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Animation */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Remove any unnecessary white blocks or columns */
    .stApp [data-testid="stHorizontalBlock"] {
        gap: 0 !important;
    }
    
    /* Ensure no extra white spaces */
    .stApp [data-testid="column"] {
        padding: 0 !important;
    }
    
    /* Main content container */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
    
    /* Fix text visibility - make main content text white for dark background */
    .stApp {
        background-color: #1e1e1e !important;
    }
    
    .main .block-container {
        color: white !important;
    }
    
    .main .block-container * {
        color: white !important;
    }
    
    /* Chat messages - white text */
    .stChatMessage {
        color: white !important;
    }
    
    .stChatMessage * {
        color: white !important;
    }
    
    /* Markdown text in main area */
    .main .stMarkdown {
        color: white !important;
    }
    
    .main .stMarkdown * {
        color: white !important;
    }
    
    /* Headers in main area */
    .main h1, .main h2, .main h3, .main h4, .main h5, .main h6 {
        color: white !important;
    }
    
    /* Sidebar - dark background with white text */
    .stApp [data-testid="stSidebar"] {
        background-color: #1e1e1e !important;
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Sidebar headers */
    .stApp [data-testid="stSidebar"] h2 {
        color: white !important;
    }
    
    /* Sidebar markdown content */
    .stApp [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }
    
    .stApp [data-testid="stSidebar"] .stMarkdown * {
        color: white !important;
    }
    
    /* Chat input styling */
    .stChatInput input {
        background-color: #2c2c2c !important;
        color: white !important;
        border: 2px solid #444 !important;
        border-radius: 8px !important;
    }
    
    /* Force main content text to be white */
    .main div, .main span, .main p, .main li, .main strong, .main em {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Groq client
@st.cache_resource
def init_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("⚠️ GROQ_API_KEY not found in environment variables!")
        st.stop()
    return Groq(api_key=api_key)

# System prompt for the programming support chatbot
SYSTEM_PROMPT = """You are Dev-Mind AI, a specialized assistant designed to help programmers with productivity, mental health, and professional development. Your role is to provide:

1. **Productivity Tips**: Practical advice on coding efficiency, time management, and workflow optimization
2. **Burnout Solutions**: Strategies for preventing and recovering from programmer burnout
3. **Tool Recommendations**: Suggest relevant tools, extensions, and resources for developers
4. **Mental Health Support**: Provide emotional support and practical advice for programming-related stress
5. **Career Guidance**: Help with career decisions, skill development, and professional growth

Guidelines:
- Be empathetic and understanding
- Provide actionable, practical advice
- Suggest specific tools with brief explanations
- Keep responses concise but comprehensive
- Always maintain a supportive and encouraging tone
- Include relevant examples when helpful
- Focus on evidence-based solutions

Remember: You're here to support programmers' well-being and productivity, not just solve coding problems."""

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "system",
        "content": SYSTEM_PROMPT
    })

if "groq_client" not in st.session_state:
    st.session_state.groq_client = init_groq_client()

# Main header
st.markdown("""
<div class="main-header">
    <h1>🧠 Dev Mind AI</h1>
    <p>Your AI companion for programming productivity, mental health, and professional growth</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with features and quick actions
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown("## 🚀 Quick Help")
    
    quick_actions = [
        "💡 Give me productivity tips for coding",
        "🔥 Help me deal with burnout",
        "🛠️ Recommend development tools",
        "⏰ Time management for programmers",
        "🧘 Stress management techniques",
        "📚 Learning resources for developers",
        "💼 Career advice for programmers"
    ]
    
    st.markdown("Click on any topic below:")
    for i, action in enumerate(quick_actions):
        if st.button(action, key=f"quick_{i}"):
            # Add the quick action as a user message
            quick_message = action[2:]  # Remove emoji
            st.session_state.messages.append({"role": "user", "content": quick_message})
            
            # Generate AI response for quick action
            try:
                response = st.session_state.groq_client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=st.session_state.messages,
                    max_tokens=1000,
                    temperature=0.7,
                    stream=False
                )
                
                ai_response = response.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                st.rerun()
                
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")

    st.markdown("---")
    st.markdown("## 📊 Features")
    st.markdown("""
    - **Productivity Enhancement**
    - **Burnout Prevention & Recovery**
    - **Mental Health Support**
    - **Career Guidance**
    - **Personalized Advice**
    - **Real-time Chat Support**
    """)
    
    st.markdown("---")
    st.markdown("## 🔄 Actions")
    if st.button("🗑️ Clear Chat History", type="secondary"):
        st.session_state.messages = [st.session_state.messages[0]]  # Keep system prompt
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main chat interface - removed the column layout to fix alignment
st.markdown("## 💬 Chat with Dev Mind AI")

# Display all chat messages using native Streamlit chat components
for message in st.session_state.messages[1:]:  # Skip system prompt
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about programming productivity, burnout, tools, or career advice..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message immediately
    with st.chat_message("user"):
        st.write(prompt)
    
    # Generate and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.groq_client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=st.session_state.messages,
                    max_tokens=1000,
                    temperature=0.7,
                    stream=False
                )
                
                ai_response = response.choices[0].message.content
                st.write(ai_response)
                
                # Add AI response to chat history
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🧠 Dev Mind AI - Supporting programmers' productivity and well-being</p>
    <p>Built with ❤️ using Streamlit and Groq API</p>
</div>
""", unsafe_allow_html=True)
