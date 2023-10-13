class Customer {
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
        this.gsm = ko.observable('')
            .extend({
                required: true
            });
        this.photo = ko.observable(toSrcImage(AppConfig.NO_IMAGE));
        this.birthYear = ko.observable(1990);
        this.email = ko.observable("someone@example.com")
            .extend({
                required: true
            });
        this.active = ko.observable(true);
        this.update = this.update.bind(this);
        this.isCustomerValid = this.isCustomerValid.bind(this);
        this.validateCustomer = this.validateCustomer.bind(this);
    }

    isCustomerValid() {
        for (let prop in this) {
            let o = this[prop];
            if (ko.isObservable(o)
                && o.hasOwnProperty('rules')
                && !o.isValid()) return false;
        }
        return true;
    }

    validateCustomer() {
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
    CRM View Model
 */
class CrmViewModel {
    constructor() {
        this.customer = new Customer();
        this.customers = ko.observableArray([]);
        this.fileData = ko.observable({
            dataUrl: ko.observable(toSrcImage(AppConfig.NO_IMAGE))
        });
        this.findAllCustomers = this.findAllCustomers.bind(this);
        this.createCustomer = this.createCustomer.bind(this);
        this.findCustomerByIdentity = this.findCustomerByIdentity.bind(this);
        this.updateCustomer = this.updateCustomer.bind(this);
        this.removeCustomer = this.removeCustomer.bind(this);
        this.insertFile = this.insertFile.bind(this);
        this.dragover = this.dragover.bind(this);
        this.copyCustomer = this.copyCustomer.bind(this);
        this.socket = io("ws://localhost:7001");
        this.socket.on('connect', () => {
            toastr.success("Connected to the server!")
            console.log("Connected!")
            this.socket.on('release', (cust) => {
                this.customers(
                    this.customers().filter(e => e.identity != cust.identity)
                );
                toastr.error(`${cust.fullname} is released!`)
            });
            this.socket.on('acquire', (cust) => {
                cust.photo = toSrcImage(cust.photo);
                this.customers.push(cust);
                toastr.success(`${cust.fullname} is acquired!`)
            });
        });
    }

    copyCustomer(cust) {
        this.customer.update(cust);
        this.fileData().dataUrl(cust.photo);
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
            this.customer.validateCustomer();
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

    removeCustomer(cust) {
        fetch(AppConfig.REST_API_BASE_URL +
            "/customers/" + cust.identity,
            {
                method: 'DELETE'
            }).then(res => res.json())
            .then(cust => {
                toastr.success("Deleted!");
                console.log(cust)
                cust.photo = toSrcImage(cust.photo)
                this.customer.update(cust);
                this.fileData().dataUrl(cust.photo);
                this.customers(
                    this.customers().filter(e => e.identity != cust.identity)
                );
            })
    }

    createCustomer() {
        let body = ko.toJS(this.customer);
        body.photo = toRawImage(this.fileData().dataUrl());
        fetch(AppConfig.REST_API_BASE_URL + "/customers",
            {
                method: 'POST',
                body: JSON.stringify(body),
                headers: new Headers(
                    {"content-type": "application/json"}
                )
            })
            .then(status => toastr.success("Created!"))
    }

    updateCustomer() {
        let body = ko.toJS(this.customer);
        body.photo = toRawImage(this.fileData().dataUrl());
        fetch(AppConfig.REST_API_BASE_URL + "/customers/" + this.customer.identity(),
            {
                method: 'PUT',
                body: JSON.stringify(body),
                headers: new Headers(
                    {"content-type": "application/json"}
                )
            })
            .then(status => toastr.success("Updated!"))
    }

    findCustomerByIdentity() {
        fetch(AppConfig.REST_API_BASE_URL +
            "/customers/" + this.customer.identity())
            .then(res => res.json())
            .then(cust => {
                cust.photo = toSrcImage(cust.photo);
                this.customer.update(cust);
                this.fileData().dataUrl(cust.photo);
            });
    }

    findAllCustomers() {
        fetch(AppConfig.REST_API_BASE_URL + "/customers")
            .then(res => res.json())
            .then(custs => {
                custs = custs.map(cust => {
                    if (!cust.hasOwnProperty('photo')) cust.photo = AppConfig.NO_IMAGE;
                    cust.photo = toSrcImage(cust.photo);
                    return cust;
                });
                this.customers(custs);
                this.i18n();
            });
    }
};












