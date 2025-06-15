from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Instagram Webhook Backend",
    description="FastAPI backend for handling Instagram webhook verification and payload processing",
    version="1.0.0"
)

# Get verify token from environment variable
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "truthscope123")
print("VERIFY_TOKEN from env:", VERIFY_TOKEN)


@app.get("/")
def root():
    """Root endpoint for health checks"""
    return {
        "message": "Instagram Webhook Backend is running!",
        "status": "healthy",
        "endpoints": {
            "webhook_get": "/webhook (GET) - Webhook verification",
            "webhook_post": "/webhook (POST) - Receive webhook payloads"
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint for Render"""
    return {"status": "healthy", "service": "instagram-webhook-backend"}

@app.get("/webhook")
def verify_webhook(request: Request):
    """Handle GET requests for webhook verification from Meta"""
    # Meta sends ?hub.mode, ?hub.challenge, and ?hub.verify_token
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    print(f"🔍 Webhook verification attempt:")
    print(f"   Mode: {mode}")
    print(f"   Token received: {token}")
    print(f"   Expected token: {VERIFY_TOKEN}")
    print(f"   Challenge: {challenge}")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("✅ Webhook verified successfully!")
        return PlainTextResponse(content=challenge, status_code=200)
    else:
        print("❌ Webhook verification failed")
        return PlainTextResponse(content="Verification failed", status_code=403)

@app.post("/webhook")
async def receive_webhook(request: Request):
    """Handle POST requests with Instagram webhook payloads"""
    try:
        body = await request.json()
        print("📩 Received webhook payload:")
        print(json.dumps(body, indent=2))

        # TODO: Add your Instagram webhook processing logic here
        # For now, just log the payload

        return {"status": "received", "message": "Webhook processed successfully"}
    except Exception as e:
        print(f"❌ Error processing webhook: {str(e)}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
