class Sensor:
    def __init__(self, code: str, metric: str, unit: str, max_threshold: float) -> None:
        self.code = code
        self.metric = metric
        self.unit = unit
        self.max_threshold = max_threshold