import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Pomodoro API'
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

_version = '0.0.1'
_name_app = 'pomodoro'

global_prefix = f'/{_name_app}/api/v{_version}/'


@app.get(global_prefix)
async def hello_app():
    return 'Welcome to pomodoro fast api'


if __name__ == '__main__':
    uvicorn.run(app="main:app", host='localhost', port=8001, reload=True)
