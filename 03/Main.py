from devices import DEVICES, update_status
from report import filter_by_bus, filter_by_status
from summary import create_summary


def main() -> None:
    print("Device Register:")
    for key, val in DEVICES.items():
        print(f"- {key}: {val['name']} | {val['bus']} | {val['status']}")
    
    print("\nOffline devices:")
    print(filter_by_status(DEVICES, "offline"))
    
    print("\nDevices connected to BUS-A:")
    print(filter_by_bus(DEVICES, "BUS-A"))
    
    print("\nStatus summary:")
    print(create_summary(DEVICES))
    
    update_status("NAV-01", "warning")
    
    print("\nStatus summary after NAV-01 update:")
    print(create_summary(DEVICES))


if __name__ == "__main__":
    main()