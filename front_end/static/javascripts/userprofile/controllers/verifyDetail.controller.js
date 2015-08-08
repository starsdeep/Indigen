/**
 * VerifyBaseController
 * @namespace indigen.authentication.controllers
 */
(function () {
    'use strict';

    angular
        .module('indigen.userprofile.controllers')
        .controller('VerifyDetailController', VerifyDetailController);

    VerifyDetailController.$inject = ['$location', '$scope', 'API', 'userAuthService', 'userProfileService'];

    /**
     * @namespace VerifyBaseController
     */
    function VerifyDetailController($location, $scope, API ,userAuthService, userProfileService) {
        var vm = this;
        vm.submit = submit;

        vm.languages = ['普通话', '英语', '日语'];
        vm.characters = ['购物狂人', '夜店达人', '背包客'];


        vm.formdata = {
            'vocation_type': '',
            'languages': ['普通话'],
            'native_province': '',
            'native_city': '',
            'vocation': '',
            'hobbies': '',
            'characters': []
        };

        activate();

        function submit() {
            userProfileService.updateUserProfile(vm.formdata);
        }
        


        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf indigen.authentication.controllers.VerifyBaseController
         */
        function activate() {
            // If the user is not authenticated, they should login in first.
            //console.log('scope is', scope);
            console.log('isAuth:' + userAuthService.isAuthenticated());
            if (!userAuthService.isAuthenticated()) {
                $location.url('/login');
            }

            vm.formdata = userProfileService.getUserProfile(Object.keys(vm.formdata));
        }

    }
})();