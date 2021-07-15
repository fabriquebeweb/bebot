import os
import json
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/cc/{id}')
def getCodecademyProfile(id: str):
    os.system(f'rm -f scrap/cc.json && scrapy parse https://www.codecademy.com/profiles/{id} --spider=codecademy -o scrap/cc.json:json')
    return json.loads(open('scrap/cc.json').read())[0]

@app.get('/sl/{id}')
def getSololearnProfile(id: str):
    os.system(f'rm -f scrap/sl.json && scrapy parse https://www.sololearn.com/profile/{id} --spider=sololearn -o scrap/sl.json:json')
    return json.loads(open('scrap/sl.json').read())[0]

def bootstrap():
    uvicorn.run('api.server:app', host='0.0.0.0', port=8000, reload=True)