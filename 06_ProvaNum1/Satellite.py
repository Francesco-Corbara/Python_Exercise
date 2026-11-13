from Sensor import Sensor


class Satellite:
    def __init__(self, name: str) -> None:
        self.name = name
        self.sensors: dict = {}
        self.readings: list = []

    def add_sensor(self, new_sensor: Sensor) -> None:
        if new_sensor.code in self.sensors:
            raise ValueError(f"Sensor code already exists: {new_sensor.code}")
        self.sensors[new_sensor.code] = new_sensor

    def record_reading(self, sensor_code: str, value: float) -> None:
        if sensor_code not in self.sensors:
            raise KeyError(f"Unregistered sensor: {sensor_code}")

        target_sensor = self.sensors[sensor_code]
        is_alarm = value > target_sensor.max_threshold

        entry = {
            "sensor": sensor_code,
            "metric": target_sensor.metric,
            "value": value,
            "unit": target_sensor.unit,
            "alarm": is_alarm,
        }
        self.readings.append(entry)

    def get_alarm_readings(self) -> list:
        alerts: list = []
        for item in self.readings:
            if item["alarm"]:
                alerts.append(item)
        return alerts

    def summary(self) -> None:
        print(f"Satellite telemetry: {self.name}")
        for item in self.readings:
            if item["alarm"]:
                status = "ALARM"
            else:
                status = "OK"
            print(f"- {item['sensor']}: {item['value']} {item['unit']} [{status}]")