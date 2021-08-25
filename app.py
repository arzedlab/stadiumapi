from fastapi import FastAPI
from models.stadium import Stadium
from models.database import Session
app = FastAPI()


session = Session()

@app.get("/api/{id}")
async def read_item(id):
    try:
        data = session.query(Stadium).filter_by(id=id).first()
        return {"id": data.id, "title": data.title, "price": data.price, "location": data.location}
    except AttributeError:
        return {"error": "ID not found"}
    
