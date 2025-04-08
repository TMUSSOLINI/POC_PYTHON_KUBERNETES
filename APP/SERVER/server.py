from fastapi import FastAPI, HTTPException


class Server:
    def __init__(self):
        self.app = FastAPI()
