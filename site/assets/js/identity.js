(() => {
  'use strict';
  const header = document.querySelector('.site-header');
  const mobile = matchMedia('(max-width: 767px)');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');

  const filters = document.querySelector('.filter-bar');
  if (filters) {
    filters.hidden = false;
    const cards = [...document.querySelectorAll('.project-card')];
    const status = document.querySelector('.filter-status');
    filters.addEventListener('click', e => {
      const button = e.target.closest('[data-filter]'); if (!button) return;
      filters.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
      let count = 0;
      cards.forEach(card => { card.hidden = button.dataset.filter !== 'all' && !card.dataset.categories.split(' ').includes(button.dataset.filter); if (!card.hidden) count++; });
      status.textContent = `${count} ${count === 1 ? 'project' : 'projects'} · ${button.textContent}`;
    });
  }

  const dialog = document.querySelector('.lightbox');
  let opener;
  if (typeof dialog.showModal === 'function') {
    document.querySelectorAll('[data-lightbox]').forEach(link => link.addEventListener('click', e => {
      e.preventDefault(); opener = link;
      dialog.querySelector('.lightbox-image').src = link.href;
      dialog.querySelector('.lightbox-image').alt = link.querySelector('img').alt;
      dialog.querySelector('#lightbox-title').textContent = link.dataset.title;
      dialog.querySelector('.lightbox-caption').textContent = link.dataset.caption;
      dialog.showModal(); document.body.classList.add('modal-open');
    }));
    dialog.querySelector('.lightbox-close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', e => { if (e.target === dialog) { const r = dialog.getBoundingClientRect(); if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dialog.close(); } });
    dialog.addEventListener('close', () => { document.body.classList.remove('modal-open'); opener?.focus(); });
  }

  const reveals = [...document.querySelectorAll('[data-reveal]')];
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('is-visible'); observer.unobserve(entry.target); }
    }), { threshold: .4 });
    reveals.forEach(element => observer.observe(element));
  } else reveals.forEach(element => element.classList.add('is-visible'));

  const scrollImages = [...document.querySelectorAll('[data-scroll-image]')];
  const stories = [...document.querySelectorAll('[data-story]')];
  const clamp = (value, min, max) => Math.min(max, Math.max(min, value));
  let scheduled = false;
  function updateScroll() {
    scheduled = false;
    header.classList.toggle('is-scrolled', scrollY > 8);
    scrollImages.forEach(frame => {
      const img = frame.querySelector('img');
      if (reduced.matches) { img.style.removeProperty('transform'); return; }
      const rect = frame.getBoundingClientRect();
      if (rect.top > innerHeight || rect.bottom < 0) return;
      const progress = clamp((innerHeight - rect.top) / (innerHeight + rect.height), 0, 1);
      const amplitude = mobile.matches ? 10 : 28;
      img.style.transform = `translate3d(0,${((.5 - progress) * amplitude).toFixed(2)}px,0) scale(${(1.035 - progress * .035).toFixed(4)})`;
    });
    stories.forEach(story => {
      const steps = [...story.querySelectorAll('[data-step]')];
      let active = 0, nearest = Infinity;
      steps.forEach((step, index) => {
        const rect = step.getBoundingClientRect();
        const distance = Math.abs(rect.top + rect.height / 2 - innerHeight * .5);
        if (distance < nearest) { nearest = distance; active = index; }
      });
      story.dataset.active = String(active);
      story.querySelectorAll('[data-frame]').forEach((frame, index) => {
        frame.classList.toggle('is-current', index === active);
        frame.setAttribute('aria-hidden', String(index !== active));
      });
    });
  }
  function scheduleScroll() { if (!scheduled) { scheduled = true; requestAnimationFrame(updateScroll); } }
  addEventListener('scroll', scheduleScroll, { passive: true });
  addEventListener('resize', scheduleScroll, { passive: true });
  reduced.addEventListener('change', scheduleScroll);
  updateScroll();
})();
