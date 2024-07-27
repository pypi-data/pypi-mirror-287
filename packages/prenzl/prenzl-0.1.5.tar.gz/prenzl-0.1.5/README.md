# Prenzl AI agent observbility tool for agents and advanced RAG
This is the python sdk of Prenzl AI - an agent and advanced RAG observability tool.

### Installation
```
pip install prenzl
```

### Using Prenzl AI Observability
```
import os
from prenzl import prenzl_observe

os.environ["PRENZL_API_KEY"] = "YOUR_API_KEY"

# If you are not using the hosted service:
# os.environ["PRENZL_BASE_URL"] = "YOUR_URL"

# Initialize the observer
prenzl = Prenzl(api_key=os.environ["PRENZL_API_KEY"])

# Write observed data into DB
data = "Here goes your data you want to log in a JSON file."
result = prenzl.prenzl_observe(data)
```

The PyPI website for Prenzl AI can be found here: https://pypi.org/project/prenzl/

