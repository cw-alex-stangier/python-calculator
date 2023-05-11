from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import math

app = FastAPI()

class PayloadSingle(BaseModel):
    operand: int

class Payload(BaseModel):
    operand1: int
    operand2: int

class PayloadList(BaseModel):
    items: list[int]

@app.get("/")
async def default():
    return {"options": {"sum", "diff", "div", "prod", "sumList", "fac"}}

#Sum function 
@app.post("/sum")
async def sum(operands: Payload):
    return {"type": operands.operand1 + operands.operand2}

#sum up all items in list
@app.post("/sumList")
async def sum(operands: PayloadList):
    val = 0
    for x in operands.items:
        val += x
    return {"result": val}

#calc factorial
@app.post("/fac")
async def fac(operand: PayloadSingle):
    return {"result": math.factorial(operand.operand)}


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