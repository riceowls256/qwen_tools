# Qwen Coder 3 Tools - User Guide

## 🚀 Getting Started

### **Step 1: Install Qwen Coder 3 Tools**
```bash
git clone https://github.com/riceowls256/qwen-coder-3-tools.git
cd qwen-coder-3-tools
./install.sh
```

### **Step 2: Get Qwen Coder 3 API Key**
1. Go to [Qwen Platform](https://platform.qwen.aliyun.com)
2. Create an account and get your API key
3. Set the environment variable:
   ```bash
   export QWEN_API_KEY="your-actual-api-key"
   ```

### **Step 3: Start Using**
```bash
# Start Claude Code with Qwen Coder 3
qwen-claude

# Initialize Qwen in your project
init-qwen-project

# Start tracking usage
qwen-dashboard --daily
```

## 📋 Usage Examples

### **Basic Claude Code Integration**
```bash
# Start interactive session
qwen-claude

# Use specific model
QWEN_MODEL=qwen-coder-3-1.5b-instruct qwen-claude

# Use custom configuration
qwen-claude --config ./my-config.json
```

### **Project Initialization**
```bash
# In your project directory
init-qwen-project

# This creates:
# - .qwen/config.json (project-specific settings)
# - .qwen/.env.template (environment variables)
# - .qwen/logs/ (usage logs)
```

### **Usage Monitoring**
```bash
# Daily usage report
qwen-dashboard --daily

# Weekly usage report
qwen-dashboard --weekly

# Custom period
qwen-dashboard --report 30

# Log usage manually
qwen-usage-tracker --log qwen-coder-3-7b-instruct 1000 200 0.0003
```

## 🔧 Configuration

### **Global Configuration**
Create `~/.config/qwen-coder-3-tools/config.json`:
```json
{
  "default_model": "qwen-coder-3-7b-instruct",
  "api_settings": {
    "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1/",
    "timeout": 30
  }
}
```

### **Project Configuration**
Edit `.qwen/config.json` in your project:
```json
{
  "project_name": "my-project",
  "qwen_model": "qwen-coder-3-7b-instruct",
  "settings": {
    "max_tokens": 4000,
    "temperature": 0.7
  }
}
```

### **Environment Variables**
```bash
# Required
export QWEN_API_KEY="your-api-key"

# Optional
export QWEN_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1/"
export QWEN_MODEL="qwen-coder-3-7b-instruct"
```

## 💰 Cost Tracking

### **Model Pricing** (as of 2025)
- **qwen-coder-3-7b-instruct**: $0.0001/1K input, $0.0002/1K output
- **qwen-coder-3-1.5b-instruct**: $0.00005/1K input, $0.0001/1K output

### **Cost Monitoring**
```bash
# Check current costs
qwen-dashboard --daily

# Export detailed report
qwen-usage-tracker --report 7 > usage_report.json
```

## 🎯 Common Workflows

### **1. New Project Setup**
```bash
# In your project directory
init-qwen-project
cp .qwen/.env.template .qwen/.env
# Edit .qwen/.env with your API key
qwen-claude
```

### **2. Daily Development**
```bash
# Start your day
qwen-dashboard --daily

# Start coding session
qwen-claude

# Check costs at end of day
qwen-dashboard --report 1
```

### **3. Team Setup**
```bash
# Share project configuration
git add .qwen/config.json .qwen/.gitignore
git commit -m "Add Qwen Coder 3 configuration"

# Team members clone and:
cp .qwen/.env.template .qwen/.env
# Add their own API key to .qwen/.env
```

## 🔍 Troubleshooting

### **"API key not found"**
```bash
# Check if API key is set
echo $QWEN_API_KEY

# If empty, set it
export QWEN_API_KEY="your-actual-api-key"
```

### **"Connection failed"**
```bash
# Check base URL
echo $QWEN_BASE_URL

# Test connection
curl -H "Authorization: Bearer $QWEN_API_KEY" \
     $QWEN_BASE_URL/models
```

### **"Command not found"**
```bash
# Ensure tools are in PATH
echo $PATH | grep -q "$HOME/.local/bin" || source ~/.bashrc

# Re-run install
./install.sh
```

## 📊 Advanced Usage

### **Custom Models**
```bash
# Use different models
QWEN_MODEL=qwen-coder-3-1.5b-instruct qwen-claude
QWEN_MODEL=qwen-coder-3-7b-instruct qwen-claude
```

### **Batch Processing**
```bash
# Process multiple files
find . -name "*.py" -exec qwen-claude --batch {} \;
```

### **Integration with CI/CD**
```yaml
# GitHub Actions example
- name: Setup Qwen Coder 3
  run: |
    git clone https://github.com/riceowls256/qwen-coder-3-tools.git
    ./qwen-coder-3-tools/install.sh
    export QWEN_API_KEY=${{ secrets.QWEN_API_KEY }}
```

## 🎉 Next Steps

1. **Get your API key** from [Qwen Platform](https://platform.qwen.aliyun.com)
2. **Install the tools** with `./install.sh`
3. **Set up your first project** with `init-qwen-project`
4. **Start coding** with `qwen-claude`
5. **Monitor costs** with `qwen-dashboard`

---

**💡 Tip**: Start with the 7B model for most tasks, and use the 1.5B model for lightweight operations to save costs!