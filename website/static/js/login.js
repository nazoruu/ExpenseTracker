$('.message a').click(function(){
    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
 });

 document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the login button
    document.getElementById('login-btn').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Redirect to the /home route
        window.location.href = '/home';
    });
});

