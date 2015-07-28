(function () {
  'use strict';

  angular
    .module('indigen.authentication', [
      'indigen.authentication.controllers',
      'indigen.authentication.services'
    ]);

  angular
    .module('indigen.authentication.controllers', []);

  angular
    .module('indigen.authentication.services', ['ngCookies']);
})();