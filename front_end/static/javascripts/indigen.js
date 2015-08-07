(function () {
    'use strict';

    angular
        .module('indigen', [
            'indigen.config',
            'indigen.routes',
            'indigen.authentication',
            'indigen.userprofile',
            'indigen.layout'
        ])
        .constant('API', '/api/v1/');

    angular
        .module('indigen.config', ['indigen.authentication']);

    angular
        .module('indigen.routes', ['ngRoute']);

    angular
        .module('indigen.anthentication', []);

    angular
        .module('indigen.userprofile', ['indigen.authentication']);

    angular
        .module('indigen.layout', ['indigen.authentication']);


    angular
        .module('indigen')
        .run(run);

    run.$inject = ['$http'];

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's defaults
     */
    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

})();