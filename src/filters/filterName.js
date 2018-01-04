app.filter("filterName", function() {
    function myFilter(array, name) {
        return array.filter(filterByName(name));
    }
    myFilter.$stateful = true;
    return myFilter;

})

function filterByName(name) {
    return function(object) {
        return object.name.indexOf(name) > -1;
    }
}