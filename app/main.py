from fastapi import FastAPI, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.database.database import get_db, operations_collection
from app.models.database_models import Operation
from app.rpn_calculator.calculator import RPNCalculator
from app.models.request_models import CalculationRequest

app = FastAPI()
calculator = RPNCalculator()


@app.post("/calculate")
async def calculate(request: CalculationRequest, db:AsyncIOMotorClient =Depends(get_db)):
    try:
        expression = request.expression
        result = calculator.calculate(expression)
        operation = Operation(expression=expression, result=result)
        await operations_collection.insert_one(operation.__dict__)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/export")
async def export_calculations():
    pass