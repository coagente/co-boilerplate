from fastapi import FastAPI

# Create a FastAPI app instance
app = FastAPI()

# Define a "Hello World" endpoint
@app.get("/")
async def read_root():
    """
    Root endpoint that returns a simple greeting.
    """
    return {"message": "Hello World"}

# Optional: Add more endpoints as needed
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Example endpoint that returns an item based on its ID.
    """
    return {"item_id": item_id}

if __name__ == "__main__":
    # This block is used when running the app directly (for development)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
