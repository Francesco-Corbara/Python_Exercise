from Sensor import Sensor
from Satellite import Satellite


def main() -> None:
    sat = Satellite("CubeSat Horizon")

    s1 = Sensor("TMP-01", "temperature", "C", 50.0)
    s2 = Sensor("BAT-01", "battery voltage", "V", 8.4)
    s3 = Sensor("GYR-01", "angular velocity", "deg/s", 15.0)

    sat.add_sensor(s1)
    sat.add_sensor(s2)
    sat.add_sensor(s3)

    sat.record_reading("TMP-01", 34.2)
    sat.record_reading("TMP-01", 50.0)
    sat.record_reading("BAT-01", 8.9)
    sat.record_reading("GYR-01", 6.5)

    sat.summary()
    print("\nAlarm readings:", sat.get_alarm_readings())

    try:
        sat.record_reading("GPS-99", 1.0)
    except KeyError as err:
        print("Error:", err)


if __name__ == "__main__":
    main()