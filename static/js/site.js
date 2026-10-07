/* EMM: mobile menu toggle. The site works without this file. */
document.documentElement.classList.add('js');
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.querySelector('.menu-toggle');
  var menu = document.getElementById('site-menu');
  if (!btn || !menu) return;
  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    menu.classList.toggle('is-open', !open);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && menu.classList.contains('is-open')) {
      btn.setAttribute('aria-expanded', 'false');
      menu.classList.remove('is-open');
      btn.focus();
    }
  });
});
