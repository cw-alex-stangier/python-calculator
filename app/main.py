from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import math
from fastapi.responses import HTMLResponse

app = FastAPI()

class PayloadSingle(BaseModel):
    operand: int

class Payload(BaseModel):
    operand1: int
    operand2: int

class PayloadList(BaseModel):
    items: list[int]

@app.get("/")
async def default(response_class=HTMLResponse):
    #return {"available options": {"sum", "diff", "div", "prod", "sumList", "fac"}}
    htmlcontent = """
            <html>
                <head>
                    <title>Calcpy</title>
                </head>
                <body>
                    <h1> Calculator </h1>
                    <h3> Options: </h3>
                    <ul> <li>POST</li>
                        <ul> 
                            <li>/sum</li>
                            <li>/diff</li>
                            <li>/div</li>
                            <li>/prod</li>
                            <li>/sumlist</li>
                            <li>/fac</li>
                        </ul>
                    </ul>
                </body>
            </html>
    """
    return HTMLResponse(content=htmlcontent, status_code=200)

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