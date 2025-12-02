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

#### Frontend server:
```bash
cd frontend
npm run dev
```

#### Backend server:
```bash
python3 -m uvicorn backend.main:app --reload
```

## 🚀 Deployment