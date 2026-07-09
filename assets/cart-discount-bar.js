/**
 * Swarakshit Discount Progress Bar
 * Handles animation of .svk-disc-fill elements after cart renders
 */
(function () {
  'use strict';

  function animateDiscountBar() {
    var fills = document.querySelectorAll('.svk-disc-fill');
    fills.forEach(function (el) {
      var pct = parseFloat(el.getAttribute('data-pct')) || 0;
      // Reset to 0 so the CSS transition fires visually
      el.style.transition = 'none';
      el.style.width = '0%';
      // Force reflow so the browser registers the reset
      el.getBoundingClientRect();
      // Re-enable transition and animate to target width
      el.style.transition = 'width 0.7s cubic-bezier(0.4, 0, 0.2, 1)';
      el.style.width = pct + '%';
    });
  }

  // Fire on initial page load (for pre-populated carts)
  document.addEventListener('DOMContentLoaded', function () {
    setTimeout(animateDiscountBar, 100);
  });

  // Fire every time the cart drawer re-renders via AJAX
  document.addEventListener('cart:rendered', function () {
    // Small delay to ensure DOM is painted
    setTimeout(animateDiscountBar, 50);
  });
})();
