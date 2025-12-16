# ADAPT - Assisted Document Authoring Platform Tool

## 🔍 Overview

A full-stack, AI-powered web application that allows
authenticated users to generate, refine, and export structured business documents.

## ✨ Features

## 🛠️ Tech Stack

- [Next.js](https://nextjs.org/) - React framework for production
- [React.js](https://react.dev/) - Frontend Library
- [TypeScript](https://www.typescriptlang.org/) - Type-safe JavaScript
- [Shadcn-ui](https://ui.shadcn.com/) - UI components
- [TailwindCSS](https://tailwindcss.com/) - CSS Framework
- [NeonDB](https://neon.com/) - serverless PostgreSQL database platform
- [FastAPI](https://fastapi.tiangolo.com/) - web framework for building APIs with Python

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

#### Backend:

```bash
pip install fastapi uvicorn psycopg[binary] sqlmodel python-multipart passlib bcrypt==3.2.2 python-jose[cryptography]

```

>[!Important]
>Install only the mentioned versions!
>
>Passlib tries to run a self-test when it starts up to check for bugs, and it uses a long password for that test. The new bcrypt version strictly forbids long passwords, causing passlib to crash immediately.

#### Frontend:

```bash
cd frontend
npm install
```

### Step 4: Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file

```env
DEBUG = True
DATABASE_URL = 
SECRET_KEY =
ALGORITHM = can be HS256 , HS384 , etc.
ACCESS_TOKEN_EXPIRE_MINUTES = 
```

>[!Tip]
>To generate secret key you can use this command:
>
>```bash
>openssl rand --hex 32
>```

### Step 5: Run Development Servers

#### Backend server:

```bash
python3 -m uvicorn backend.main:app --reload
```

#### Frontend server:

```bash
cd frontend
npm run dev
```


## 🚀 Deployment
