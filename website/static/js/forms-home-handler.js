// $(function() {
//     $("#registerForm").submit(function(event) {
//         // Stop form from submitting normally
//         event.preventDefault();
//         var friendForm = $(this);
//         // Send the data using post
//         var posting = $.post( friendForm.attr('action'), friendForm.serialize() );
//         // if success:
//         posting.done(function(data) {
//             // success actions, maybe change submit button to 'friend added' or whatever
//         });
//         // if failure:
//         posting.fail(function(data) {
//             // 4xx or 5xx response, alert user about failure
//         });
//     });
// });