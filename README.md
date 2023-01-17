## How to run locally
All images are uploaded on Docker Hub. Simply run
```
docker-compose up -d
```

---

## Technologies
- Backend: Spring Boot, Hibernate, H2 (for Spring Boot Testing)
- Frontend: Plain HTML and Javascript
- Database: Postgres

---

## Rest API Endpoints

- `GET localhost:8080/employee`
- `POST localhost:8080/employee`
    - `{ "firstName": "Sherjeel", "lastName": "Sikander", "departmentId": "1" }`
- `DELETE localhost:8080/employee`
- `GET localhost:8080/department`

---

