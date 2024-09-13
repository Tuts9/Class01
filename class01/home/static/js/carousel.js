let carousels = document.querySelectorAll(".js-carousel");

carousels.forEach((element) => {
  let carouselViewport = element.querySelector(".js-carousel-viewport");
  let carouselWidth = carouselViewport.clientWidth;
  let carouselRight = element.querySelector(".js-carousel-btn-right");
  let carouselLeft = element.querySelector(".js-carousel-btn-left");

  carouselRight.addEventListener("click", () => {
    let currentScroll = carouselViewport.scrollLeft;
    let nextScroll = currentScroll + carouselWidth;

    // Check if reached the end of the carousel
    if (nextScroll >= carouselViewport.scrollWidth) {
      nextScroll = 0; // Go back to the start
    }

    carouselViewport.scrollTo({
      left: nextScroll,
      behavior: "smooth"
    });
  });

  carouselLeft.addEventListener("click", () => {
    let currentScroll = carouselViewport.scrollLeft;
    let nextScroll = currentScroll - carouselWidth;

    // Check if scrolling past the beginning
    if (nextScroll < 0) {
      nextScroll = carouselViewport.scrollWidth - carouselWidth;
    } else if (nextScroll >= carouselViewport.scrollWidth) {
      nextScroll = carouselViewport.scrollWidth - carouselWidth; // Go to the end
    }

    carouselViewport.scrollTo({
      left: nextScroll,
      behavior: "smooth"
    });
  });
});