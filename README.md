# fullstack_task_1
## An app for creating employees
## Technology Stack:

---

• FastAPI \
• SQLAlchemy \
• Uvicorn (server) \
• Pytest \
• Postgres 


## How to start the app ?

---
``` git clone git@github.com:tesar27/fullstack_task_1.git 
  cd fullstack_task_1 
  python -m venv venv #create a virtual environment
  source venv/bin/activate #activate your virtual environment
  pip install -r .requirements.txt
  create .env file in the root with the following data
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=yourpassword
  POSTGRES_SERVER=localhost
  POSTGRES_PORT=5432
  POSTGRES_DB=heimkapital
  uvicorn main:app --reload #start server
  visit  127.0.0.1:8000
 ```






