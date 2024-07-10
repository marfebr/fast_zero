from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, users

app = FastAPI()
app.include_router(auth.router)
app.include_router(users.router)


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', response_class=HTMLResponse)
def read_html():
    #  html_content = """
    #  <html>
    # <head>
    # <title> oi</title>
    # </head>
    # <body>
    # <h2>Olá Mundo</h2>
    # </body>
    # </html>
    # """
    html_content = 'Ola mundo'
    return html_content
