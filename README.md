# DevTrack-Developer-Productivity-Project-Tracker


DevTrack is a full-stack web application that helps developers manage projects, track tasks, and monitor productivity.

Built with:

- React (Vite)
- Node.js
- Express
- MongoDB
- JWT Authentication
- Chart.js
- TailwindCSS

---

## 📂 Project Structure


---

## 🔐 Features

- Add, list, and remove tasks
- Task lifecycle management (`todo → doing → done`)
- User Authentication (JWT)
- Protected Routes
- Project Management
- Task Tracking
- Dashboard Analytics
- REST API Architecture
- Log development activities during the day
- View a daily work summary

---

##  Installation

### 1️⃣ Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/devtrack.git
cd devtrack
```

### 2️⃣ Backend Setup
```bash
cd server
npm install
```

Create .env file:
```bash
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
```

Run backend:
```bash
npm start
```

### 3️⃣ Frontend Setup
```bash
cd client
npm install
npm run dev
```

## Task Workflow

DevTrack now supports a simple task lifecycle to help you track your development progress.

### Create a task

```bash
devtrack add "Implement authentication endpoint"
```

### Start working on a task

```bash
devtrack start 1
```

Task status changes to:

```bash
doing
```

### Complete a task

```bash
devtrack done 1
```

Task status changes to:

```bash
done
```

### Tag a task

```bash
devtrack tag 1 backend
```

Tags help organize and filter tasks.



## Work Logging

DevTrack allows you to log development activities throughout the day.

This helps track what you actually worked on without leaving the terminal.

### Log work

```bash
devtrack log 1 "Implemented JWT authentication"
