# **Dev Mind AI**

**Your AI companion for programming productivity, mental health, and professional growth**

---
## **Overview**

Dev Mind AI is a specialized Streamlit application designed to help programmers enhance their productivity, manage burnout, and support their mental health journey. Built with a focus on developer well-being, this AI-powered chatbot provides personalized advice, practical tips, and emotional support tailored specifically for the programming community.

## **Features**

### **Core Functionality**
- **Productivity Enhancement**: Get personalized tips for coding efficiency and workflow optimization
- **Burnout Prevention & Recovery**: Evidence-based strategies to prevent and recover from programmer burnout
- **Mental Health Support**: Emotional support and practical advice for programming-related stress
- **Career Guidance**: Professional development advice and career decision support
- **Tool Recommendations**: Curated suggestions for development tools and resources

### **Interactive Chat Interface**
- Real-time AI-powered conversations
- Quick action buttons for common topics
- Clean, dark-themed user interface
- Responsive design for all screen sizes

### **Quick Help Topics**
- Productivity tips for coding
- Burnout management strategies
- Development tool recommendations
- Time management techniques
- Stress management solutions
- Learning resources for developers
- Career advice for programmers

## **Project Structure**

```
dev-mind-ai/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (not tracked in git)
├── README.md             # Project documentation
├── LICENSE               # License file

```

### **Environment Variables**
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

## **Technology Stack**

- **Frontend**: Streamlit
- **AI Model**: Groq API with Llama3-8b-8192
- **Language**: Python
- **Styling**: Custom CSS for enhanced UI/UX

## **Prerequisites**

- Python 3.7 or higher
- Groq API key
- Required Python packages (see requirements.txt)

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dev-mind-ai.git
   cd dev-mind-ai
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

## **Usage**

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`

3. Start chatting with Dev Mind AI about your programming productivity, mental health, or career concerns

## **Quick Start Guide**

1. **Select a Quick Help Topic**: Use the sidebar buttons for instant advice on common developer challenges
2. **Ask Custom Questions**: Type your specific questions in the chat interface
3. **Clear Chat History**: Use the clear button to start fresh conversations
4. **Explore Features**: Browse through productivity tips, burnout solutions, and tool recommendations

## **Configuration**

The application can be customized by modifying the following:

- **System Prompt**: Edit the `SYSTEM_PROMPT` variable to adjust the AI's behavior
- **Model Settings**: Modify the Groq model parameters in the chat completion calls
- **UI Styling**: Customize the CSS in the `st.markdown` sections
- **Quick Actions**: Add or modify the quick help topics in the sidebar

## **API Requirements**

This application requires a valid Groq API key. You can obtain one by:
1. Visiting the Groq website
2. Creating an account
3. Generating an API key
4. Adding it to your environment variables

## **Contributing**

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Support**

If you encounter any issues or have questions about Dev Mind AI, please:
- Open an issue on GitHub
- Check the documentation
- Contact the development team

## **Acknowledgments**

- Built with Streamlit framework
- Powered by Groq API and Llama3 model
- Designed specifically for the developer community's mental health and productivity needs

---

**Dev Mind AI - Supporting programmers' productivity and well-being**
