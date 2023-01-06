import React, { useEffect, useState } from 'react';
import {useNavigate} from "react-router-dom";
import axios from "axios";
import { Form, Button } from 'react-bootstrap';

const EmployeeForm = () => {
  const baseURL = "http://localhost:8005/api/create_employee/";
  const navigate = useNavigate();
  const [enteredFirstName, setFirstName] = useState('');
  const [enteredLastName, setLastName] = useState('');
  const [enteredDepartment, setDepartment] = useState('');

  const [departments, setDepartments] = useState([]);

  const setDepartmentsData = () => {
    axios.get("http://localhost:8005/api/get_departments").then((response) => {
      setDepartments(response.data.departments);
    }).catch(error => {
      alert("Error Ocurred while loading data:" + error);
    });
  }

  useEffect(() => {
    setDepartmentsData();
  }, []);

  const firstnameChangeHandler = (event) => {
    setFirstName(event.target.value);
  };

  const lastnameChangeHandler = (event) => {
    setLastName(event.target.value);
  };

  const departmentChangeHandler = (event) => {
    setDepartment(event.target.value);
  };


  const submitActionHandler = (event) => {
    event.preventDefault();
    axios
      .post(baseURL, {
        first_name: enteredFirstName,
        last_name: enteredLastName,
        department_id: enteredDepartment
      })
      .then((response) => {
        alert(response.data.msg.toString());
        navigate("/");
      }).catch(error => { 
        alert("error==="+error);
      });
    
  };

    return(
        <div className="col-md-12 add-emp">
            <div className="container">
                <div className="row">
                    <div className="col-6">
                        <Form onSubmit={submitActionHandler}>
                            <Form.Group controlId="form.first_name">
                                <Form.Control type="text" value={enteredFirstName} onChange={firstnameChangeHandler} placeholder=" Enter First Name *" required/>
                            </Form.Group>
                            <br></br>
                        <Form.Group controlId="form.last_name">
                            <Form.Control type="text" value={enteredLastName} onChange={lastnameChangeHandler} placeholder="Enter Last Name *" required/>
                        </Form.Group>
                            <br></br>

                        <Form.Select onChange={departmentChangeHandler}>
                            <option >Enter Department *</option>
                             {
                                departments &&
                                departments.map((department, index) => (
                                <option value={department.id} onChange={departmentChangeHandler} >{department.name}</option>
                                ))
                             }
                        </Form.Select>
                        <br></br>
                        <Button type='submit'>Add Employee</Button>
                        </Form>
                    </div>
                </div>
            </div>
        </div>
    );
}
export default EmployeeForm;