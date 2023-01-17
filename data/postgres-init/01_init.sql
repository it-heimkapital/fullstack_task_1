CREATE TABLE department (
	id serial PRIMARY KEY,
	name VARCHAR (20) NOT NULL
);

CREATE TABLE employee (
	id serial PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	department_id INT NOT NULL,
	CONSTRAINT fk_department_id
      FOREIGN KEY(department_id) 
	  REFERENCES department(id)
);

INSERT INTO department (name) VALUES('Sales'), ('Ops'), ('IT');