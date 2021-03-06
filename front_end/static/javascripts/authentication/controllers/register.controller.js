/**
 * Register controller
 * @namespace indigen.authentication.controllers
 */
(function () {
    'use strict';

    angular
        .module('indigen.authentication.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'userAuthService'];

    /**
     * @namespace RegisterController
     */
    function RegisterController($location, $scope, userAuthService) {
        var vm = this;

        vm.register = register;

        /**
        activate();

        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf thinkster.authentication.controllers.RegisterController

        function activate() {
            // If the user is authenticated, they should not be here.
            if (Authentication.isAuthenticated()) {
                $location.url('/');
            }
        }
         */


        /**
         * @name register
         * @desc Register a new user
         * @memberOf indigen.authentication.controllers.RegisterController
         */
        function register() {
            userAuthService.register(vm.telephone, vm.nickname, vm.password, vm.captcha);
        }
    }
})();