/**
* Register controller
* @namespace indigen.authentication.controllers
*/
(function () {
  'use strict';

  angular
    .module('indigen.authentication.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['$location', '$scope', 'Authentication'];

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register;

    /**
    * @name register
    * @desc Register a new user
    * @memberOf indigen.authentication.controllers.RegisterController
    */
    function register() {
      Authentication.register(vm.telephone, vm.nickname, vm.password, vm.captcha);
    }
  }
})();