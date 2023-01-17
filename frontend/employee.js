function getEmployees() {
    return fetch('http://localhost:8080/employee')
        .then(function (res) { return res.json() })
}

function deleteEmployee(id) {
    fetch('http://localhost:8080/employee/' + id, {
        method: 'DELETE',
    })
        .then(function (response) {
            if (response.ok) {
                window.location.reload();
            }
            throw new Error('Something went wrong');
        })
        .catch(function (error) {
            console.log(error)
        });
}

function addEmployee(json) {
    fetch('http://localhost:8080/employee', {
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        body: json
    })
        .then(function (response) {
            if (response.ok) {
                window.location.replace("http://localhost");
            }
            throw new Error('Something went wrong');
        })
        .catch(function (error) {
            console.log(error)
        });
}

function setEmployeesTable(elementName) {
    getEmployees().then(function (json) {
        var root = document.getElementById(elementName);
        json.forEach(element => root.insertAdjacentHTML('beforebegin', `<tr>
            <td>${element.id}</td>
            <td>${element.firstName}</td>
            <td>${element.lastName}</td>
            <td>${element.department.name}</td>
            <td><button type="button" class="btn btn-danger"
                onclick="deleteEmployee(${element.id})">Delete</button></td>
            </tr>`));
        root.insertAdjacentHTML('beforebegin', `<br/><p class="text-muted">Query returned ${json.length} result(s)</p>`);
    });
}

