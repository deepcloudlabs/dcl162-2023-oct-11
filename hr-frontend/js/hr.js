class Employee {
    constructor() {
        this.identity = ko.observable('')
            .extend({
                required: true,
                tcKimlikNo: true
            });
        this.fullname = ko.observable("")
            .extend({
                required: true,
                minLength: 5
            });
        this.iban = ko.observable('TR')
            .extend({
                required: true,
                iban: true
            });
        this.photo = ko.observable(toSrcImage(AppConfig.NO_IMAGE));
        this.birthYear = ko.observable(1990);
        this.salary = ko.observable(20000)
            .extend({
                required: true,
                min: 2100
            });
        this.department = ko.observable("IT");
        this.fulltime = ko.observable(true);
        this.update = this.update.bind(this);
        this.isEmployeeValid = this.isEmployeeValid.bind(this);
        this.validateEmployee = this.validateEmployee.bind(this);
    }

    isEmployeeValid() {
        for (let prop in this) {
            let o = this[prop];
            if (ko.isObservable(o)
                && o.hasOwnProperty('rules')
                && !o.isValid()) return false;
        }
        return true;
    }

    validateEmployee() {
        for (let prop in this) {
            let value = this[prop];
            if (ko.isObservable(value)
                && 'rules' in value) {
                value.isModified(true);
                ko.validation.validateObservable(value);
            }
        }
    }

    update(emp) {
        for (let prop in emp) {
            if (this.hasOwnProperty(prop)) {
                let o = this[prop];
                if (ko.isObservable(o)) {
                    this[prop](emp[prop]);
                } else {
                    this[prop] = emp[prop];
                }
            }
        }
    }
};

/*
    HR View Model
 */
class HrViewModel {
    constructor() {
        this.employee = new Employee();
        this.employees = ko.observableArray([]);
        this.fileData = ko.observable({
            dataUrl: ko.observable(toSrcImage(AppConfig.NO_IMAGE))
        });
        this.findAllEmployees = this.findAllEmployees.bind(this);
        this.createEmployee = this.createEmployee.bind(this);
        this.findEmployeeByIdentity = this.findEmployeeByIdentity.bind(this);
        this.updateEmployee = this.updateEmployee.bind(this);
        this.removeEmployee = this.removeEmployee.bind(this);
        this.insertFile = this.insertFile.bind(this);
        this.dragover = this.dragover.bind(this);
        this.copyEmployee = this.copyEmployee.bind(this);
        this.socket = io("ws://localhost:7001");
        this.socket.on('connect', () => {
            toastr.success("Connected to the server!")
            console.log("Connected!")
            this.socket.on('fire', (emp) => {
                this.employees(
                    this.employees().filter(e => e.identity != emp.identity)
                );
                toastr.error(`${emp.fullname} is fired!`)
            });
            this.socket.on('hire', (emp) => {
                emp.photo = toSrcImage(emp.photo);
                this.employees.push(emp);
                toastr.success(`${emp.fullname} is hired!`)
            });
        });
    }

    copyEmployee(emp) {
        this.employee.update(emp);
        this.fileData().dataUrl(emp.photo);
    }

    i18n() {
        $(document).i18n();
    }

    changeLangToTr() {
        this.changeLang('tr');
    }

    changeLangToEn() {
        this.changeLang('en');
    }

    changeLang(lang) {
        i18n.setLng(lang, () => {
            this.i18n();
            knockoutLocalize(lang);
            this.employee.validateEmployee();
        });
    }

    insertFile(e, data) {
        e.preventDefault();
        let files = e.target.files || e.originalEvent.dataTransfer.files;
        let reader = new FileReader();
        reader.readAsDataURL(files[0]);
        reader.onload = (event) => {
            this.fileData().dataUrl(event.target.result);
        };
    };

    dragover(e) {
        e.preventDefault();
    };

    removeEmployee(emp) {
        fetch(AppConfig.REST_API_BASE_URL +
            "/employees/" + emp.identity,
            {
                method: 'DELETE'
            }).then(res => res.json())
            .then(emp => {
                toastr.success("Deleted!");
                console.log(emp)
                emp.photo = toSrcImage(emp.photo)
                this.employee.update(emp);
                this.fileData().dataUrl(emp.photo);
                this.employees(
                    this.employees().filter(e => e.identity != emp.identity)
                );
            })
    }

    createEmployee() {
        let body = ko.toJS(this.employee);
        body.photo = toRawImage(this.fileData().dataUrl());
        fetch(AppConfig.REST_API_BASE_URL + "/employees",
            {
                method: 'POST',
                body: JSON.stringify(body),
                headers: new Headers(
                    {"content-type": "application/json"}
                )
            })
            .then(status => toastr.success("Created!"))
    }

    updateEmployee() {
        let body = ko.toJS(this.employee);
        body.photo = toRawImage(this.fileData().dataUrl());
        fetch(AppConfig.REST_API_BASE_URL + "/employees/" + this.employee.identity(),
            {
                method: 'PUT',
                body: JSON.stringify(body),
                headers: new Headers(
                    {"content-type": "application/json"}
                )
            })
            .then(status => toastr.success("Updated!"))
    }

    findEmployeeByIdentity() {
        fetch(AppConfig.REST_API_BASE_URL +
            "/employees/" + this.employee.identity())
            .then(res => res.json())
            .then(emp => {
                emp.photo = toSrcImage(emp.photo);
                this.employee.update(emp);
                this.fileData().dataUrl(emp.photo);
            });
    }

    findAllEmployees() {
        fetch(AppConfig.REST_API_BASE_URL + "/employees")
            .then(res => res.json())
            .then(emps => {
                emps = emps.map(emp => {
                    if (!emp.hasOwnProperty('photo')) emp.photo = AppConfig.NO_IMAGE;
                    emp.photo = toSrcImage(emp.photo);
                    return emp;
                });
                this.employees(emps);
                this.i18n();
            });
    }
};












