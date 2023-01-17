package com.heimkapital.backend.controller;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultHandlers;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

@SpringBootTest
@AutoConfigureMockMvc
class DepartmentControllerTest {

    private final String initialDepartments = "[{\"id\":1,\"name\":\"Sales\"},{\"id\":2,\"name\":\"Ops\"},{\"id\":3,\"name\":\"IT\"}]";

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void test() throws Exception {
        this.mockMvc.perform(MockMvcRequestBuilders.get("/department"))
                .andExpect(MockMvcResultMatchers.content().json(initialDepartments))
                .andDo(MockMvcResultHandlers.print());
    }
}