import json
import argparse

def load_config(filename):
    """Loads a JSON config file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON file!")
        return None

def remove_duplicates(items):
    """Remove duplicate items from a list that may contain dicts."""
    seen = []
    result = []
    for item in items:
        # Convert dict to tuple of sorted items for comparison
        if isinstance(item, dict):
            item_tuple = tuple(sorted(item.items()))
            if item_tuple not in seen:
                seen.append(item_tuple)
                result.append(item)
        else:
            if item not in seen:
                seen.append(item)
                result.append(item)
    return result

def merge_configs(configs):
    """Merges multiple Burp Suite scope configurations."""
    merged = {
        "target": {
            "scope": {
                "include": [],
                "exclude": []
            }
        }
    }
    
    for config in configs:
        if config and "target" in config and "scope" in config["target"]:
            merged["target"]["scope"]["include"].extend(config["target"]["scope"].get("include", []))
            merged["target"]["scope"]["exclude"].extend(config["target"]["scope"].get("exclude", []))
    
    # Remove duplicates (handles both strings and dicts)
    merged["target"]["scope"]["include"] = remove_duplicates(merged["target"]["scope"]["include"])
    merged["target"]["scope"]["exclude"] = remove_duplicates(merged["target"]["scope"]["exclude"])
    
    return merged

def main():
    parser = argparse.ArgumentParser(description="Merge Burp Suite scope configurations (JSON files).")
    parser.add_argument(
        "-f", "--files",
        nargs="+",
        required=True,
        help="List of config files to merge (min 2, max 5). Example: -f config1.json config2.json"
    )
    parser.add_argument(
        "-o", "--output",
        default="merged_scope.json",
        help="Output filename (default: merged_scope.json)"
    )
    args = parser.parse_args()

    if len(args.files) < 2 or len(args.files) > 5:
        print("Error: Specify between 2 and 5 config files.")
        return

    configs = [load_config(f) for f in args.files]
    if None in configs:
        print("\n❌ Failed to merge: Invalid input files.")
        return

    merged_config = merge_configs(configs)
    with open(args.output, 'w') as f:
        json.dump(merged_config, f, indent=4)
    
    print(f"\n✅ Success! Merged config saved to '{args.output}'.")

if __name__ == "__main__":
    main()