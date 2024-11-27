# Setup and Running Guide for **tg-youtube-shortener-backend**

Follow these steps to set up and run the project:

---

## ! To use asyncio with flask install flask with [async]

```bash
pip install flask[async]
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
