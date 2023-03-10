from fastapi import FastAPI
from pydantic import BaseModel
import wbdata
import country_converter as coco

app = FastAPI()

dictcode = { "GDP" : "NY.GDP.MKTP.CD" ,
        "GDP per Capita PPP" : "NY.GNP.PCAP.PP.CD",
        "GDP Growth Rate" : "NY.GDP.MKTP.KD.ZG",
        "Inflation Rate" : "FP.CPI.TOTL.ZG",
        "Unemployment Rate" : "SL.UEM.TOTL.NE.ZS",
        "Fertility rate" : "SP.DYN.TFRT.IN",
        "CO2 Emissions per capita" : "EN.ATM.CO2E.PC",
        "Life expectancy" : "SP.DYN.LE00.IN"
        } # WorldBank official codes for respective datasets.


class Data(BaseModel):
    indicator: str
    countries: list


@app.post("/process")
async def process(data: Data):
    
    inputdata = data.dict()
    
    countries = inputdata["countries"]
    indicator = inputdata["indicator"]
    
    iso_countries = coco.convert(names=countries, to = "ISO3")
    
    indicator_code = dictcode[indicator]
    
    valuelist = []
    for iso_country in iso_countries:
        value = wbdata.get_data(indicator_code, country=iso_country)[3]['value']
        indicator = wbdata.get_data(indicator_code, country=iso_country)[3]['indicator']['value']
        valuelist.append(round(value,1))

    return {"data":valuelist, "indicator":indicator}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)