app.controller("oneSpellCtrl", function($scope, url, $showdown, $http) {
    let newUrl = "https://raw.githubusercontent.com/juliobguedes/TormentaSpellbook/master/" + url;
    $http.get(newUrl)
        .then(res => {
            $scope.spell = $showdown.makeHtml(res.data);
        }).catch(error => {
            console.log("error");
            console.log(error)
        })
})