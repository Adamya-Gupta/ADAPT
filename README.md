# ADAPT - Assisted Document Authoring Platform Tool

## 🔍 Overview

## ✨ Features

## 🛠️ Tech Stack

## ⚙️Installation & Setup

### Step 1: Clone the Repository

```bash
  git clone https://github.com/Adamya-Gupta/ADAPT
  cd ADAPT
```

### Step 2: Create and activate vitrual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies

```bash
pip install fastapi uvicorn psycopg[binary] sqlmodel
```


### Step 4: Environment Variables
To run this project, you will need to add the following environment variables to your `.env` file

```env
DEBUG = True
DATABASE_URL = 
```

### Step 5: Run Development Servers

```bash
#frontend server
npm run dev
```

```bash
#backend server
python3 -m uvicorn backend.main:app --reload
```

## 🚀 Deployment