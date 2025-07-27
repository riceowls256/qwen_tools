#!/usr/bin/env python3
"""
Qwen Coder 3 Usage Tracker
Tracks API usage and costs for Qwen Coder 3 integration
"""

import json
import os
import requests
from datetime import datetime, timedelta
from pathlib import Path

class QwenUsageTracker:
    def __init__(self, api_key=None, base_url=None):
        self.api_key = api_key or os.getenv('QWEN_API_KEY')
        self.base_url = base_url or os.getenv('QWEN_BASE_URL', 'https://dashscope.aliyuncs.com/compatible-mode/v1/')
        self.config_dir = Path.home() / ".config" / "qwen-coder-3-tools"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.usage_file = self.config_dir / "usage.json"
    
    def log_usage(self, model, tokens_input, tokens_output, cost):
        """Log API usage to file"""
        usage_data = {
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "tokens_input": tokens_input,
            "tokens_output": tokens_output,
            "cost": cost,
            "project": os.getcwd().split('/')[-1]
        }
        
        with open(self.usage_file, 'a') as f:
            f.write(json.dumps(usage_data) + '\n')
    
    def get_usage_summary(self, days=7):
        """Get usage summary for last N days"""
        if not self.usage_file.exists():
            return []
        
        cutoff_date = datetime.now().date() - timedelta(days=days)
        usage_data = []
        
        with open(self.usage_file, 'r') as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    entry_date = datetime.fromisoformat(entry['timestamp']).date()
                    if entry_date >= cutoff_date:
                        usage_data.append(entry)
                except:
                    continue
        
        return usage_data
    
    def generate_report(self, days=7):
        """Generate usage report"""
        usage_data = self.get_usage_summary(days)
        
        if not usage_data:
            print("📊 No usage data found")
            return
        
        # Calculate totals
        total_cost = sum(entry['cost'] for entry in usage_data)
        total_input = sum(entry['tokens_input'] for entry in usage_data)
        total_output = sum(entry['tokens_output'] for entry in usage_data)
        
        # Group by model
        model_usage = {}
        for entry in usage_data:
            model = entry['model']
            if model not in model_usage:
                model_usage[model] = {'cost': 0, 'input': 0, 'output': 0}
            model_usage[model]['cost'] += entry['cost']
            model_usage[model]['input'] += entry['tokens_input']
            model_usage[model]['output'] += entry['tokens_output']
        
        print("🤖 Qwen Coder 3 Usage Report")
        print("=" * 50)
        print(f"📅 Period: Last {days} days")
        print(f"💰 Total Cost: ${total_cost:.4f}")
        print(f"📊 Total Tokens: {total_input + total_output:,} ({total_input:,} in, {total_output:,} out)")
        print()
        
        if model_usage:
            print("📈 Model Usage:")
            for model, data in model_usage.items():
                print(f"  {model}: ${data['cost']:.4f} ({data['input'] + data['output']:,} tokens)")
        
        print()
        print("📋 Recent Activity:")
        for entry in usage_data[-5:]:
            time = datetime.fromisoformat(entry['timestamp']).strftime('%m-%d %H:%M')
            print(f"  {time} - {entry['model']}: ${entry['cost']:.4f} ({entry['project']})")

if __name__ == "__main__":
    import sys
    
    tracker = QwenUsageTracker()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--report":
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
            tracker.generate_report(days)
        elif sys.argv[1] == "--log":
            if len(sys.argv) > 4:
                model = sys.argv[2]
                input_tokens = int(sys.argv[3])
                output_tokens = int(sys.argv[4])
                cost = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
                tracker.log_usage(model, input_tokens, output_tokens, cost)
                print(f"✅ Logged usage for {model}: ${cost:.4f}")
    else:
        tracker.generate_report(7)