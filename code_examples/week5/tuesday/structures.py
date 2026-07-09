import json

# classifies type of structure for data
def classify(value, source_hint: str = "") -> str:
    """Rough heuristic: structured / semi-structured / unstructured."""
    hint = source_hint.lower()
    if any(k in hint for k in ("csv", "sql", "table", "parquet")):
        return "structured"
    if any(k in hint for k in ("json", "xml", "yaml")):
        return "semi-structured"
    if any(k in hint for k in ("pdf", "jpg", "png", "mp4", "wav", "txt")):
        return "unstructured"

    # No hint: inspect the value itself.
    if isinstance(value, list) and value and all(isinstance(r, dict) for r in value):
        keys = set(value[0])
        same_keys = all(set(r) == keys for r in value)
        flat = all(not isinstance(v, (dict, list)) for r in value for v in r.values())
        return "structured" if (same_keys and flat) else "semi-structured"
    if isinstance(value, (dict, list)):
        return "semi-structured"
    if isinstance(value, (bytes, str)):
        try:
            json.loads(value)            # a JSON string is semi-structured
            return "semi-structured"
        except (ValueError, TypeError):
            return "unstructured"        # raw text / bytes
    return "unstructured"


# Structured: list of flat dicts, identical keys
print(classify([{"id": 1, "amt": 9.9}, {"id": 2, "amt": 5.0}]))   # structured

# Semi-structured: nested
print(classify({"id": 1, "name": {"first": "Ada"}, "tags": ["x"]}))  # semi-structured

# Unstructured: free text
print(classify("The invoice total is about five thousand dollars."))  # unstructured