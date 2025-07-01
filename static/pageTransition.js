// pageTransition.js

// Zoom out on link click
document.querySelectorAll("a").forEach(link => {
  link.addEventListener("click", function (e) {
    const href = link.getAttribute("href");

    // Ignore external or anchor links
    if (!href || href.startsWith("#") || href.startsWith("javascript:")) return;

    e.preventDefault();
    document.body.classList.remove("zoom-in");
    document.body.classList.add("zoom-out");

    setTimeout(() => {
      window.location.href = href;
    }, 400); // match the CSS transition time
  });
});

// Zoom in on page load
window.addEventListener("pageshow", function () {
  document.body.classList.add("zoom-in");
});