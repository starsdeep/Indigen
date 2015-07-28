(function () {
    'use strict';

    angular
        .module('indigen', [
            'indigen.config',
            'indigen.routes',
            'indigen.authentication',
            'indigen.layout'
        ]);

    angular
        .module('indigen.config', []);

    angular
        .module('indigen.routes', ['ngRoute']);


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