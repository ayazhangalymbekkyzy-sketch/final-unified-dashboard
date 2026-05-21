import matplotlib.pyplot as plt
from PandasKPI import PandasKPI

class PlotBuilder:
    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.kpi = PandasKPI(dashboard)

    def build_kpi_data(self):
        self.kpi.build_showcase()
        self.kpi.group_kpi()

    def save_metric_plots(self):
        self.build_kpi_data()

        if self.kpi.kpi_df.empty:
            print("Нет данных для графиков")
            return []

        filenames = []

        for metric_name in self.kpi.kpi_df["metric"].unique():
            metric_data = self.kpi.kpi_df[self.kpi.kpi_df["metric"] == metric_name]

            plt.figure(figsize=(8, 5))
            plt.bar(metric_data["source"], metric_data["value"])
            plt.title(f"KPI for {metric_name}")
            plt.xlabel("Source")
            plt.ylabel("Value")

            filename = f"{metric_name}.png"
            plt.savefig(filename)
            plt.close()

            filenames.append(filename)

        return filenames

    def show_plot_files(self):
        files = self.save_metric_plots()
        for file in files:
            print(file)