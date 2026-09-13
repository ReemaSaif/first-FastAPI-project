# first-FastAPI-project


## A simple FastAPI project for learning how to build and run an API in Python.


## How to Run (Open Command Prompt in the Terminal):

### **1. Create a virtual environment**

```bash
 python -m venv .env 
```

### **2. Activate the virtual environment** 

**For Windows:**

```bash
.env\Scripts\activate
```

**For Linux / MacOS:**

```bash
source .env/bin/activate
```


### **3. Install the required packages**

```bash
pip install -r requirements.txt
```


### **4. Start the API** 

```bash
uvicorn app:app
```


**The API will start locally. You can open:**

```bash
http://127.0.0.1:8000
```

### **API Endpoints:**

- **GET /home** — Returns a welcome message.

  `http://127.0.0.1:8000/home`

- **GET /time** — Returns the current date and time.

  `http://127.0.0.1:8000/time`



### **You can also view the interactive API documentation at:**

  `http://127.0.0.1:8000/docs`


