package com.heimkapital.backend.controller;

import com.heimkapital.backend.dto.EmployeeDTO;
import com.heimkapital.backend.model.Employee;
import com.heimkapital.backend.service.EmployeeService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class EmployeeController {

    private final EmployeeService employeeService;

    public EmployeeController(EmployeeService employeeService) {
        this.employeeService = employeeService;
    }

    @GetMapping("/employee")
    public List<Employee> getEmployees() {
        return employeeService.getEmployees();
    }

    @PostMapping("/employee")
    public EmployeeDTO addEmployee(@RequestBody EmployeeDTO employee) {
        employeeService.addEmployee(employee);
        return employee;
    }

    @DeleteMapping("/employee/{id}")
    public void deleteEmployee(@PathVariable("id") Long id) {
        employeeService.deleteEmployee(id);
    }

}
