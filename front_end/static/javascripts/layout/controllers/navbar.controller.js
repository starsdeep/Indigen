/**
* NavbarController
* @namespace indigen.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('indigen.layout.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', 'userAuthService'];

  /**
  * @namespace NavbarController
  */
  function NavbarController($scope, userAuthService) {
    var vm = this;
    vm.AuthenticatedAccount = userAuthService.getAuthenticatedAccount();
    vm.logout = logout;
    console.log('narbar auth: ' + JSON.stringify(vm.AuthenticatedAccount));


    /**
    * @name logout
    * @desc Log the user out
    * @memberOf indigen.layout.controllers.NavbarController
    */
    function logout() {
      userAuthService.logout();
    }
  }
})();