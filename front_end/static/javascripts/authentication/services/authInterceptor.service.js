(function () {
    'use strict';

    angular
        .module('indigen.authentication.services')
        .factory('AuthInterceptor', AuthInterceptor);

    AuthInterceptor.$inject = ['API', 'tokenService'];

    function AuthInterceptor(API, tokenService) {
        return {
            // automatically attach Authorization header
            request: function (config) {
                var token = tokenService.getToken();
                if (config.url.indexOf(API) === 0 && token) {
                    config.headers.Authorization = 'Token ' + token;
                }

                return config;
            },

            // If a token was sent back, save it
            response: function (res) {
                if (res.config.url.indexOf(API) === 0 && res.data.token) {
                    tokenService.saveToken(res.data.token);
                }

                return res;
            }
        }

    };

})();