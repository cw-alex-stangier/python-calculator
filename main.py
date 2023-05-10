from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payload(BaseModel):
    operand1: int
    operand2: int

#Sum function 
@app.post("/sum")
async def sum(operands: Payload):
    return {"result": operands.operand1 + operands.operand2}

#difference function
@app.post("/diff")
async def diff(operands: Payload):
    return {"result": operands.operand1 - operands.operand2}

#division function
@app.post("/div")
async def div(operands: Payload):
    return {"result": (operands.operand1 / operands.operand2)}

#product function
@app.post("/prod")
async def prod(operands: Payload):
    return {"result": operands.operand1 * operands.operand2}
