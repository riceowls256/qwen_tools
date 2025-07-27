#!/bin/bash

# Qwen Coder 3 Tools Installation Script
set -e

echo "🚀 Installing Qwen Coder 3 Tools..."

# Create directories
mkdir -p ~/.local/bin ~/.config/qwen-coder-3-tools

# Make scripts executable
chmod +x bin/*
chmod +x tools/*

# Install to ~/.local/bin
echo "📦 Installing executables to ~/.local/bin..."
for script in bin/*; do
    basename_script=$(basename "$script")
    cp "$script" ~/.local/bin/"$basename_script"
    chmod +x ~/.local/bin/"$basename_script"
done

# Install tools to ~/.local/bin
echo "📦 Installing tools to ~/.local/bin..."
for tool in tools/*; do
    basename_tool=$(basename "$tool")
    cp "$tool" ~/.local/bin/"$basename_tool"
    chmod +x ~/.local/bin/"$basename_tool"
done

# Add ~/.local/bin to PATH if not already there
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo "📝 Adding ~/.local/bin to PATH..."
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc 2>/dev/null || true
fi

echo "✅ Qwen Coder 3 Tools installed successfully!"
echo ""
echo "🔧 Next steps:"
echo "1. Set your Qwen Coder 3 API key:"
echo "   export QWEN_API_KEY='your-api-key'"
echo "2. Set base URL:"
echo "   export QWEN_BASE_URL='https://dashscope.aliyuncs.com/compatible-mode/v1/'"
echo "3. Use tools:"
echo "   qwen-claude"
echo "   qwen-dashboard"
echo "   init-qwen-project"
echo ""
echo "💡 Don't forget to restart your terminal or run: source ~/.bashrc"