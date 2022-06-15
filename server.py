from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import RPi.GPIO as GPIO
from fastapi.staticfiles import StaticFiles

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 7

GPIO.setup(LED, GPIO.OUT)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/toggle")
async def main():
    state = GPIO.input(LED)
    if state:
        GPIO.output(LED, GPIO.LOW)
    else:
        GPIO.output(LED, GPIO.HIGH)
    return {"message": "OK"}

app.mount('/', StaticFiles(directory='static', html=True), name="static")