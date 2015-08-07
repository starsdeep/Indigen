(function () {
    'use strict';

    angular
        .module('indigen.authentication.services')
        .service('userAuthService', userAuthService);

    userAuthService.$inject = ['$http', '$cookies', 'API', 'tokenService'];

    function userAuthService($http, $cookies, API, tokenService) {
        var self = this;

        // add authentication methods here
        self.register = function (telephone, nickname, password, captcha) {
            return $http.post(API + 'register/', {
                telephone: telephone,
                nickname: nickname,
                password: password,
                captcha: captcha
            }).then(registerSuccessFn, registerErrorFn);

            function registerSuccessFn(data, status, headers, config) {
                userAuthService.login(telephone, password);
            }

            function registerErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }
        };

        self.logout = function() {
            return $http.post(API +'logout/')
                .then(logoutSuccessFn, logoutErrorFn);

            function logoutSuccessFn(data, status, headers, config) {
                self.unauthenticate();
                window.location = '/';
            }

            function logoutErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }
        };

        self.login = function (username, password) {
            return $http.post(API + 'login/', {
                username: username,
                password: password
            }).then(loginSuccessFn, loginErrorFn);

            function loginSuccessFn(data, status, headers, config) {
                console.log("data: " + JSON.stringify(data.data));
                self.setAuthenticatedAccount(data.data);
                window.location = '/';
            }

            function loginErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }

        };

        self.isAuthenticated = function() {
            return  !!$cookies.get('authenticatedAccount');
        };

        self.getAuthenticatedAccount = function() {
            if (!$cookies.get('authenticatedAccount')) {
                return;
            }
            return JSON.parse($cookies.get('authenticatedAccount'));
        };

        self.setAuthenticatedAccount = function (account) {

            /* this the cookies set by this method is not persisting
             $cookies.authenticatedAccount = JSON.stringify(account);
             */
            //to make the cookies persisting, we should set the expiration date
            var today = new Date();
            var expired = new Date(today);
            expired.setDate(today.getDate() + 5); //Set expired date to tomorrow
            $cookies.put('authenticatedAccount', JSON.stringify(account), {expires: expired});
            console.log('cookies:' + $cookies.get('authenticatedAccount'));
        }


        self.unauthenticate = function unauthenticate() {
            $cookies.remove('authenticatedAccount');
            //tokenService.logout();
        }


    }

})();
