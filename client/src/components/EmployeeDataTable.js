import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from "axios";
import "../App.css";


const EmployeeDataTable = () => {

  const navigate = useNavigate();
  const baseURL = "http://localhost:8005/api";
  const [employees, setEmployees] = useState([]);

  const setEmployeeData = () => {
    axios.get(baseURL + "/get_employees").then((response) => {
      setEmployees(response.data.employees);
    }).catch(error => {
      alert("Error Ocurred while loading data:" + error);
    });
  }

  useEffect(() => {
    setEmployeeData();
  }, []);


  return (
    <div className="card-body">
      <br>
      </br>
      <br></br>
      <div className="col-md-12">

        <div className="container">
          <div className="row">
            <div className="col-12">
              <h4>Employees</h4>
              <span> List View</span>
              <table className="table table-bordered table-striped">
                <thead>
                  <tr>
                    <th>Id</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Department</th>
                  </tr>
                </thead>
                <tbody>

                  {
                    employees &&
                    employees.map((employee, index) => (

                      <tr>
                        <th scope="row">{employee.id}</th>
                        <td>{employee.first_name}</td>
                        <td>{employee.last_name}</td>
                        <td>{employee.department.name}</td>
                      </tr>

                    ))
                  }
                </tbody>
              </table>
            </div>
          </div>
          <button className="btn btn-primary create-employee-btn"
                  onClick={() => navigate("/create")}>
                  Add Employee
          </button>
        </div>
      </div>

    </div>

  );
}
export default EmployeeDataTable;