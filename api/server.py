import os
import json
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/cc/{id}')
def getCodecademyProfile(id: str):
    os.system(f'rm -f tmp/cc.json && scrapy parse https://www.codecademy.com/profiles/{id} --spider=codecademy -o tmp/cc.json:json')
    return json.loads(open('tmp/cc.json').read())[0]

@app.get('/sl/{id}')
def getSololearnProfile(id: str):
    os.system(f'rm -f tmp/sl.json && scrapy parse https://www.sololearn.com/profile/{id} --spider=sololearn -o tmp/sl.json:json')
    return json.loads(open('tmp/sl.json').read())[0]

def bootstrap():
    uvicorn.run('api.server:app', host='0.0.0.0', port=5901, reload=True)