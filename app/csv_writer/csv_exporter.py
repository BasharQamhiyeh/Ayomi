import csv
from typing import List
from app.models.database_models import Operation

class CSVExporter:
    @staticmethod
    def export_operations_to_csv(operations: List[Operation], file_path: str):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Expression", "Result"])
            for op in operations:
                writer.writerow([op.expression, op.result])

    @staticmethod
    async def fetch_all_operations(db_client):
        operations = await db_client.operations_collection.find().to_list()  # Fetch first 100 operations
        return [Operation(**op) for op in operations]
