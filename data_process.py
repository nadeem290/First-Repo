import json

data = {
    "name": "Pipeline",
    "status": "running"
}

print("🔍 Data as JSON:")
print(json.dumps(data, indent=2))
