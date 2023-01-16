package com.heimkapital.backend.service;

import com.heimkapital.backend.model.Department;
import com.heimkapital.backend.repository.DepartmentRepository;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class DepartmentService {
    private final DepartmentRepository repository;

    public DepartmentService(DepartmentRepository repository) {
        this.repository = repository;
    }

    public Department getReference(Long id) {
        return repository.getReferenceById(id);
    }

    public List<Department> getDepartments() {
        List<Department> departments = new ArrayList<>();
        repository.findAll().forEach(departments::add);
        return departments;
    }
}
