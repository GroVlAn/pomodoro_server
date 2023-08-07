import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from auth.base_config import auth_backend, fastapi_users, current_user
from auth.shemas import UserRead, UserCreate

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

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=f'{global_prefix}/auth/jwt',
    tags=['auth'],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=f'{global_prefix}/auth',
    tags=['auth'],
)


@app.get(global_prefix)
async def hello_app():
    return 'Welcome to pomodoro fast api'


if __name__ == '__main__':
    uvicorn.run(app="main:app", host='localhost', port=8001, reload=True)
