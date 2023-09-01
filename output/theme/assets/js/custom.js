jQuery( document ).ready(function( $ ) {


	"use strict";


        // Page loading animation

        $("#preloader").animate({
            'opacity': '0'
        }, 600, function(){
            setTimeout(function(){
                $("#preloader").css("visibility", "hidden").fadeOut();
            }, 300);
        });
        

        $(window).scroll(function() {
          var scroll = $(window).scrollTop();
          var box = $('.header-text').height();
          var header = $('header').height();

          if (scroll >= box - header) {
            $("header").addClass("background-header");
          } else {
            $("header").removeClass("background-header");
          }
        });

        if ($('.owl-clients').length) {
            $('.owl-clients').owlCarousel({
                loop: true,
                nav: false,
                dots: true,
                items: 1,
                margin: 30,
                autoplay: false,
                smartSpeed: 700,
                autoplayTimeout: 6000,
                responsive: {
                    0: {
                        items: 1,
                        margin: 0
                    },
                    460: {
                        items: 1,
                        margin: 0
                    },
                    576: {
                        items: 3,
                        margin: 20
                    },
                    992: {
                        items: 5,
                        margin: 30
                    }
                }
            });
        }

        if ($('.owl-banner').length) {
            $('.owl-banner').owlCarousel({
                loop: true,
                nav: true,
                dots: true,
                items: 3,
                margin: 10,
                autoplay: false,
                smartSpeed: 700,
                autoplayTimeout: 6000,
                responsive: {
                    0: {
                      items: 1,
                      margin: 0
                    },
                    460: {
                        items: 1,
                        margin: 0
                    },
                    576: {
                        items: 1,
                        margin: 10
                    },
                    992: {
                      items: 3,
                      margin: 10
                    }
                }
            });
        }
 
});



// Place the script at the end of the body
document.addEventListener('DOMContentLoaded', function() {
    var currentUrl = window.location.pathname;
    var navItems = document.querySelectorAll('.navbar-nav .nav-item');

    navItems.forEach(function(item) {
        var link = item.querySelector('.nav-link');
        if (link.getAttribute('href') === currentUrl) {
            item.classList.add('active');
        }
    });
});


/* --------------- Search ----------------  */


function searchAndAddToElement(res, targetElementId) {
    const searchInputValue = document.getElementById('search-query').value.toLowerCase();
    const searchResultElement = document.getElementById(targetElementId);
  
    if (searchInputValue.length < 2) {
        searchResultElement.innerHTML = ''; // Clear search results if input length is less than 2
        return;
    }
  
    const searchWords = searchInputValue.split(/\s+/);
    const searchResults = JSON.parse(res).filter(item => {
        const lowerTitle = item.title.toLowerCase();
        return searchWords.every(word => lowerTitle.includes(word));
    });
  
    if (searchResults.length === 0) {
        searchResultElement.innerHTML = `
            <p class="mt-4" style="color:red">Sorry, we couldn't find any results matching your search query.</p>`;
    } else {
        const resultHTML = searchResults.map(result => `
            <p class="mt-4"><a href="/${result.slug}">${result.title}</a></p>`).join('');
  
        searchResultElement.innerHTML = resultHTML;
    }
}

async function fetchArticles() {
    try {
        const response = await fetch('/articles.json/');
        if (!response.ok) {
            throw new Error(`Failed to fetch articles: ${response.status} ${response.statusText}`);
        }
        const res = await response.text();
        searchAndAddToElement(res, 'search-results'); // Replace with actual ID
    } catch (error) {
        console.error('Error fetching articles:', error);
    }
}

function initializeSearchInput() {
    const searchInput = document.getElementById('search-query');
    if (searchInput) {
        let timeoutId;

        searchInput.addEventListener('input', function () {
            clearTimeout(timeoutId);
            timeoutId = setTimeout(fetchArticles, 300); // Adjust the delay as needed
        });
    }
}

// Call the initialization function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeSearchInput);

  


