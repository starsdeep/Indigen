(function () {
    'use strict';

    angular
        .module('indigen.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    function config($routeProvider) {
        $routeProvider.when('/register', {
            controller: 'RegisterController',
            controllerAs: 'vm',
            templateUrl: 'front_end/static/templates/authentication/register.html'
        }).when('/login', {
            controller: 'LoginController',
            controllerAs: 'vm',
            templateUrl: 'front_end/static/templates/authentication/login.html'
        }).otherwise('/')
    }

    /*
     function config($routeProvider) {
     $routeProvider.when('/register', {
     controller: 'RegisterController',
     controllerAs: 'vm',
     templateUrl: '/static/templates/authentication/register.html'
     }).when('/login', {
     controller: 'LoginController',
     controllerAs: 'vm',
     templateUrl: '/static/templates/authentication/login.html'
     }).when('/', {
     controller: 'IndexController',
     controllerAs: 'vm',
     templateUrl: '/static/templates/layout/index.html'
     }).otherwise('/');
     }*/
})();