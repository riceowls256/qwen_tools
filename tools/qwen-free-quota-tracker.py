#!/usr/bin/env python3
"""
Qwen Free Quota Tracker
Tracks free token usage and remaining quota for all Qwen models
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

class QwenFreeQuotaTracker:
    def __init__(self):
        self.config_dir = Path.home() / ".config" / "qwen-coder-3-tools"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.usage_file = self.config_dir / "free_quota_usage.json"
        self.start_date_file = self.config_dir / "activation_date.txt"
        
        # Initialize activation date if not exists
        if not self.start_date_file.exists():
            with open(self.start_date_file, 'w') as f:
                f.write(datetime.now().isoformat())
    
    def log_usage(self, model, tokens_input, tokens_output):
        """Log free quota usage"""
        usage_data = {
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "tokens_input": tokens_input,
            "tokens_output": tokens_output,
            "project": os.getcwd().split('/')[-1]
        }
        
        with open(self.usage_file, 'a') as f:
            f.write(json.dumps(usage_data) + '\n')
    
    def get_free_quota_usage(self):
        """Get usage against free quota"""
        # Read activation date
        with open(self.start_date_file, 'r') as f:
            activation_date = datetime.fromisoformat(f.read().strip())
        
        # 180 days validity period
        expiry_date = activation_date + timedelta(days=180)
        
        # Free quota limits (1 million tokens each)
        free_quotas = {
            "qwen-max": 1000000,
            "qwen-plus": 1000000,
            "qwen-turbo": 1000000,
            "qwen3-coder-plus": 1000000,
            "qwen3-coder-turbo": 1000000,
            "qwq-plus": 1000000,
            "qvq-max": 1000000,
            "qwen-vl-max": 1000000,
            "qwen-vl-plus": 1000000,
            "qwen-omni-turbo": 1000000,
            "qwen3-72b-instruct": 1000000,
            "qwen3-32b-instruct": 1000000,
            "qwen3-8b-instruct": 1000000,
            "qwen3-7b-instruct": 1000000,
            "qwen3-1.5b-instruct": 1000000,
            "qwen3-0.5b-instruct": 1000000
        }
        
        # Calculate usage
        usage = {model: {"input": 0, "output": 0, "total": 0} for model in free_quotas}
        
        if self.usage_file.exists():
            with open(self.usage_file, 'r') as f:
                for line in f:
                    try:
                        entry = json.loads(line.strip())
                        model = entry['model']
                        if model in usage:
                            usage[model]['input'] += entry.get('tokens_input', 0)
                            usage[model]['output'] += entry.get('tokens_output', 0)
                            usage[model]['total'] += entry.get('tokens_input', 0) + entry.get('tokens_output', 0)
                    except:
                        continue
        
        return {
            "activation_date": activation_date.isoformat(),
            "expiry_date": expiry_date.isoformat(),
            "days_remaining": max(0, (expiry_date - datetime.now()).days),
            "usage": usage,
            "quotas": free_quotas
        }
    
    def display_quota_report(self):
        """Display comprehensive quota report"""
        report = self.get_free_quota_usage()
        
        print("🎁 Qwen Free Quota Tracker")
        print("=" * 50)
        print(f"📅 Activation: {report['activation_date'][:10]}")
        print(f"📅 Expires: {report['expiry_date'][:10]}")
        print(f"⏰ Days remaining: {report['days_remaining']}")
        print()
        
        print("📊 Model Usage (against 1M free tokens):")
        print("-" * 60)
        
        total_used = 0
        for model, quota in report['quotas'].items():
            used = report['usage'][model]['total']
            remaining = max(0, quota - used)
            percentage = (used / quota) * 100 if quota > 0 else 0
            
            if used > 0 or model in ["qwen3-coder-plus", "qwen-plus", "qwen-turbo", "qwen-max"]:
                status = "✅" if remaining > 0 else "❌"
                print(f"{status} {model:25} {used:>8,} / {quota:,} ({percentage:>5.1f}%) {remaining:>8,} remaining")
                total_used += used
        
        print("-" * 60)
        print(f"📈 Total tokens used: {total_used:,}")
        print(f"💰 Money saved: ${total_used/1000000 * 0.5:.2f} (estimated)")
        
        if report['days_remaining'] <= 7:
            print("⚠️  Expires soon! Days remaining:", report['days_remaining'])
    
    def reset_quota(self):
        """Reset quota tracking (for testing)"""
        if self.usage_file.exists():
            self.usage_file.unlink()
        with open(self.start_date_file, 'w') as f:
            f.write(datetime.now().isoformat())
        print("✅ Free quota tracking reset")

def main():
    import sys
    
    tracker = QwenFreeQuotaTracker()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--reset":
            tracker.reset_quota()
        elif sys.argv[1] == "--log":
            if len(sys.argv) > 3:
                model = sys.argv[2]
                tokens_input = int(sys.argv[3])
                tokens_output = int(sys.argv[4]) if len(sys.argv) > 4 else 0
                tracker.log_usage(model, tokens_input, tokens_output)
                print(f"✅ Logged usage for {model}: {tokens_input + tokens_output:,} tokens")
        else:
            tracker.display_quota_report()
    else:
        tracker.display_quota_report()

if __name__ == "__main__":
    main()