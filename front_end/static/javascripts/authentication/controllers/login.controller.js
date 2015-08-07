/**
 * LoginController
 * @namespace indigen.authentication.controllers
 */
(function () {
    'use strict';

    angular
        .module('indigen.authentication.controllers')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', '$scope', 'userAuthService'];

    /**
     * @namespace LoginController
     */
    function LoginController($location, $scope, userAuthService) {
        var vm = this;

        vm.login = login;

        activate();


        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf indigen.authentication.controllers.LoginController
         */
        function activate() {
            // If the user is authenticated, they should not be here.
            if (userAuthService.isAuthenticated()) {
                $location.url('/');
            }
        }


        /**
         * @name login
         * @desc Log the user in
         * @memberOf indigen.authentication.controllers.LoginController
         */
        function login() {
            userAuthService.login(vm.username, vm.password);
        }
    }
})();