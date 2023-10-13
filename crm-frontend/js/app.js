let crmViewModel = new CrmViewModel();
$(document).ready(() => {
    i18n.init(AppConfig.I18N_CONFIG, function (t) {
        $(document).i18n();
        ko.applyBindings(crmViewModel);
        knockoutLocalize('en');
        crmViewModel.customer.validateCustomer();
    });});