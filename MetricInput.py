#  http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from Metric import Metric
from UnifiedDashboard import UnifiedDashboard
from PandasKPI import PandasKPI
from PlotBuilder import PlotBuilder
from DashboardConfig import DashboardConfig


app = FastAPI(title="Final Unified Dashboard API")

dashboard = UnifiedDashboard()
config = DashboardConfig()


class MetricInput(BaseModel):
    source: str
    metric: str
    value: float
    date: str


@app.post("/ingest")
def ingest_metric(item: MetricInput):
    if item.source not in config.sources:
        raise HTTPException(status_code=400, detail="Неизвестный source")

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
    csv_file = "kpi.csv"
    kpi.export_kpi_csv(csv_file)

    return FileResponse(
        path=csv_file,
        media_type="text/csv",
        filename="kpi.csv",
        content_disposition_type="attachment"
    )


@app.get("/plots")
def get_plots():
    plot_builder = PlotBuilder(dashboard)
    files = plot_builder.save_metric_plots()

    if not files:
        raise HTTPException(status_code=404, detail="Нет данных для графиков")

    plot_file = files[0]

    return FileResponse(
        path=plot_file,
        media_type="image/png",
        filename=plot_file,
        content_disposition_type="inline"
    )