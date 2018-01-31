app.controller("featsCtrl", function($scope, Tormenta, $state) {

    $scope.separatePerType = (data) => {
        $scope.combate = data.filter(typeFilter("Combate"));
        $scope.magia = data.filter(typeFilter("Magia"));
        $scope.pericia = data.filter(typeFilter("Perícia"));
        $scope.destino = data.filter(typeFilter("Destino"));
        $scope.tormenta = data.filter(typeFilter("Tormenta"));
        $scope.poderesConcedidos = data.filter(typeFilter("Poderes Concedidos"));
        $scope.racial = data.filter(typeFilter("Racial"));
        $scope.regional = data.filter(typeFilter("Regional"));
    }

    $scope.initiate = () => {
        $scope.combate = [];
        $scope.magia = [];
        $scope.pericia = [];
        $scope.destino = [];
        $scope.tormenta = [];
        $scope.poderesConcedidos = [];
        $scope.racial = [];
        $scope.regional = [];
    }

    loadFeats($scope, Tormenta);

    $scope.showHide = (field) => {
        if (field == "combate") {
            $scope.showCombate = !$scope.showCombate;
        } else if (field == "magia") {
            $scope.showMagia = !$scope.showMagia;
        } else if (field == "pericia") {
            $scope.showPericia = !$scope.showPericia;
        } else if (field == "destino") {
            $scope.showDestino = !$scope.showDestino;
        } else if (field == "poderconcedido") {
            $scope.showPoderConcedido = !$scope.showPoderConcedido;
        } else if (field == "raciais") {
            $scope.showRaciais = !$scope.showRaciais;
        } else if (field == "regionais") {
            $scope.showRegionais = !$scope.showRegionais;
        } else {
            $scope.showTormenta = !$scope.showTormenta;
        };
    };

    $scope.change = (feat) => {
        $state.go("oneSpell", {"name":feat.nome, "url":feat.url});
    }

});

function typeFilter(type) {
    return function(talento) {
        return type == talento.tipo;
    }
}

function showAll($scope) {
    $scope.showCombate = true;
    $scope.showMagia = true;
    $scope.showPericia = true;
    $scope.showDestino = true;
    $scope.showTormenta = true;
    $scope.showPoderConcedido = true;
    $scope.showRegionais = true;
    $scope.showRaciais = true;
}

function loadFeats($scope, Tormenta) {
    $scope.initiate();
    Tormenta.getFeats()
        .then(res => {
            $scope.separatePerType(res.data.data);
            showAll($scope);
        }).catch(err => {
            console.log("Ocorreu um erro");
            console.log(err);
        });
}