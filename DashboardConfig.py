import json
class DashboardConfig:
    def __init__(self):
        self.sources = {
            "google_analytics": {
                "name": "Google Analytics",
                "active": True
            },
            "ads": {
                "name": "Advertising Platform",
                "active": True
            },
            "crm": {
                "name": "CRM System",
                "active": True
            }
        }

    def show_sources(self):
        for key, value in self.sources.items():
            print(key, "->", value)

    def to_dict(self, dashboard):
        return {
            "sources": self.sources,
            "metrics": dashboard.get_all_as_dicts()
        }

    def export_to_json(self, dashboard, filename):
        data = self.to_dict(dashboard)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("JSON файл сохранен:", filename)