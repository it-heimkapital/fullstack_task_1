package com.heimkapital.backend.service;

import com.heimkapital.backend.dto.EmployeeDTO;
import com.heimkapital.backend.model.Employee;
import com.heimkapital.backend.repository.EmployeeRepository;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class EmployeeService {

    private final EmployeeRepository repository;
    private final DepartmentService departmentService;

    public EmployeeService(EmployeeRepository repository, DepartmentService departmentService) {
        this.repository = repository;
        this.departmentService = departmentService;
    }

    public void addEmployee(EmployeeDTO employeeDTO) {
        Employee employee = new Employee();
        employee.setFirstName(employeeDTO.firstName());
        employee.setLastName(employeeDTO.lastName());
        employee.setDepartment(departmentService.getReference(employeeDTO.departmentId()));
        repository.save(employee);
    }

    public List<Employee> getEmployees() {
        List<Employee> employees = new ArrayList<>();
        repository.findAll().forEach(employees::add);
        return employees;
    }

    public void deleteEmployee(Long id) {
        repository.deleteById(id);
    }
}
