// Here vanilla JavaScript is mixed with JQuery (3.6.0 slim).
// This is very bad. But works. TODO: delete jQuery.

// Toggle sidebar and change elements width.
$('.sidebar-toggle-btn').click(function(){
    $(this).toggleClass("click");
    $('.sidebar').toggleClass("hide");
    $('#to-top-btn').toggleClass("wide");
    $('article').toggleClass("wide");
    if (screen.width > 1200 ) {
        $('.content').toggleClass("wide");
    }
});

// Add styling for tables.
$('table').toggleClass("table table-bordered")

// Back to top button.
var btn = $('#to-top-btn');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: "smooth"});
});

// Add marker to sidebar links.
$('.sidebar a').append('<div class="mark"></div>');

// Highlight current page link in sidebar -
// toggle marker on current page link.
var pathname = window.location.pathname;
var links = document.getElementsByTagName("a");

for (var element of links) {
    var ref = element.getAttribute('href');
    if (ref.substr(-1) !== "/") {
        ref = ref + '/';
    }
    if (ref == pathname) {
        $(element).children('.mark').css('color', '#212529');
    }
}

// Add paragraph button aside of headings
$(function() {
  return $("h1, h2, h3, h4").each(function(i, el) {
    var $el, icon, id;
    $el = $(el);
    id = $el.attr('id');
    icon = '<i class="bi bi-paragraph"></i>';
    if (id) {
      return $el.append($("<a />").addClass("header-link").attr("href", "#" + id).html(icon));
    }
  });
});