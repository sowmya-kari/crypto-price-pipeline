from datetime import datetime

def transform_data(data):
    now = datetime.utcnow()
    result = []

    for name, details in data.items():
        result.append({
            "name": name.capitalize(),
            "symbol": name[:3].upper(),
            "price_usd": details["usd"],
            "timestamp": now
        })

    return result
