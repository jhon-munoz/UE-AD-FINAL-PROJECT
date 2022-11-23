from fastapi import FastAPI

matches = FastAPI(
    title='Poke-Fu-Mi Matches Service',
    version='0.1.0',
)


@matches.get('/')
async def root():
    return {'message': 'Hello World'}
