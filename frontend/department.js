function getDepartments() {
    return fetch('http://localhost:8080/department')
        .then(function (res) { return res.json() })
}

function setDepartmentOptions(elementName) {
    getDepartments().then(function (json) {
        options = "<option disabled selected value>Choose...</option>";
        for (var key in json) {
            options += "<option value=" + json[key].id + ">" + json[key].name + "</option>"
        }
        document.getElementById(elementName).innerHTML = options;
    });
}