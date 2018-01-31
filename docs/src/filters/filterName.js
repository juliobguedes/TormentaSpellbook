app.filter("filterName", function() {
    return function myFilter(array, name) {
        return array.filter(filterByName(name));
    }
})

function filterByName(name) {
    return function(object) {
        if (name) {
            let nameS = object.name.toLowerCase();
            return nameS.indexOf(name) > -1;
        }
        return true;
    }
}