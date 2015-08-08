/**
 * VerifyRealController
 * @namespace indigen.authentication.controllers
 */
(function () {
    'use strict';

    angular
        .module('indigen.userprofile.controllers')
        .controller('VerifyRealController', VerifyRealController);

    VerifyRealController.$inject = ['$location', '$scope', 'Upload', 'API', 'userAuthService', 'userProfileService'];

    /**
     * @namespace VerifyRealController
     */
    function VerifyRealController($location, $scope, Upload, API ,userAuthService, userProfileService) {
        var vm = this;
        vm.submit = submit;
        vm.formdate = {
            'verify_country': '',
            'verify_telephone': '',
            'verify_city': '',
            'live_start_year': ''
        };


        activate();

        //upload avatar
        $scope.$watch('file', function () {
            upload([$scope.file], 'Token ' + userAuthService.getAuthenticatedAccount()['token']);
        });



        function submit() {
            userProfileService.updateUserProfile(vm.formdate).then(updateSuccessFn, updateErrorFn);

            function updateSuccessFn(data, status, headers, config) {
                console.log('success');
                //$location.url('/verify_detail');
            }

            function updateErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            };
        }




        // set default directive values
        // Upload.setDefaults( {ngf-keep:false ngf-accept:'image/*', ...} );
        function upload(files, token) {
            console.log('in upload, token is: ' + token);
            if (files && files.length) {
                console.log('in for');
                for (var i = 0; i < files.length; i++) {
                    var file = files[i];
                    Upload.upload({

                        url: '/api/v1/upload_file/',
                        method: 'POST',
                        headers: {'Authorization': token},
                        fields: {
                            'username': $scope.username
                        },
                        avatar: file

                        /*
                         url: 'https://angular-file-upload-cors-srv.appspot.com/upload',
                         fields: {
                         'username': vm.username
                         },
                         file: file
                         */
                    }).progress(function (evt) {
                        var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                        vm.log = 'progress: ' + progressPercentage + '% ' + evt.config.file.name;
                    }).success(function (data, status, headers, config) {
                        vm.log = 'file ' + config.file.name + 'uploaded. Response: ' + data;
                    }).error(function (data, status, headers, config) {
                        vm.log = 'error status: ' + status;
                    })
                }
            }
        };


        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf indigen.authentication.controllers.VerifyRealController
         */
        function activate() {
            // If the user is not authenticated, they should login in first.
            //console.log('scope is', scope);
            console.log('isAuth:' + userAuthService.isAuthenticated());
            if (!userAuthService.isAuthenticated()) {
                $location.url('/login');
            }

            vm.formdate = userProfileService.getUserProfile(Object.keys(vm.formdate));
        }


    }
})();