$(document).ready(function(){
    $('.modal-news').modal();
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelector('#modalLoginRegister');
    var instances = M.Modal.init(elems, {
        'opacity': 0.8,
        'startingTop': '4%'
    });
});