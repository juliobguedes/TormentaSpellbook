app.controller("oneSpellCtrl", function($scope, url, $showdown, $http) {
    $http.get(url)
        .then(res => {
            console.log(res);
            $scope.spell = $showdown.makeHtml(res.data);
        }).catch(error => {
            console.log("error");
            console.log(error)
        })
})