# 🔄 Burp Suite Scope Config Merger

A Python utility for merging multiple Burp Suite scope configuration files into a single unified JSON file.

## ✨ Features
- **Multi-file merging**: Combine 2-5 JSON configuration files
- **Rule preservation**: Handles both URL strings and complex rule dictionaries
- **Duplicate removal**: Intelligent deduplication algorithm
- **Burp-compatible**: Maintains proper scope structure
- **CLI interface**: Simple command-line operation

## 📥 Installation
```bash
git clone https://github.com/yourusername/burp-scope-merger.git
cd burp-scope-merger
```

 Usage
Basic Command

```bash
python3 scope.py -f file1.json file2.json [-o output.json]
```

Options

```-f/--files```  	Input JSON files (2-5)	✅ Yes

```-o/--output``` 	Output filename	❌ No

Configuration Format
Input Example

```
{
  "target": {
    "scope": {
      "include": [
        "https://example.com",
        {"enabled": true, "file": "^login\\.php$"}
      ],
      "exclude": ["https://staging.example.com"]
    }
  }
}

```

🐛 Troubleshooting

Error	Solution

```File not found``` 	Verify file paths

```Invalid JSON```  	Validate JSON syntax

```Unhashable type```	Check rule formatting
