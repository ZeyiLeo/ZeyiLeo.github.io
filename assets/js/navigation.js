(() => {
 'use strict';
 const header=document.querySelector('.site-header'), nav=document.querySelector('#navigation');
 if(!header||!nav)return;
 const shell=header.querySelector('.mega-shell'), backdrop=document.querySelector('.nav-backdrop'), menu=header.querySelector('.menu-toggle');
 const triggers=[...header.querySelectorAll('[data-nav-trigger]')], panels=[...header.querySelectorAll('[data-nav-panel]')];
 const main=document.querySelector('main'), footer=document.querySelector('.site-footer');
 const mobile=matchMedia('(max-width:767px)'), reduced=matchMedia('(prefers-reduced-motion:reduce)');
 let active=null, opener=null, mode='click', closeTimer, hoverTimer, animationTimer, backdropTimer;
 function background(open){main.inert=open;footer.inert=open;document.body.classList.toggle('nav-open',open);clearTimeout(backdropTimer);if(open){backdrop.hidden=false;requestAnimationFrame(()=>{if(document.body.classList.contains('nav-open'))backdrop.classList.add('is-visible');});}else{backdrop.classList.remove('is-visible');if(reduced.matches)backdrop.hidden=true;else backdropTimer=setTimeout(()=>backdrop.hidden=true,440);}}
 function setMobile(open,restore=false){
  menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close menu':'Open menu');
  nav.inert=mobile.matches&&(!open||!!active);nav.classList.toggle('is-open',open);header.classList.toggle('menu-is-open',open);document.body.classList.toggle('menu-open',open);
  if(!open)closePanel(false,true);
  background(open||!!active);
  if(open&&!active)nav.querySelector('button:not([hidden]),a:not([hidden])')?.focus({preventScroll:true});
  else if(restore)menu.focus({preventScroll:true});
 }
 function closePanel(restore=false,immediate=false){
  clearTimeout(hoverTimer);clearTimeout(closeTimer);clearTimeout(animationTimer);
  const previous=opener;active=null;header.dataset.navState='closed';
  triggers.forEach(x=>x.setAttribute('aria-expanded','false'));shell.classList.remove('is-open');shell.inert=true;
  panels.forEach(x=>x.inert=true);
  const mobileOpen=mobile.matches&&menu.getAttribute('aria-expanded')==='true';
  nav.inert=mobile.matches&&!mobileOpen;
  background(mobileOpen);
  const finish=()=>{shell.classList.remove('is-open');shell.hidden=true;panels.forEach(x=>x.hidden=true);};
  if(immediate||reduced.matches)finish();else closeTimer=setTimeout(finish,440);
  if(restore&&previous)previous.focus({preventScroll:true});
 }
 function openPanel(id,source='click'){
  clearTimeout(closeTimer);clearTimeout(hoverTimer);clearTimeout(animationTimer);
  active=id;mode=source;opener=triggers.find(x=>x.dataset.navTrigger===id);
  triggers.forEach(x=>x.setAttribute('aria-expanded',String(x===opener)));
  shell.hidden=false;shell.inert=false;
  panels.forEach(x=>{x.hidden=x.dataset.navPanel!==id;x.inert=x.hidden;});
  if(mobile.matches&&menu.getAttribute('aria-expanded')!=='true')setMobile(true);
  nav.inert=mobile.matches;header.dataset.navState=id;background(true);
  requestAnimationFrame(()=>{if(active===id&&!shell.hidden)shell.classList.add('is-open');});
  if(source==='keyboard'||mobile.matches)panels.find(x=>!x.hidden)?.querySelector('a')?.focus({preventScroll:true});
 }
 triggers.forEach(button=>{
  button.hidden=false;button.previousElementSibling.hidden=true;
  button.addEventListener('click',e=>active===button.dataset.navTrigger?closePanel(true):openPanel(button.dataset.navTrigger,e.detail===0?'keyboard':'click'));
  button.addEventListener('keydown',e=>{if(e.key==='ArrowDown'){e.preventDefault();openPanel(button.dataset.navTrigger,'keyboard');}});
  button.addEventListener('pointerenter',e=>{clearTimeout(hoverTimer);if(e.pointerType==='mouse'&&!mobile.matches)hoverTimer=setTimeout(()=>openPanel(button.dataset.navTrigger,'hover'),130);});
  button.addEventListener('pointerleave',()=>clearTimeout(hoverTimer));
 });
 header.addEventListener('pointerenter',()=>clearTimeout(hoverTimer));
 header.addEventListener('pointerleave',()=>{clearTimeout(hoverTimer);if(active&&mode==='hover'&&!mobile.matches)hoverTimer=setTimeout(()=>closePanel(),220);});
 header.querySelector('[data-nav-close]').addEventListener('click',()=>mobile.matches?setMobile(false,true):closePanel(true));
 header.querySelector('[data-nav-back]').addEventListener('click',()=>closePanel(true));
 backdrop.addEventListener('click',()=>mobile.matches?setMobile(false,true):closePanel(true));
 menu.addEventListener('click',()=>setMobile(menu.getAttribute('aria-expanded')!=='true',true));
 header.addEventListener('click',e=>{if(e.target.closest('a')){closePanel(false,true);if(mobile.matches)setMobile(false);}});
 document.addEventListener('keydown',e=>{
  const mobileOpen=mobile.matches&&menu.getAttribute('aria-expanded')==='true';
  if(e.key==='Escape'&&(active||mobileOpen)){e.preventDefault();if(active)closePanel(true);else setMobile(false,true);return;}
  if(e.key!=='Tab'||(!active&&!mobileOpen))return;
  const items=[...header.querySelectorAll('a,button')].filter(x=>!x.hidden&&!x.closest('[hidden]')&&!x.closest('[inert]')&&x.getClientRects().length);
  const first=items[0],last=items.at(-1);
  if(e.shiftKey&&document.activeElement===first){e.preventDefault();last?.focus();}
  else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first?.focus();}
 });
 function adapt(){closePanel(false,true);menu.hidden=!mobile.matches;setMobile(false);}
 mobile.addEventListener('change',adapt);adapt();
})();
