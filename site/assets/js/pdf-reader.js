const reader = document.querySelector('[data-pdf-reader]');
async function initializePdfReader() {
  const status = reader.querySelector('[data-pdf-status]');
  const pages = reader.querySelector('[data-pdf-pages]');
  const scroller = reader.querySelector('.pdf-scroll');
  const zoomLabel = reader.querySelector('[data-zoom-label]');
  let pdf, zoom = 1, rendering = false, rerender = false;
  const controls = [...reader.querySelectorAll('button')];
  const normalizeZoom = value => Math.max(.65, Math.min(reader.hasAttribute('data-fullscreen') && innerWidth < 768 ? 4 : 2.5, value));
  async function renderDocument() {
    if (rendering) { rerender = true; return; }
    rendering = true; controls.forEach(b => b.disabled = true);
    reader.setAttribute('aria-busy', 'true');
    const fragment = document.createDocumentFragment();
    try {
      for (let n = 1; n <= pdf.numPages; n++) {
        const page = await pdf.getPage(n);
        const original = page.getViewport({ scale: 1 });
        const fit = Math.max(250, scroller.clientWidth - 48) / original.width;
        const viewport = page.getViewport({ scale: fit * zoom });
        const ratio = Math.min(devicePixelRatio || 1, 2);
        const canvas = document.createElement('canvas');
        canvas.width = Math.ceil(viewport.width * ratio);
        canvas.height = Math.ceil(viewport.height * ratio);
        canvas.style.width = `${viewport.width}px`;
        canvas.style.height = `${viewport.height}px`;
        canvas.setAttribute('role', 'img');
        canvas.setAttribute('aria-label', `Page ${n} of the original CV. Open original PDF for your browser’s full document tools.`);
        await page.render({ canvasContext: canvas.getContext('2d'), viewport, transform: [ratio, 0, 0, ratio, 0, 0] }).promise;
        fragment.append(canvas);
      }
      pages.replaceChildren(fragment);
      zoomLabel.textContent = `${Math.round(zoom * 100)}%`;
      status.textContent = `${pdf.numPages} page · Original PDF`;
      reader.dataset.rendered = 'true';
    } catch (error) {
      status.textContent = 'Unable to display the PDF here. Use Open original PDF above.';
      reader.dataset.rendered = 'error';
    } finally {
      rendering = false; controls.forEach(b => b.disabled = false);
      reader.setAttribute('aria-busy', 'false');
      if (rerender) { rerender = false; renderDocument(); }
    }
  }
  try {
    const pdfjs = await import('../vendor/pdfjs/build/pdf.mjs');
    pdfjs.GlobalWorkerOptions.workerSrc = new URL('../vendor/pdfjs/build/pdf.worker.mjs', import.meta.url).href;
    pdf = await pdfjs.getDocument({
      url: reader.dataset.pdfUrl,
      standardFontDataUrl: new URL('../vendor/pdfjs/standard_fonts/', import.meta.url).href,
      cMapUrl: new URL('../vendor/pdfjs/cmaps/', import.meta.url).href,
      cMapPacked: true,
      wasmUrl: new URL('../vendor/pdfjs/wasm/', import.meta.url).href,
      isEvalSupported: false,
      verbosity: 0
    }).promise;
    reader.querySelector('[data-zoom-in]').addEventListener('click', () => { zoom = normalizeZoom(zoom + .2); renderDocument(); });
    reader.querySelector('[data-zoom-out]').addEventListener('click', () => { zoom = normalizeZoom(zoom - .2); renderDocument(); });
    reader.querySelector('[data-zoom-fit]').addEventListener('click', () => { zoom = 1; renderDocument(); });
    await renderDocument();
    let width = scroller.clientWidth;
    new ResizeObserver(() => { if (scroller.clientWidth && scroller.clientWidth !== width) { width = scroller.clientWidth; renderDocument(); } }).observe(scroller);
  } catch (error) {
    reader.setAttribute('aria-busy', 'false');
    reader.dataset.rendered = 'error';
    status.textContent = 'Unable to display the PDF here. Use Open original PDF above.';
  }
}

const desktopPdf = matchMedia('(min-width: 768px)');
let readerStarted = false;
function startWhenVisible() {
  if (reader && (desktopPdf.matches || reader.hasAttribute('data-fullscreen')) && !readerStarted) {
    readerStarted = true;
    initializePdfReader();
  }
}
desktopPdf.addEventListener('change', startWhenVisible);
startWhenVisible();
