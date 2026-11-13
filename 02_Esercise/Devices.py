Devices = {
    "NAV-01": {"name": "Navigation receiver", "bus": "BUS-A", "status": "OK"},
    "COM-02": {"name": "Communication radio", "bus": "BUS-B", "status": "WARNING"},
    "SEN-03": {"name": "Attitude sensor", "bus": "BUS-A", "status": "OFFLINE"},
}

AllowedStates = ["OK", "WARNING", "OFFLINE"]


def add_device(code: str, name: str, bus: str, status: str) -> bool:
    norm_state = status.upper()
    
    if code in Devices:
        return False
        
    if norm_state not in AllowedStates:
        return False

    Devices[code] = {"name": name, "bus": bus, "status": norm_state}
    return True


def update_status(code: str, status: str) -> bool:
    norm_state = status.upper()
    
    if code not in Devices:
        return False
        
    if norm_state not in AllowedStates:
        return False

    Devices[code]["status"] = norm_state
    return True