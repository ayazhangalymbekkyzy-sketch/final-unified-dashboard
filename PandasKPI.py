import pandas as pd

class PandasKPI:
    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.df = pd.DataFrame()
        self.kpi_df = pd.DataFrame()

    def build_showcase(self):
        data = self.dashboard.get_all_as_dicts()
        self.df = pd.DataFrame(data)
        return self.df

    def group_kpi(self):
        self.kpi_df = self.df.groupby(["source", "metric"], as_index=False)["value"].sum()
        return self.kpi_df

    def export_kpi_csv(self, filename):
        self.kpi_df.to_csv(filename, index=False, encoding="utf-8")
        print("CSV файл сохранен:", filename)

    def show_showcase(self):
        print(self.df)

    def show_kpi(self):
        print(self.kpi_df)