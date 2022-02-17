document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelector('#modalAddRate');
    var instances = M.Modal.init(elems, {
        'opacity': 0.7,
        'startingTop': '4%'
    });
});
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelector('#modalAddComment');
    var instances = M.Modal.init(elems, {
        'opacity': 0.7,
        'startingTop': '4%'
    });
});