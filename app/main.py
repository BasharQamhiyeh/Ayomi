from fastapi import FastAPI, HTTPException

from app.rpn_calculator.calculator import RPNCalculator
from app.models.calculation_request import CalculationRequest

app = FastAPI()
calculator = RPNCalculator()


@app.post("/calculate")
async def calculate(request: CalculationRequest):
    try:
        result = calculator.calculate(request.expression)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/export")
async def export_calculations():
    pass