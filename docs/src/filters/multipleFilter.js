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
                let newString = selected.procedence;
                bool = bool && (spell.procedence.indexOf(newString) > -1);
            }
            if (selected.level != undefined) {
                let newString = "level" + selected.level;
                bool = bool && (spell.level.indexOf(newString) > -1);
            }
            if (selected.description) {
                let newString = patternString(selected.description);
                bool = bool && (spell.descriptions.indexOf(newString) > -1);
            }
            if (selected.executionTime) {
                let newString = patternString(selected.executionTime);
                bool = bool && (spell.executionTimes.indexOf(newString) > -1);
            }
            if (selected.range) {
                let newString = patternString(selected.range);
                bool = bool && (spell.ranges.indexOf(newString) > -1);
            }
            if (selected.effect) {
                let newString = patternString(selected.effect);
                bool = bool && (spell.effects.indexOf(newString) > -1);
            }
            if (selected.duration) {
                let newString = patternString(selected.duration);
                bool = bool && (spell.durations.indexOf(newString) > -1);
            }
            if (selected.resTest) {
                let newString = patternString(selected.resTest);
                bool = bool && (spell.restTests.indexOf(newString) > -1);
            }
            if (selected.resType) {
                let newString = patternString(selected.resType);
                bool = bool && (spell.resTypes.indexOf(newString) > -1);
            }
            if (selected.god) {
                let newString = patternString(selected.god);
                bool = bool && (spell.gods.indexOf(newString) > -1);
            }
            if (selected.class) {
                let newString = patternString(selected.class);
                bool = bool && (spell.classes.indexOf(newString) > -1);
            }
            if (selected.source) {
                let newString = patternString(selected.source);
                bool = bool && (spell.source.indexOf(selected.source) > -1);
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