# Setup and Running Guide for **tg-youtube-shortener-backend**

Follow these steps to set up and run the project:

---

## ! To use asyncio with flask install flask with [async]

```bash
pip install flask[async]
```

## Cookies

Some videos are age restricted, so this module won't be able to access those videos without some sort of authentication. To do this, you will need to have access to the desired video in a browser. Then, you will need to download that pages cookies into a text file. You can use the Chrome extension [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en) and select "Netscape" during export, or the Firefox extension [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/).

Once you have that, you can use it with the module to access age-restricted videos' captions like so.

```python
from youtube_transcript_api import YouTubeTranscriptApi

YouTubeTranscriptApi.get_transcript(video_id, cookies='/path/to/your/cookies.txt')

YouTubeTranscriptApi.get_transcripts([video_id], cookies='/path/to/your/cookies.txt')
```

## 1. **Clone the Repository**

First, clone the repository and navigate into the project directory:

```bash
git clone <repository_url>
cd tg-youtube-shortener-backend
```

---

## 2. **Create and Activate a Virtual Environment** (Optional but Recommended)

Creating a virtual environment ensures that dependencies are isolated for the project. Use one of the methods below based on your operating system:

### On Unix/Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:

You have multiple options to activate the virtual environment:

#### Using `python3`:

```bash
python3 -m venv venv
venv\Scripts\activate
```

#### Using `py`:

```bash
py -m venv venv
venv\Scripts\activate
```

#### Using `python`:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. **Install Dependencies**

Once inside the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 4. **Run the Server**

Start the server using the appropriate command for your operating system:

### On Windows:

```bash
python .\server.py
```

### On Unix/Linux/macOS:

```bash
python server.py
```

---

## 5. **Test the Server**

To test the server, follow these steps:

1. Open a new terminal.
2. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```
3. Run the test script:
   ```bash
   python .\test_server_with_terminal_input.py
   ```

---
