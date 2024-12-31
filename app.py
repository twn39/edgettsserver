import io
import edge_tts
from fastapi import FastAPI,  Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {
        'title': 'Edge TTS Server API.',
        'version': '1.0',
    }


@app.get("/tts")
async def tts(text: str, voice: str = 'en-GB-SoniaNeural'):
    # Generate TTS
    communicate = edge_tts.Communicate(text, voice)

    audio_stream = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_stream.write(chunk["data"])
    audio_stream.seek(0)

    # Return audio response
    return Response(
        content=audio_stream.read(),
        media_type='audio/mpeg'
    )

