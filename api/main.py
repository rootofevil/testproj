from typing import Annotated
import rasterio
from fastapi import FastAPI, File, Body, Request
from fastapi.staticfiles import StaticFiles
from matplotlib import pyplot
import matplotlib
from  datetime import datetime
import os

app = FastAPI()
app.mount("/thumbnail/static", StaticFiles(directory="static"), name="static")

@app.post("/attributes")
def read_attr(file: Annotated[bytes, File()]):
    res = {}
    with rasterio.MemoryFile(file) as memfile:
        with memfile.open() as dataset:
            bounds = {}
            bounds['left'] = dataset.bounds.left
            bounds['bottom'] = dataset.bounds.bottom
            bounds['right'] = dataset.bounds.right
            bounds['top'] = dataset.bounds.top
            res['bounds'] = bounds
            res['width'] = dataset.width
            res['height'] = dataset.height
            res['count'] = dataset.count
            res['crs'] = str(dataset.crs)
    return res

@app.post("/thumbnail")
def thumbnail(file: Annotated[bytes, File()], request: Request, dpi: Annotated[int, Body(embed=True)] = None):
    if dpi is None:
        dpi = "figure"
    res = {}
    time = datetime.now()
    filename = os.path.join("static", time.strftime("%Y%m%d%H%M%s") + ".png")
    res['path'] = os.path.join(str(request.url), filename)
    with rasterio.MemoryFile(file) as memfile:
        with memfile.open() as dataset:
            matplotlib.use('agg')
            pyplot.imshow(dataset.read(1), cmap='pink')
            pyplot.savefig(filename, dpi=dpi)
    return res

