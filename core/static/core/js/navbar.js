// mobile menu toggle
document.addEventListener('DOMContentLoaded', function () {
  const openBtn = document.getElementById('mobile-open');
  const mobileMenu = document.getElementById('mobile-menu');
  const darkToggle = document.getElementById('dark-toggle');
  const darkIcon = document.getElementById('dark-icon');

  openBtn && openBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
  });

  // update dark icon (moon/sun)
  function setDarkIcon() {
    if (document.documentElement.classList.contains('dark')) {
      darkIcon.className = 'bx bx-sun';
    } else {
      darkIcon.className = 'bx bx-moon';
    }
  }

  setDarkIcon();

  // button uses same darkmode.js toggle; keep icon in sync
  darkToggle && darkToggle.addEventListener('click', () => {
    setTimeout(setDarkIcon, 100); // small delay to allow class toggle
  });
});
