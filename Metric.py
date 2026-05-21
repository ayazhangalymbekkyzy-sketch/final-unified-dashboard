from datetime import datetime

class Metric:
    def __init__(self, source, metric, value, date):
        if not isinstance(source, str) or source.strip() == "":
            raise ValueError("source должен быть непустой строкой")

        if not isinstance(metric, str) or metric.strip() == "":
            raise ValueError("metric должен быть непустой строкой")

        try:
            self.value = float(value)
        except:
            raise ValueError("value должен быть числом")

        if not isinstance(date, str) or date.strip() == "":
            raise ValueError("date должна быть непустой строкой")

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("date должна быть в формате YYYY-MM-DD")

        self.source = source
        self.metric = metric
        self.date = date

    def to_dict(self):
        return {
            "source": self.source,
            "metric": self.metric,
            "value": self.value,
            "date": self.date
        }

    def show(self):
        print("source =", self.source)
        print("metric =", self.metric)
        print("value =", self.value)
        print("date =", self.date)
        print()
