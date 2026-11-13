(() => {
  'use strict';

  const root = document.documentElement;
  if (!root.classList.contains('brand-intro-pending')) return;

  const art = document.querySelector('.wordmark-art');
  const veil = document.querySelector('.brand-intro-veil');
  const skip = document.querySelector('.brand-intro-skip');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  if (!art || !veil || !skip || reduced.matches || scrollY > 0 || getComputedStyle(veil).position !== 'fixed') {
    root.classList.remove('brand-intro-pending');
    return;
  }

  const duration = 3040;
  const revealAt = 1840;
  const travel = 'cubic-bezier(.64, 0, .16, 1)';
  const settle = 'cubic-bezier(.22, .7, .25, 1)';
  const link = art.closest('.wordmark');
  const stem = art.querySelector('.wordmark-stem');
  const foot = art.querySelector('.wordmark-foot');
  const e = art.querySelector('.wordmark-e');
  const o = art.querySelector('.wordmark-o');
  const controller = new AbortController();
  const { signal } = controller;
  const effects = [];
  let revealTimer, deadline;

  function finish(skipped = false) {
    if (signal.aborted) return;
    const restoreFocus = document.activeElement === skip;
    controller.abort();
    clearTimeout(revealTimer);
    clearTimeout(deadline);
    if (skipped) root.classList.add('brand-intro-skipped');
    effects.forEach(effect => effect.cancel());
    link.style.removeProperty('--wordmark-compact');
    root.classList.remove('brand-intro-pending', 'brand-intro-active', 'brand-intro-revealing');
    skip.hidden = true;
    if (restoreFocus) document.querySelector('#main').focus({ preventScroll: true });
  }

  function animate(element, frames) {
    const [lastTime, lastFrame] = frames.at(-1);
    if (lastTime < duration) frames.push([duration, lastFrame]);
    const effect = element.animate(frames.map(([ms, values]) => ({ offset: ms / duration, ...values })), {
      duration,
      fill: 'both'
    });
    effects.push(effect);
    return effect;
  }

  try {
    const stage = veil.getBoundingClientRect();
    const slot = art.getBoundingClientRect();
    const scale = Math.min(320, stage.width * .57, stage.height * .67) / slot.width;
    const x = stage.x + stage.width / 2 - (slot.x + slot.width / 2);
    const y = stage.y + stage.height / 2 - (slot.y + slot.height / 2);
    const centered = `translate3d(${x}px, ${y}px, 0) scale(${scale})`;
    // The ink of the compact mark sits 17 SVG units left of the wordmark center.
    const compactCenter = `translate3d(${x + 17 * scale}px, ${y}px, 0) scale(${scale})`;
    const readLetters = () => [foot, e, o].map(part => getComputedStyle(part).transform);
    const resting = readLetters();
    link.style.setProperty('--wordmark-compact', '1');
    const compact = readLetters();
    link.style.setProperty('--wordmark-compact', '0');
    const full = readLetters();
    link.style.removeProperty('--wordmark-compact');

    const flight = animate(art, [
      [0, { transform: compactCenter }],
      [510, { transform: compactCenter, easing: settle }],
      [1260, { transform: centered }],
      [1680, { transform: centered, easing: travel }],
      [duration, { transform: 'none' }]
    ]);
    animate(stem, [
      [0, { transform: 'scaleY(.04)', easing: settle }],
      [425, { transform: 'scaleY(1)' }]
    ]);
    animate(foot, [
      [0, { transform: 'scaleX(.04)' }],
      [80, { transform: 'scaleX(.04)', easing: settle }],
      [470, { transform: compact[0] }],
      [510, { transform: compact[0], easing: settle }],
      [1170, { transform: full[0] }],
      [1930, { transform: full[0], easing: travel }],
      [2660, { transform: resting[0] }]
    ]);
    animate(e, [
      [0, { transform: compact[1] }],
      [680, { transform: compact[1], easing: settle }],
      [1210, { transform: full[1] }],
      [1900, { transform: full[1], easing: settle }],
      [2360, { transform: resting[1] }]
    ]);
    animate(o, [
      [0, { transform: `translateY(-4px) ${compact[2]}`, opacity: 0 }],
      [110, { transform: `translateY(-4px) ${compact[2]}`, opacity: 0, easing: settle }],
      [490, { transform: compact[2], opacity: 1 }],
      [510, { transform: compact[2], opacity: 1, easing: settle }],
      [1260, { transform: full[2], opacity: 1 }],
      [1930, { transform: full[2], opacity: 1, easing: travel }],
      [2660, { transform: resting[2], opacity: 1 }]
    ]);
    animate(veil, [
      [0, { opacity: 1 }],
      [1740, { opacity: 1, easing: 'ease-in-out' }],
      [2830, { opacity: 0 }]
    ]);

    skip.addEventListener('click', () => finish(true), { signal });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape') finish(true);
    }, { signal });
    // Native navigation and scrolling remain available throughout the sequence.
    for (const type of ['pointerdown', 'focusin']) {
      document.addEventListener(type, event => {
        if (!skip.contains(event.target)) finish(true);
      }, { capture: true, signal });
    }
    for (const type of ['wheel', 'touchmove', 'scroll', 'pagehide']) {
      addEventListener(type, () => finish(true), { passive: true, signal });
    }
    addEventListener('resize', () => {
      const current = veil.getBoundingClientRect();
      if (current.width !== stage.width || current.height !== stage.height) finish(true);
    }, { passive: true, signal });
    reduced.addEventListener('change', () => finish(true), { signal });

    root.classList.replace('brand-intro-pending', 'brand-intro-active');
    skip.hidden = false;
    revealTimer = setTimeout(() => root.classList.add('brand-intro-revealing'), revealAt);
    deadline = setTimeout(() => finish(), duration + 250);
    flight.onfinish = () => finish();
  } catch {
    finish(true);
  }
})();
