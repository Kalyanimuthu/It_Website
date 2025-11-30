document.addEventListener('DOMContentLoaded', function () {
  // AOS init
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 800,
      once: true,
      offset: 120,
    });
  }

  // GSAP: subtle hero text entrance (if hero exists)
  try {
    const heroTitle = document.querySelector('.hero-animate-title');
    const heroSub = document.querySelector('.hero-animate-sub');

    if (heroTitle) {
      gsap.from(heroTitle, { y: 40, opacity: 0, duration: 1, ease: 'power3.out' });
    }
    if (heroSub) {
      gsap.from(heroSub, { y: 20, opacity: 0, duration: 1, delay: 0.3, ease: 'power3.out' });
    }

    // subtle float animation for CTAs
    document.querySelectorAll('.cta-float').forEach(el => {
      gsap.to(el, {
        y: -6, repeat: -1, yoyo: true, ease: 'sine.inOut', duration: 2
      });
    });
  } catch (e) {
    console.warn('Animations init failed', e);
  }
});
