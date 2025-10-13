from fastapi import FastAPI

app = FastAPI()

def say_hello():
    return 'hello'

@app.get('/')
async def read_results():
    results = await say_hello()
    return results



async def get_burgers(number: int):
    return [number]

@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers


