import asyncio
import discord
import uvicorn
import requests as req
from fastapi import FastAPI
from dotenv import dotenv_values

app = FastAPI()
ENV = dotenv_values()
bebot = discord.Client()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(bebot.start(ENV['TOKEN']))

@bebot.event
async def on_ready():
    print('HELLO WORLD!')
    print(req.get('https://w3schools.com'))

@app.get("/")
async def read_root():
    return {"Hello": str(bebot.user)}

def bootstrap():
    uvicorn.run('bebot.app:app', host='0.0.0.0', port=5555, reload=True)