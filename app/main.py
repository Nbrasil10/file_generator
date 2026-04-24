from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse

from utils import to_bytes
import generators as gen
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r") as f:
        return f.read()

@app.post("/generate")
def generate(
    size: int = Form(...),
    unit: str = Form(...),
    ftype: str = Form(...)
):
    total_bytes = to_bytes(size, unit)
    filename = f"output.{ftype}"

    if ftype == "txt":
        gen.generate_txt(filename, total_bytes)
    elif ftype == "csv":
        gen.generate_csv(filename, total_bytes)
    elif ftype == "pdf":
        gen.generate_pdf(filename, total_bytes)
    elif ftype == "docx":
        gen.generate_docx(filename, total_bytes)
    elif ftype == "xlsx":
        gen.generate_xlsx(filename, total_bytes)
    elif ftype == "bin":
        gen.generate_bin(filename, total_bytes)

    return FileResponse(filename, filename=filename)