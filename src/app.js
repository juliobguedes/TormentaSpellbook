const app = angular.module("TormentaApp", ['ngSanitize', 'ng-showdown', 'ui.router', 'ui.router.stateHelper']);

app.config(function($urlRouterProvider, $stateProvider) {
    $urlRouterProvider.otherwise("/spells");
    $stateProvider.state("spells", {
        url: "/spells",
        templateUrl:'templates/spells.html',
        controller:'spellsCtrl'
    }).state("feats", {
        url: "/feats",
        templateUrl: 'templates/feats.html',
        controller:'featsCtrl'
    }).state("oneSpellCtrl", {
        url: "/spell",
        templateUrl:'templates/oneSpell.html',
        controller:'oneSpellCtrl',
        resolve: {
            url: function($stateParams) {
                return $stateParams;
            }
        }
    });
})