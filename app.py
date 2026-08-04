from fastapi import FastAPI, Request

app = FastAPI()

VERIFY_TOKEN = "tushar123"

@app.get("/webhook")
async def verify(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)

    return {"error": "Verification Failed"}


@app.post("/webhook")
async def webhook(request: Request):

    body = await request.json()

    print(body)

    return {"status": "ok"}
