# 🛡 ChessCast Security Policy

## **🚀 Reporting Security Issues**
If you discover a security vulnerability, please **DO NOT** post it publicly.
Instead, report it privately by emailing **[thehormat@gmail.com]**. We take security seriously and will respond promptly.

## **🛠 Security Best Practices for Developers**
To ensure ChessCast remains secure and reliable, follow these best practices:

### 🔑 **1. Protect API Keys & Tokens**
- Never expose **API keys** (e.g., Telegram Bot Token, MongoDB URI) in your code.
- Use **environment variables** (`.env`) to store sensitive data.
- **Example:** Instead of hardcoding:
  ```python
  BOT_TOKEN = "your-secret-token"