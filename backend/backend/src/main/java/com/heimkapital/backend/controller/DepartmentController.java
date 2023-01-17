package com.heimkapital.backend.controller;

import com.heimkapital.backend.model.Department;
import com.heimkapital.backend.service.DepartmentService;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@CrossOrigin(origins = "http://localhost")
@RestController
public class DepartmentController {

    private final DepartmentService departmentService;

    public DepartmentController(DepartmentService departmentService) {
        this.departmentService = departmentService;
    }

    @GetMapping("/department")
    public List<Department> getDepartments() {
        return departmentService.getDepartments();
    }
}
