from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from db import MyDb
from log_model import Log


class Server:
    def __init__(self) -> None:
        self.connected_to_db = False
        self.app = FastAPI()
        self.app.swagger_ui_parameters

    async def ensure_connection(self) -> None:
        if self.connected_to_db:
            return
        try:
            self.db = MyDb()
            self.connected_to_db = True
            print("database uploaded")
        except:
            print("Failed to connect the database")

    def shut_down(self) -> None:
        print("Closing database connection.")
        self.db.close()

    def run_server(self) -> None:
        @self.app.get("/")
        async def root():
            return {"message": "HELLO", "connected to db": self.connected_to_db}

        @self.app.get("/logs/{name}")
        async def get_log_by_name(name: str):
            await self.ensure_connection()
            exist, data = self.db.query(name)
            if exist:
                return HTMLResponse(data, 200)
            return HTMLResponse("key doesn't match", 400)

        @self.app.post("/add_log/")
        async def add_log(msg: Log):
            await self.ensure_connection()
            if self.db.create_log(msg):
                return HTMLResponse("INSERT SUCCEEDED", 200)
            return HTMLResponse("FAILED TO INSERT", 400)

        @app.on_event("startup")
        def startup():
            print("startup")

        @app.on_event("shutdown")
        def shutdown():
            self.shut_down()
            print("shutdown")


server = Server()
app = server.app
server.run_server()
