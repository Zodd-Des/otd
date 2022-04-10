/* 1) Auto close boootstrap alert after 3s */
window.setTimeout(function() {
  $('.alert').fadeTo(500, 0).slideUP(500, function() {
    $(this).remove();
  });
}, 3000);

// 2) script to protect against DDOS attack(prevent F5 after submit)
if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}