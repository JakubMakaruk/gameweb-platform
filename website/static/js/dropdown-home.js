document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-account');
    console.log(elems)
    var instances = M.Dropdown.init(elems, {
        'alignment': 'right',
        'coverTrigger': false
    });
  });