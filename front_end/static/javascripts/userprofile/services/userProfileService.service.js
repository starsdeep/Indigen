(function () {
    'use strict';

    angular
        .module('indigen.userprofile.services')
        .service('userProfileService', userProfileService);

    userProfileService.$inject = ['$http', 'API', 'userAuthService'];

    function userProfileService($http, API, userAuthService){
        var self = this;


        function setup(){
            $http.defaults.headers.common.Authorization = 'Token ' + userAuthService.getAuthenticatedAccount()['token'];
            console.log('userProfileService Token ' + userAuthService.getAuthenticatedAccount()['token'] );
        }


        //field is an array of requirefield
        this.getUserProfile = function(field){
            setup();
            return $http.get(API + 'profile/', field).then(getSuccessFn, getErrorFn);

            function getSuccessFn(data, status, headers, config) {
                console.log('success');
                //console.log("data: " + JSON.stringify(data.data));
                //self.setAuthenticatedAccount(data.data);
                //window.location = '/';
            }

            function getErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }

        }

        //base_info is a dict
        this.updateUserProfile = function(base_info){
            setup();
            return $http.put( API + 'profile/', base_info);
        };




    }

} )();