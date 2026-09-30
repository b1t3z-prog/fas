from typing import Callable
import time
from fastapi import FastAPI, Request, Response
import uvicorn

app = FastAPI()

@app.middleware("http")
async def my_middlewear(request: Request, call_next: Callable):
    ip_address = request.client.host
    print(f'{ip_address=}')
    if ip_address in ["127.0.0.1", "localhost"]:
        return Response(status_code=429, content="Вы превысили кол-во запросов")
            
    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter() - start
    print(f'Время запроса: {end:.4f}')
    return response
    
    

@app.get("/user", tags=["Пользователи"])
async def get_users():
    time.sleep(0.5)
    return [{"id":1, "name":"Viktor"}]






if __name__ == "__main__":
    uvicorn.run("middlewear:app", reload = True)