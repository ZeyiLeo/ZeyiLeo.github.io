(() => {
  'use strict';
  const root = document.documentElement;
  const themeButton = document.querySelector('.theme-toggle');
  const themeLabel = () => themeButton.setAttribute('aria-label', `Switch to ${root.dataset.theme === 'dark' ? 'light' : 'dark'} theme`);
  themeButton.hidden = false;
  themeLabel();
  themeButton.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('zeyileo-theme', root.dataset.theme); } catch (_) { /* Theme still works when storage is unavailable. */ }
    themeLabel();
  });

  const menu = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('#navigation');
  const mobile = matchMedia('(max-width: 900px)');
  const closeMenu = () => { navigation.classList.remove('is-open'); menu.setAttribute('aria-expanded', 'false'); };
  const adaptMenu = () => { menu.hidden = !mobile.matches; closeMenu(); };
  adaptMenu();
  mobile.addEventListener('change', adaptMenu);
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open)); navigation.classList.toggle('is-open', open);
  });
  navigation.addEventListener('click', e => { if (e.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { closeMenu(); menu.focus(); }
  });
  document.addEventListener('click', e => { if (!e.target.closest('.site-header')) closeMenu(); });

  const filters = document.querySelector('.filter-bar');
  if (filters) {
    filters.hidden = false;
    const cards = [...document.querySelectorAll('.project-card')];
    const status = document.querySelector('.filter-status');
    filters.addEventListener('click', e => {
      const button = e.target.closest('[data-filter]'); if (!button) return;
      const category = button.dataset.filter;
      filters.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
      let count = 0;
      cards.forEach(card => { card.hidden = category !== 'all' && !card.dataset.categories.split(' ').includes(category); if (!card.hidden) count++; });
      status.textContent = `${count} ${count === 1 ? 'project' : 'projects'} · ${button.textContent}`;
    });
  }

  const dialog = document.querySelector('.lightbox');
  let opener;
  if (typeof dialog.showModal === 'function') {
    document.querySelectorAll('[data-lightbox]').forEach(link => link.addEventListener('click', e => {
      e.preventDefault(); opener = link;
      const img = link.querySelector('img');
      dialog.querySelector('.lightbox-image').src = link.href;
      dialog.querySelector('.lightbox-image').alt = img.alt;
      dialog.querySelector('#lightbox-title').textContent = link.dataset.title;
      dialog.querySelector('.lightbox-caption').textContent = link.dataset.caption;
      dialog.showModal(); document.body.classList.add('modal-open');
    }));
    dialog.querySelector('.lightbox-close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', e => { if (e.target === dialog) { const r = dialog.getBoundingClientRect(); if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dialog.close(); } });
    dialog.addEventListener('close', () => { document.body.classList.remove('modal-open'); opener?.focus(); });
  }
})();
