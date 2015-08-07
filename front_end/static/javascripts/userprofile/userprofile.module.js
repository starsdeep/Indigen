(function () {
    'use strict';

    angular
        .module('indigen.userprofile', [
            'indigen.userprofile.services',
            'indigen.userprofile.controllers'
        ]);

    angular
        .module('indigen.userprofile.services', ['ngCookies']);

    angular
        .module('indigen.userprofile.controllers', ['ngFileUpload', 'checklist-model']);


})();