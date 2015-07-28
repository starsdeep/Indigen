/**
* Authentication
* @namespace indigen.authentication.services
*/
(function () {
  'use strict';

  angular
    .module('indigen.authentication.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$cookies', '$http'];

  /**
  * @namespace Authentication
  * @returns {Factory}
  */
  function Authentication($cookies, $http) {
    /**
    * @name Authentication
    * @desc The Factory to be returned
    */
    var Authentication = {
      register: register
    };

    return Authentication;

    ////////////////////

    /**
    * @name register
    * @desc Try to register a new user
    * @param {string} username The username entered by the user
    * @param {string} password The password entered by the user
    * @param {string} email The email entered by the user
    * @returns {Promise}
    * @memberOf thinkster.authentication.services.Authentication
    */
    function register(telephone, nickname, password, captcha) {
      return $http.post('/users/', {
        telephone: telephone,
        nickname: nickname,
        password: password,
        captha: captcha
      });
    }
  }
})();