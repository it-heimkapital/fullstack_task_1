# fullstack_task_1

# Heimkapital backend

## Run on local:
  Change .env.sample to .env before doing the setup:

   1. Install the requirement using `poetry install` .
   2. Create initial department `python3 -m utils.create_department` from `server` directory.
   3. Run the uvicorn server: `uvicorn app.api:app --host '0.0.0.0' --port 8005`
   4. Run the tests: `python3 -m pytest`. Note: create test database `test_db` for testing.

## Run on Docker:
 `docker-compose up --build`

## Swagger UI:
`localhost:8005/docs` : Swagger UI with interactive exploration, call and test your API directly from the browser

Backend application will be available on `localhost:8005`. 
Note: Check if port `8005` is free on your machine. Make it free if it's in use.

# Heimkapital Front-end
