def filter_by_status(devices_dict: dict, status: str) -> list:
    target_state = status.upper()
    return [device for device in devices_dict.values() if device.get("status") == target_state]


def filter_by_bus(devices_dict: dict, bus: str) -> list:
    return [device for device in devices_dict.values() if device.get("bus") == bus]