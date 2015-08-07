(function () {
  'use strict';

  angular
    .module('indigen.config')
    .config(config);

  config.$inject = ['$locationProvider', '$httpProvider'];

  /**
  * @name config
  * @desc Enable HTML5 routing and JWT token
  */
  function config($locationProvider, $httpProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
    //$httpProvider.interceptors.push('AuthInterceptor');
  }

})();