-- For testing only. H2 Database
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

INSERT INTO department (id, name) VALUES(1, 'Sales'), (2, 'Ops'), (3, 'IT');
INSERT INTO employee (id, first_name, last_name, department_id) VALUES(1, 'Sherjeel', 'Sikander', 3);
INSERT INTO employee (id, first_name, last_name, department_id) VALUES(2, 'Heim', 'Kapital', 2);