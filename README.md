# Instagram Webhook Backend

FastAPI backend for handling Instagram webhook verification and payload processing.

## Features

- ✅ GET `/webhook` - Returns hub.challenge for webhook verification
- ✅ POST `/webhook` - Logs Instagram webhook payloads
- ✅ Render deployment ready
- ✅ Environment variable support
- ✅ Health check endpoints
- ✅ Auto-scaling and free tier support

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file:
```bash
VERIFY_TOKEN=your_instagram_verify_token_here
```

3. Run locally:
```bash
python main.py
# or
python -m uvicorn main:app --reload
```

4. Test the endpoints:
- Health check: `http://localhost:8000/health`
- Root: `http://localhost:8000/`
- Webhook: `http://localhost:8000/webhook`

## Render Deployment

### Option 1: Deploy from GitHub (Recommended)

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: `instagram-webhook-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add environment variable:
   - **Key**: `VERIFY_TOKEN`
   - **Value**: `IGAAYtHUexPntBZAE5IMlliVUhGODZApcGYzT0tCaWpJbUZABTDE0Y1lmaWp2SWRnX1hjc1lSY2ZA2U1FxMjdlRGRfcmthc3VqRi1oemhYSzBUcDJQZAFdqSlFoV2JrYXFDZAUM0eXUwRS03MldNZADdETUJpX3dVNlBxRFNRTGpUUmZAUQQZDZD`
7. Click "Create Web Service"

### Option 2: Deploy with render.yaml

1. The included `render.yaml` file will automatically configure your deployment
2. Just connect your repository and Render will use the configuration

### Your Deployment URL

After deployment, you'll get a URL like: `https://instagram-webhook-backend-xxxx.onrender.com`

## Meta App Configuration

Use your Render URL as the callback URL in your Meta app settings:
- **Webhook URL**: `https://your-app-name.onrender.com/webhook`
- **Verify Token**: `IGAAYtHUexPntBZAE5IMlliVUhGODZApcGYzT0tCaWpJbUZABTDE0Y1lmaWp2SWRnX1hjc1lSY2ZA2U1FxMjdlRGRfcmthc3VqRi1oemhYSzBUcDJQZAFdqSlFoV2JrYXFDZAUM0eXUwRS03MldNZADdETUJpX3dVNlBxRFNRTGpUUmZAUQQZDZD`

## Endpoints

- `GET /` - Service information and health status
- `GET /health` - Health check for monitoring
- `GET /webhook` - Instagram webhook verification
- `POST /webhook` - Receive Instagram webhook payloads

## Benefits of Render

- ✅ **Free tier available** - Perfect for development and testing
- ✅ **Auto-scaling** - Handles traffic spikes automatically
- ✅ **Persistent URLs** - Your webhook URL won't change
- ✅ **Built-in SSL** - HTTPS by default
- ✅ **Easy deployment** - Direct GitHub integration
- ✅ **Environment variables** - Secure configuration management