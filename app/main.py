from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse

from app.csv_writer.csv_exporter import CSVExporter
from app.database.database import db_client
from app.models.database_models import Operation
from app.rpn_calculator.calculator import RPNCalculator
from app.models.request_models import CalculationRequest

app = FastAPI()
calculator = RPNCalculator()


@app.post("/calculate")
async def calculate(request: CalculationRequest, db=Depends(db_client.get_operations_collection)):
    try:
        expression = request.expression
        result = calculator.calculate(expression)
        operation = Operation(expression=expression, result=result)
        await db_client.insert_operation(operation)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/export")
async def export_csv(db=Depends(db_client.get_operations_collection)):
    try:
        operations = await CSVExporter.fetch_all_operations(db_client)
        file_path = "/tmp/operations.csv"
        CSVExporter.export_operations_to_csv(operations, file_path)
        return FileResponse(file_path, media_type='text/csv', filename="operations.csv")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to export CSV")