app.controller("spellsCtrl", function(Tormenta, $scope, $state) {

    $scope.initiate = () => {
        $scope.zero = [];
        $scope.one = [];
        $scope.two = [];
        $scope.three = [];
        $scope.four = [];
        $scope.five = [];
        $scope.six = [];
        $scope.seven = [];
        $scope.eight = [];
        $scope.nine = [];        
    }

    $scope.separatePerLevel = (data) => {
        $scope.zero = data.filter(levelFilter("0"));
        $scope.one = data.filter(levelFilter("1"));
        $scope.two = data.filter(levelFilter("2"));
        $scope.three = data.filter(levelFilter("3"));
        $scope.four = data.filter(levelFilter("4"));
        $scope.five = data.filter(levelFilter("5"));
        $scope.six = data.filter(levelFilter("6"));
        $scope.seven = data.filter(levelFilter("7"));
        $scope.eight = data.filter(levelFilter("8"));
        $scope.nine = data.filter(levelFilter("9"));
    }
    
    loadSpells($scope, Tormenta);
    $scope.showHide = function(field) {
        if (field == 0) {
            $scope.showZero = !$scope.showZero;
        } else if (field == 1) {
            $scope.showOne = !$scope.showOne;
        } else if (field == 2) {
            $scope.showTwo = !$scope.showTwo;
        } else if (field == 3) {
            $scope.showThree = !$scope.showThree;
        } else if (field == 4) {
            $scope.showFour = !$scope.showFour;
        } else if (field == 5) {
            $scope.showFive = !$scope.showFive;
        } else if (field == 6) {
            $scope.showSix = !$scope.showSix;
        } else if (field == 7) {
            $scope.showSeven = !$scope.showSeven;
        } else if (field == 8) {
            $scope.showEight = !$scope.showEight;
        } else if (field == 9) {
            $scope.showNine = !$scope.showNine;
        }
    }

    $scope.spellC = {
        "procedence": ["Arcana", "Divina"], 
        "levels": [0,1,2,3,4,5,6,7,8,9], 
        "description": ["Abjuração", "Ácido", "Adivinhação", "Água", "Ar", "Caos", "Cura", "Eletricidade", "Encantamento", "Escuridão", "Essência", "Fogo", "Frio", "Sônico", "Terra",
        "Bem", "Mal", "Ordem", "Luz", "Ilusão", "Invocação", "Medo", "Necromancia", "Tempo",
        "Transmutação"], 
        "executionTime": ["livre", "movimento", "padrao", "completa", "concentração", "rodadas"], 
        "range": ["pessoal","toque", "metros", "ilimitada"], 
        "effect": ["criatura", "objeto", "cilindro", "cone", "esfera", "linha", "explosão", "dispersão", "emanação", "raio", "outros"], 
        "duration": ["instantânea", "concentração", "permanente", "descarregar"], 
        "resistanceTest": ["fortitude", "reflexos", "vontade"], 
        "resistanceType": ["anula", "parcial", "metade", "nenhum"], 
        "ingredients": ["componente material", "experiência"],
        "gods": ["Allihanna", "Azgher", "Hynnin", "Kallyandranoch", "Keenn", "Khalmyr", "Lena", "Lin-Wu", "Marah", "Megalokk", "Nimb",
        "Oceano", "Ragnar", "Sszzas", "Tanna-Toh", "Tauron", "Tenebra", "Thyatis", "Valkária", "Wynna"], 
        "classes": ["Abençoado", "Bardo", "Clérigo", "Druida", "Feiticeiro", "Mago", "Paladino", "Ranger"]
    };

    $scope.change = (spell) => {
        console.log(spell);
        $state.go("oneSpell", {"name":spell.name, "url":spell.url});
    }

})

function showAll($scope) {
    $scope.showZero = true;
    $scope.showOne = true;
    $scope.showTwo = true;
    $scope.showThree = true;
    $scope.showFour = true;
    $scope.showFive = true;
    $scope.showSix = true;
    $scope.showSeven = true;
    $scope.showEight = true;
    $scope.showNine = true;
}

function levelFilter(level) {
    return function(spell) {
        if (spell.level == undefined) {
            console.log(spell);
        }
        return spell.level.indexOf("level" + level) > -1;
    }
}

function loadSpells($scope, Tormenta) {
    $scope.initiate();
    Tormenta.getSpells()
        .then(res => {
            $scope.separatePerLevel(res.data.data);
            showAll($scope);
        })

}