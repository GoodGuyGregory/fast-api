from fastapi import FastAPI

# create an instance of FastAPI
app = FastAPI()

@app.get("/add")
async def add_numbers(num1: float, num2: float):
    result = num1 + num2
    return { "result": result}

