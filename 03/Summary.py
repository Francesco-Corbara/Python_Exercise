def create_summary(devices_dict: dict) -> dict:
    summary_data = {
        "total": len(devices_dict),
        "OK": 0,
        "WARNING": 0,
        "OFFLINE": 0
    }
    
    for device in devices_dict.values():
        current_state = device["status"]
        if current_state in summary_data:
            summary_data[current_state] += 1
            
    return summary_data