app.filter("multipleFilter", function() {
    return function(array, selected) {
        return array.filter(multipleFilter(selected));
    }
})

function multipleFilter(selected) {
    return function(spell) {
        let bool = true;
        if (selected) {
            if (selected.procedence) {
                let newString = selected.procedence.toLowerCase();
                bool = bool && (spell.procedence.indexOf(newString) > -1);
            }
            if (selected.level) {
                let newString = selected.level.toLowerCase();
                newString = "level" + newString;
                bool = bool && (spell.level.indexOf(newString) > -1);
            }
            if (selected.description) {
                let newString = selected.description.toLowerCase();
                bool = bool && (spell.descriptions.indexOf(newString) > -1);
            }
            if (selected.executionTime) {
                let newString = selected.executionTime.toLowerCase();
                bool = bool && (spell.executionTimes.indexOf(newString) > -1);
            }
            if (selected.range) {
                let newString = selected.range.toLowerCase();
                bool = bool && (spell.ranges.indexOf(newString) > -1);
            }
            if (selected.effect) {
                let newString = selected.effect.toLowerCase();
                bool = bool && (spell.effects.indexOf(newString) > -1);
            }
            if (selected.duration) {
                let newString = selected.duration.toLowerCase();
                bool = bool && (spell.durations.indexOf(newString) > -1);
            }
            if (selected.resTest) {
                let newString = selected.resTest.toLowerCase();
                bool = bool && (spell.restTests.indexOf(newString) > -1);
            }
            if (selected.resType) {
                let newString = selected.resType.toLowerCase();
                bool = bool && (spell.resTypes.indexOf(newString) > -1);
            }
            if (selected.god) {
                let newString = selected.god.toLowerCase();
                bool = bool && (spell.gods.indexOf(newString) > -1);
            }
            if (selected.class) {
                let newString = selected.class.toLowerCase();
                bool = bool && (spell.classes.indexOf(newString) > -1);
            }
        }
        return bool;
    }
}

function patternString(string) {
    let newString = string.toLowerCase();
    newString = newString.normalize('NFD').replace(/[\u0300-\u036f]/g, "");
    return newString;
}