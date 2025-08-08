# AI-POLICY-FORGER

An AI-powered legislative analysis and debate simulation system that facilitates comprehensive policy evaluation through automated debate, judicial review, and amendment and send you the report pdf on you email.

<img width="12272" height="6641" alt="image" src="https://github.com/user-attachments/assets/8c7c9eea-3a99-4222-9367-6571d05148c6" />


## 🚀 Features

- **Automated Legislative Analysis**: Parse and structure complex policy documents
- **Multi-Agent Debate System**: Simulate political discourse between ruling and opposition parties
- **Judicial Review**: AI judges evaluate policies against legal and ethical standards
- **Amendment Suggestions**: Get AI-powered recommendations for policy improvements
- **Comprehensive Reporting**: Detailed debate transcripts and analysis summaries
- **Email Delivery**: Automated PDF report generation and delivery to specified email addresses

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI-POLICY-FORGER.git
   cd AI-POLICY-FORGER
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

## 🚀 Quick Start

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open and run the `demo_version.ipynb` notebook

3. Follow the prompts to analyze your policy document

## 🤖 Agent Architecture

### Core Agents

1. **Bill Parser**
   - Extracts and structures legislative documents
   - Identifies key components (definitions, sections, penalties)

2. **Debate Agents**
   - Ruling Party Agent: Advocates for the policy
   - Opposition Party Agent: Critically analyzes potential issues
   - Debate Moderator: Ensures fair and structured discussion

3. **Judicial Panel**
   - Multiple Judge Agents evaluate the policy
   - Considers legal, ethical, and social implications
   - Provides final verdict and recommendations

4. **Amendment Writer**
   - Suggests specific changes to improve the policy
   - Provides alternative wordings and additional clauses

## 📚 Example Usage

```python
# Initialize the policy analysis system
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent

# Set up your agents
bill_parser = AssistantAgent(
    name="bill_parser_agent",
    system_message="""
    You are BillParserAgent, a legislative document parser within the PolicyForgeAI system.
    Your role is to analyze and structure policy documents.
    """
)

# Add more agent initializations...
```

## 📊 Output

The system generates:
- Structured policy analysis
- Debate transcripts
- Judicial reviews and votes
- Amendment suggestions
- Implementation roadmaps

## ✉️ Email Reporting

AI-POLICY-FORGER includes a powerful email reporting feature that automatically generates and sends comprehensive PDF reports to specified email addresses. These reports include:

- Complete policy analysis
- Debate transcripts
- Judicial reviews and verdicts
- Recommended amendments
- Implementation roadmap

### How to Use Email Reporting

1. Configure your email settings in the `.env` file:
   ```
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-specific-password
   EMAIL_USE_TLS=True
   RECIPIENT_EMAIL=recipient@example.com
   ```

2. The system will automatically generate and send the report when the analysis is complete.

3. Sample report: [Data Privacy Act Review](sample_docs/Data_Privacy_Act_Review.pdf)

## 🌐 API Integration

AI-POLICY-FORGER supports integration with:
- OpenAI API (GPT models)
- Ollama for local model inference
- Custom model endpoints

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

For inquiries or support, please contact me at atharvarai07@gmail.com

## 📄 Documentation

For detailed documentation, please visit [Documentation Link](https://github.com/AtharvaRai07/AUTOGEN-POLICY-FORGER/blob/main/DOCUMENTATION.md)

---

<div align="center">
  Made with ❤️ by Atharva
</div>
