# 💊 Pillulu · Your Smart Medicine Assistant & Health Companion

Pillulu 是一款由 AI 驱动的智能药丸助手，帮助用户识别药物、了解用法，并通过智能提醒管

### 🔐 Environment Variables

To run Pillulu locally, you need to set up a `.env` file to securely store the API key used.  
This file will not be uploaded to GitHub (thanks to `.gitignore`), so your credentials remain private.

#### 🔧 Steps:

1. Create a file named `.env` in the project root file.
2. Add the following line to it (replace with your actual OpenAI API key):

   ```env
   OPENAI_API_KEY=your_openai_api_key_here

### 💁 Server

Pillulu is hosted on AWS servers, using a stack of Docker, Nginx, Gunicorn, Flask, GitHub, and Let’s Encrypt (HTTPS).

### 📝 Why "Pillulu":

- ~~The domain names "MedPal" and "Pillie" were already taken.~~
- "Pillulu" reminds me of a smart, friendly childhood novel character "Pi Pi Lu" written by famous author Zheng Yuanjie, and I thought it would be a cute and approachable name for users of all ages.