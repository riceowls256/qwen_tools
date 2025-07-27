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

# Install qwen-code CLI
echo "📦 Installing official qwen-code CLI..."
./bin/qwen-code-setup

# Install qwen-claude wrapper
echo "📦 Installing qwen-claude wrapper..."
cp bin/qwen-claude ~/.local/bin/qwen-claude
chmod +x ~/.local/bin/qwen-claude

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

# Create global Qwen configuration
GLOBAL_CONFIG="$HOME/.config/qwen-coder-3-tools/global.env"
mkdir -p "$(dirname "$GLOBAL_CONFIG")"

echo "📝 Creating global Qwen configuration..."
cat > "$GLOBAL_CONFIG" << 'EOF'
# Global Qwen API Configuration
# Set your Qwen API key here for all projects
# export QWEN_API_KEY="your-dashscope-api-key"
export QWEN_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1/"
export QWEN_MODEL="qwen3-coder-plus"
EOF

# Add source command to shell profiles
for shell_file in ~/.bashrc ~/.zshrc; do
    if [[ -f "$shell_file" ]]; then
        if ! grep -q "source $GLOBAL_CONFIG" "$shell_file" 2>/dev/null; then
            echo "" >> "$shell_file"
            echo "# Qwen Coder 3 Global Configuration" >> "$shell_file"
            echo "source $GLOBAL_CONFIG" >> "$shell_file"
        fi
    fi
done

echo "✅ Qwen Coder 3 Tools installed successfully!"
echo ""
echo "🔧 Next steps:"
echo "1. Set your Qwen Coder 3 API key:"
echo "   export QWEN_API_KEY='your-api-key'"
echo "2. Set base URL:"
echo "   export QWEN_BASE_URL='https://dashscope.aliyuncs.com/compatible-mode/v1/'"
echo "3. Use tools:"
echo "   qwen-claude                # Interactive model selection"
echo "   qwen-claude --help         # Use selected model directly"
echo "   qwen-dashboard             # Free quota tracking"
echo "   init-qwen-project          # Project initialization"
echo ""
echo "💡 Interactive features:"
echo "   - qwen-claude shows current model and prompts for selection"
echo "   - Model choice persists across sessions"
echo "   - 16 Qwen models available with descriptions"
echo ""
echo "💡 Global setup complete - API key persists across all projects!"
echo "   Config file: ~/.config/qwen-coder-3-tools/global.env"
echo "   Run: source ~/.bashrc  # or ~/.zshrc to reload"