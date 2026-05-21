from fastapi import FastAPI
from pydantic import BaseModel

from Metric import Metric
from UnifiedDashboard import UnifiedDashboard
from PandasKPI import PandasKPI
from PlotBuilder import PlotBuilder
from DashboardConfig import DashboardConfig


app = FastAPI()

dashboard = UnifiedDashboard()
config = DashboardConfig()


class MetricInput(BaseModel):
    source: str
    metric: str
    value: float
    date: str


@app.post("/ingest")
def ingest_metric(item: MetricInput):
    if item.source not in config.get_sources():
        return {"error": "Неизвестный source"}

    metric = Metric(item.source, item.metric, item.value, item.date)
    dashboard.add_metric(metric)

    return {
        "message": "Метрика добавлена",
        "metric": metric.to_dict()
    }


@app.get("/kpi")
def get_kpi():
    kpi = PandasKPI(dashboard)
    kpi.build_showcase()
    kpi.group_kpi()
    kpi.export_kpi_csv(config.csv_file)

    return {
        "kpi": kpi.kpi_df.to_dict(orient="records"),
        "csv_file": config.csv_file
    }


@app.get("/plots")
def get_plots():
    plot_builder = PlotBuilder(dashboard)
    files = plot_builder.save_metric_plots()

    for file in files:
        config.add_plot_file(file)

    return {
        "message": "Графики построены",
        "files": config.get_plot_files()
    }