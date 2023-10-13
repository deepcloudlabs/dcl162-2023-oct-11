let hrvm = new HrViewModel();
$(document).ready(() => {
    i18n.init(AppConfig.I18N_CONFIG, function (t) {
        $(document).i18n();
        ko.applyBindings(hrvm);
        knockoutLocalize('en');
        hrvm.employee.validateEmployee();
    });});