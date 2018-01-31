app.service("Tormenta", function($http) {

    this.getSpells = () => {
        return $http.get('spells.json');
    }

    this.getFeats = () => {
        return $http.get('feats.json');
    }
})