(function () {
    'use strict';

    angular
        .module('indigen.authentication', [
            'indigen.authentication.services',
            'indigen.authentication.controllers'
        ]);

    angular
        .module('indigen.authentication.services', ['ngCookies']);

    angular
        .module('indigen.authentication.controllers', []);




})();