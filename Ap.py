from fastapi import FastAPI

app = FastAPI()

all_items=[
    {"id":1,"laptop": "Dell","price":60000},
    {"id":2,"laptop": "HP","price":55000},
    {"id":3,"laptop": "Lenovo","price":50000},
    {"id":4,"laptop": "Apple","price":120000},


]

@app.get('/')
def index():
    return {"message":" Sayonara Anna  "}


@app.get('/items/{item_id}')
async def get_items(item_id:int):
    for item in  all_items:
        if item["id"] ==id:
            return item 
    return {"message": "Item not found"}
        
@app.get('/items/')
def get_all_items(first_n: int =None):
    if first_n:
        return all_items[:first_n]
    else:
      return all_items


