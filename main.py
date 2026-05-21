from Metric import Metric
from UnifiedDashboard import UnifiedDashboard
from PandasKPI import PandasKPI
from PlotBuilder import PlotBuilder
from DashboardConfig import DashboardConfig

def main():
    dashboard = UnifiedDashboard()
    config = DashboardConfig()

    m1 = Metric("google_analytics", "sessions", 1523, "2026-05-17")
    m2 = Metric("google_analytics", "sessions", 1000, "2026-05-18")
    m3 = Metric("ads", "clicks", 320, "2026-05-17")
    m4 = Metric("ads", "clicks", 180, "2026-05-18")
    m5 = Metric("crm", "revenue", 12000, "2026-05-17")

    dashboard.add_metric(m1)
    dashboard.add_metric(m2)
    dashboard.add_metric(m3)
    dashboard.add_metric(m4)
    dashboard.add_metric(m5)

    print("=== Все метрики ===")
    dashboard.show_all_metrics()

    print("\n=== Источники ===")
    config.show_sources()

    print("\n=== Экспорт JSON ===")
    config.export_to_json(dashboard, "dashboard_data.json")

    print("\n=== KPI Pandas ===")
    kpi = PandasKPI(dashboard)
    kpi.build_showcase()
    kpi.group_kpi()
    kpi.show_kpi()
    kpi.export_kpi_csv("kpi.csv")

    print("\n=== Графики ===")
    plot_builder = PlotBuilder(dashboard)
    files = plot_builder.save_metric_plots()
    print(files)


if __name__ == "__main__":
    main()