from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path

app = FastAPI()

UPLOAD_DIR = "uploaded_files"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

@app.post("/files/{name}")
async def upload_file(name: str, file: UploadFile = File(...)):
    file_path = Path(UPLOAD_DIR) / name
    if file_path.exists():
        raise HTTPException(status_code=400, detail="File already exists")
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return JSONResponse(status_code=201, content={"detail": "File uploaded successfully"})

@app.delete("/files/{name}")
async def delete_file(name: str):
    file_path = Path(UPLOAD_DIR) / name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    file_path.unlink()
    return JSONResponse(status_code=200, content={"detail": "File deleted successfully"})

@app.get("/files")
async def list_files():
    files = [f.name for f in Path(UPLOAD_DIR).glob("*") if f.is_file()]
    return files
