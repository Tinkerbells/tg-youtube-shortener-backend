## Setup and Running

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd tg-youtube-shortener-backend
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**

   ```bash
   python server.py
   ```

5. **Test the `/ping` endpoint:**
   Open your browser or use a tool like `curl` or `Postman` to access:
   ```
   http://127.0.0.1:5000/ping
   ```
   Expected response:
   ```json
   {
     "message": "pong"
   }
   ```
