const menu_button = document.querySelector('.menu\-button'),
    up_button = document.querySelector('.back\-to\-top'),
    menu = document.querySelector('.menu'),
    menu_box = document.querySelector('.menu\-box'),
    menuWidth = menu.offsetWidth,
    content = document.querySelector('.content'),
    divForTable = document.createElement('div'),
    burgerMenu = document.querySelector('.burger'),
    burgerContent = document.querySelector('.burger\-content');

let buttonClicked = false,
    menu_buttonPosition = menu_button.getBoundingClientRect().left,
    uls = content.getElementsByTagName('ul'),
    ols = content.getElementsByTagName('ol'),
    tables = content.getElementsByTagName('table'),
    documentWidth = document.body.clientWidth;

    // Indent left fot "burger-content"
    burgerContent.style.left = -documentWidth + 'px';

// Back to top button
(function() {
  'use strict';

function trackScroll() {
    var scrolled = window.pageYOffset;
    var coords = 300;

    if (scrolled > coords) {
      goTopBtn.classList.add('back-to-top-show');
    }
    if (scrolled < coords) {
      goTopBtn.classList.remove('back-to-top-show');
    }
  }

function backToTop() {
    if (window.pageYOffset > 0) {
      window.scrollTo({ top: 0,
                        behavior: "smooth"
                        });
    }
  }

var goTopBtn = document.querySelector('.back-to-top');

document.addEventListener('DOMContentLoaded', trackScroll);
window.addEventListener('scroll', trackScroll);
goTopBtn.addEventListener('click', backToTop);

})();

// Hide/Show left sidebar
menu_button.addEventListener('click', function(){
    if (buttonClicked === false) {
        menu.style.marginLeft = -menuWidth + 'px';
        menu_box.style.marginLeft = -menuWidth + 'px';
        menu_button.style.left = menu_buttonPosition - menuWidth + 'px';
        up_button.style.left = menu_buttonPosition - menuWidth + 'px';
        content.style.width = 100 + '%';
        buttonClicked = true;
    } else {
        menu.style.marginLeft = 0;
        menu_box.style.marginLeft = 0;
        menu_button.style.left = menu_buttonPosition + 'px';
        up_button.style.left = menu_buttonPosition + 'px';
        content.style.width = document.documentElement.clientWidth - menu.clientWidth -1 + 'px';
        buttonClicked = false;
    }
})

// Creating div for tables, ol, ul
// and placing content into them
for (let i=0; i<tables.length; i++) {
    tables[i].insertAdjacentHTML('afterend', '<div class="tables" id="tables'+i+'"></div>');
    let tableCount = document.querySelector('#tables'+i+'');
    tableCount.appendChild(tables[i]);
}
for (let i=0; i<ols.length; i++) {
    ols[i].insertAdjacentHTML('afterend', '<div class="ols" id="ols'+i+'"></div>');
    let tableCount = document.querySelector('#ols'+i+'');
    tableCount.appendChild(ols[i]);
}
for (let i=0; i<uls.length; i++) {
    uls[i].insertAdjacentHTML('afterend', '<div class="uls" id="uls'+i+'"></div>');
    let tableCount = document.querySelector('#uls'+i+'');
    tableCount.appendChild(uls[i]);
}

// Burger menu
let clicked = false,
    pres = document.getElementsByTagName('pre'),
    time_out = 200;

function burderShow(show) {burgerContent.style.display = "'" + show + "'"}

burgerMenu.addEventListener('click', function() {
    if (clicked == false) {
        burgerContent.style.transition = 'all 0.2s ease 0s'
        burgerContent.style.left = 0;
        document.body.classList.add('hide');
        for (i in pres) {
            if (pres[i].tagName == 'PRE') {
                pres[i].classList.add('hide');
            }
        }
        clicked = true;
    } else {
        burgerContent.style.left = -documentWidth + 'px'
        setTimeout(burderShow('none'), time_out)
        document.body.classList.remove('hide');
        for (i in pres) {
            if (pres[i].tagName == 'PRE') {
                pres[i].classList.remove('hide');
            }
        }
        clicked = false
    }
})

// Resizing "content" block
content.style.width = document.documentElement.clientWidth - menu.clientWidth -1 + 'px';
window.addEventListener('resize', function() {
    documentWidth = document.body.clientWidth;
    content.style.width = document.documentElement.clientWidth - menu.clientWidth -1 + 'px';
})
