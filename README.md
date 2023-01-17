## How to run locally
All images are uploaded on Docker Hub. Simply run
```
docker-compose up -d
```
and access `http://localhost/`

## Technologies
- Backend: Spring Boot, Hibernate, H2 (for Spring Boot Testing)
- Frontend: Plain HTML and Javascript
- Database: Postgres

## Rest API Endpoints

- `GET localhost:8080/employee`
- `POST localhost:8080/employee`
    - `{ "firstName": "Sherjeel", "lastName": "Sikander", "departmentId": "1" }`
- `DELETE localhost:8080/employee/{id}`
- `GET localhost:8080/department`

## Additional Information

- Postgres is running on `localhost:5432/heimkapital`
- Postgres image uses `data/postgres-init/01_init.sql` for initialization
- Backend server is running on `localhost:8080`
- Frontend server is running on `localhost:80`
- Passwords are stored in plain text only for demo purposes. For production purposes use a vault e.g. HashiCorp Vault
- Query logging is not enabled

## Building images locally

Backend:
```
// Build maven project (e.g. without running tests)
mvn -f backend\backend\pom.xml package -Dmaven.test.skip

// Build image
docker build -f Dockerfile-backend -t sherjeelsikander/heimkapital:backend-v1 .
```

Frontend:
```
// Build image
docker build -f Dockerfile-frontend -t sherjeelsikander/heimkapital:frontend-v1 .
```
