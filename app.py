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


# Bhaiii! 🎉🔥

# Ho gaya!

# Ye sabse important line hai:

# Application startup complete.

# Matlab:

# ✅ FastAPI server chal raha hai.

# ✅ Uvicorn sahi chal raha hai.

# ✅ Koi error nahi hai.

# Ab test karo

# Browser me ye kholo:

# http://127.0.0.1:8000/docs

# Agar FastAPI ka Swagger UI khul gaya, to sab perfect hai.

# Aur ek baat 😄

# Yaad hai uvicorn.py wali problem?

# Ye ek classic Python mistake hai. Aaj se yaad rakhna:

# ❌ Kabhi bhi file ka naam library ke naam par mat rakhna.

# Jaise:

# requests.py
# fastapi.py
# uvicorn.py
# google.py

# Ye sab problems create karte hain.

# Agla step

# Ab hum 
# isi FastAPI app ko GitHub par push karenge, phir 
# Railway par deploy karenge, aur uske baad 
# Meta Webhook connect karenge.

# Ab asli chatbot banana shuru hoga. 🚀





# 😂 Bhai meri galti. Main assume kar gaya tha ki tumhe pata hoga.

# Ye /docs kya hai?

# FastAPI apne aap ek testing website banata hai.

# Matlab tumhare code ko test karne ke liye ek webpage.

# Iska naam hai:

# Swagger UI

# Tumhe ye yaad rakhne ki zarurat nahi hai.

# Kya karna hai?
# Chrome ya Brave browser kholo.
# Upar address bar me ye likho:
# http://127.0.0.1:8000/docs
# Enter dabao.
# Agar sab sahi hai to ek webpage khulega.

# Usme likha hoga:

# FastAPI

# Aur niche:

# GET /webhook
# POST /webhook

# dikhai dega.

# 👉 Bas us page ka screenshot bhej dena.

# Ye sirf check karne ke liye hai ki tumhara FastAPI server sahi chal raha hai. Phir hum Railway par deploy karenge. 🚀