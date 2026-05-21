from Metric import Metric

class UnifiedDashboard:
    def __init__(self):
        self.metrics = []

    def add_metric(self, metric):
        if not isinstance(metric, Metric):
            raise ValueError("Можно добавлять только объекты Metric")
        self.metrics.append(metric)

    def get_all_metrics(self):
        return self.metrics

    def show_all_metrics(self):
        for metric in self.metrics:
            metric.show()

    def get_all_as_dicts(self):
        result = []
        for metric in self.metrics:
            result.append(metric.to_dict())
        return result