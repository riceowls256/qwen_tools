# Qwen Coder 3 Tools

🤖 **Qwen Coder 3 Integration for Claude Code and Development Tools**

Similar to kimik2-tools but for Alibaba's Qwen Coder 3. Provides seamless integration between Qwen Coder 3 and Claude Code.

## 🚀 Quick Start

### **Installation**
```bash
git clone https://github.com/riceowls256/qwen_tools.git
cd qwen_tools
./install.sh
```

### **Usage**
```bash
# Start official Qwen Code CLI
qwen-code                    # Interactive mode
qwen-code 'write a function' # Direct prompt

# Track usage and costs
qwen-dashboard

# Initialize project-specific settings
init-qwen-project

# Legacy integration (Claude Code wrapper)
qwen-claude
```

## 📋 Prerequisites

- **Python 3.7+**
- **Node.js 14+** (for dashboard)
- **Qwen Coder 3 API Key** from [Qwen Platform](https://platform.qwen.aliyun.com)

## 🔧 Configuration

### **Global Setup**
```bash
# Set your Qwen Coder 3 API key
export QWEN_API_KEY="your-qwen-coder-3-api-key"

# Set base URL
export QWEN_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1/"
```

### **Project Setup**
```bash
# Initialize Qwen Coder 3 in your project
init-qwen-project
```

## 🎯 Features

- **Cost Tracking**: Monitor Qwen Coder 3 usage and costs
- **Project Isolation**: Per-project Qwen Coder 3 settings
- **Usage Dashboard**: Visual tracking of API calls and expenses
- **Configuration Management**: Easy setup and switching between projects
- **Compatible with Claude Code**: Drop-in replacement for Anthropic API