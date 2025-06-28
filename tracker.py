import json
from datetime import datetime

DATA_FILE = 'data.json'

def load_data():
    """Load data from the JSON file."""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"entries": []}
    
def save_data(data):
    """Save data to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def log_entry(sucstance):
    data = load_data()
    data['entries'].append({
        'sucstance': sucstance,
        'timestamp': datetime.now().isoformat()
    })
    save_data(data)
    