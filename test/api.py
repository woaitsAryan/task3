from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

dict1 = { "GDP" : "NY.GDP.MKTP.CD" ,
        "GDP per Capita PPP" : "NY.GNP.PCAP.PP.CD",
        "GDP Growth Rate" : "NY.GDP.MKTP.KD.ZG",
        "Inflation Rate" : "FP.CPI.TOTL.ZG",
        "Unemployment Rate" : "SL.UEM.TOTL.NE.ZS",
        "Fertility rate" : "SP.DYN.TFRT.IN",
        "CO2 Emissions per capita" : "EN.ATM.CO2E.PC",
        "Life expectancy" : "SP.DYN.LE00.IN"
        } # WorldBank official codes for respective datasets.


# Define a Pydantic model to represent the incoming data
class Item(BaseModel):
    name: str
    description: str
    price: float

# Define a route to handle the POST request
@app.post("/items/")
async def create_item(item: Item):
    # Process the incoming data
    item_dict = item.dict()
    # Return a response
    return {"item": item_dict}