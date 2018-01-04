app.filter("multipleFilter", function() {
    return function(spells, selected) {
        console.log(spells);
        console.log(selected);
        return spells.filter(multipleFilter(selected));
    }
})

function multipleFilter(selected) {
    return function(spell) {
        let bool = true;
        if (selected) {
            if (selected.procedence) {
                bool = bool && (spell.procedence.indexOf(selected.procedence) > -1);
            }
            if (selected.levels) {
                bool = bool && (spell.level.indexOf(selected.level) > -1);
            }
            if (selected.description) {
                bool = bool && (spell.descriptions.indexOf(selected.description) > -1);
            }
            if (selected.executionTime) {
                bool = bool && (spell.executionTimes.indexOf(selected.executionTime) > -1);
            }
            if (selected.range) {
                bool = bool && (spell.ranges.indexOf(selected.range) > -1);
            }
            if (selected.effect) {
                bool = bool && (spell.effects.indexOf(selected.effect) > -1);
            }
            if (selected.duration) {
                bool = bool && (spell.durations.indexOf(selected.duration) > -1);
            }
            if (selected.resistanceTest) {
                bool = bool && (spell.restTests.indexOf(selected.resTest) > -1);
            }
            if (selected.resistanceType) {
                bool = bool && (spell.resTypes.indexOf(selected.resType) > -1);
            }
            if (selected.gods) {
                bool = bool && (spell.gods.indexOf(selected.god) > -1);
            }
            if (selected.classes) {
                bool = bool && (spell.classes.indexOf(selected.class) > -1);
            }
        }
        return bool;
    }
}