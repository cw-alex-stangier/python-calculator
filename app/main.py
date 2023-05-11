from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import math
from fastapi.responses import HTMLResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

app = FastAPI()

class PayloadSingle(BaseModel):
    operand: int

class Payload(BaseModel):
    operand1: int
    operand2: int

class PayloadList(BaseModel):
    items: list[int]

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(f"Request contains non valid types. Only integers can be consumed."), status_code=400)

@app.get("/")
async def default(response_class=HTMLResponse):
    #return {"available options": {"sum", "diff", "div", "prod", "sumList", "fac"}}
    htmlcontent = """
            <html>
                <head>
                    <title>Calcpy TEST</title>
                </head>
                <body>
                    <h1> Calculator </h1>
                    <h3> Options: </h3>
                    <ul> <li>POST</li>
                        <ul> 
                            <li>/sum -> sum up to 2 literals</li>
                            <li>/diff -> get the difference between two literals</li>
                            <li>/div -> divide literal 1 by literal 2</li>
                            <li>/prod -> get the product of two literals</li>
                            <li>/sumlist -> get the sum of a list of int literals</li>
                            <li>/fac -> calculate the factorial of a literal</li>
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