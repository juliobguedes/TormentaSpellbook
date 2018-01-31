app.filter("procedenceFilter", function() {
    return function(array, param1) {
        return array.filter(procFilter(param1));
    }
})

function procFilter(proc) {
    return function(spell) {
        if (proc) 
            return spell.procedence.indexOf(proc) > -1;
        return true;
    }
}