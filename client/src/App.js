import React from 'react';
import {Routes,Route,Navigate} from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import AddEmployee from './components/AddEmployee';
import EmployeeDataTable from './components/EmployeeDataTable';

function App() { 

  return (
   
    <div  class="container">
    
        <div>
            <h2 class="heading">HK Task</h2>
          </div>

    <Routes>
        <Route exact path="/create" element={<AddEmployee/>}/>
        <Route exact path="/" element={<EmployeeDataTable/>}/>
      </Routes>

    </div>
  );
}

export default App;
