import os
import json
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/cc/{id}')
def getCodecademyProfile(id: str):
    return os.popen(f"scrapy parse https://www.sololearn.com/profile/{id} --spider=sololearn --nolog | grep '[{{.*}}]'").read()
    

@app.get('/sl/{id}')
def getSololearnProfile(id: str):
    os.system(f'rm -f scrap/sl.json && scrapy parse https://www.sololearn.com/profile/{id} --spider=sololearn -o scrap/sl.json:json')
    return json.loads(open('scrap/sl.json').read())[0]

def bootstrap():
    uvicorn.run('api.server:app', host='0.0.0.0', port=5000, reload=True)