document.addEventListener('DOMContentLoaded', () => {
  const progressBar = document.getElementById('progress-bar');

  // 1. View Tabs Switcher (图文剧情 vs 二创人物志 vs 方法论)
  const tabBtns = document.querySelectorAll('[data-view-target]');
  const views = document.querySelectorAll('.view-section');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-view-target');
      tabBtns.forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-view-target') === targetId);
      });
      views.forEach(v => {
        v.classList.toggle('active', v.id === targetId);
      });
      const heroEl = document.querySelector('.hero');
      const navOffset = window.innerWidth <= 640 ? 52 : 58;
      window.scrollTo({ top: Math.max(0, heroEl.offsetHeight - navOffset), behavior: 'smooth' });
    });
  });

  // 2. Scroll Progress & Active Chapter Spy (with Mobile Horizontal TOC Auto-Scroll)
  let lastActiveLink = null;
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    if (progressBar) progressBar.style.width = `${pct}%`;

    const activeView = document.querySelector('.view-section.active');
    if (!activeView) return;

    const chapters = activeView.querySelectorAll('.chapter-block');
    const tocLinks = activeView.querySelectorAll('.toc-link');

    let currentId = '';
    chapters.forEach(sec => {
      const top = sec.offsetTop - 160;
      if (scrollTop >= top) {
        currentId = sec.getAttribute('id');
      }
    });

    tocLinks.forEach(link => {
      const isActive = link.getAttribute('href') === `#${currentId}`;
      link.classList.toggle('active', isActive);
      if (isActive && link !== lastActiveLink) {
        lastActiveLink = link;
        const sidebar = link.closest('.toc-sidebar');
        if (sidebar && window.innerWidth <= 960) {
          const linkLeft = link.offsetLeft - sidebar.offsetWidth / 2 + link.offsetWidth / 2;
          sidebar.scrollTo({ left: Math.max(0, linkLeft), behavior: 'smooth' });
        }
      }
    });
  }, { passive: true });

  // 3. Font Size Switcher
  const sizeBtns = document.querySelectorAll('[data-size]');
  sizeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      sizeBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.body.style.fontSize = btn.getAttribute('data-size');
    });
  });

  // 4. Tap-to-Zoom Lightbox for Mobile & Desktop Stills
  const lightbox = document.createElement('div');
  lightbox.className = 'lightbox-overlay';
  lightbox.innerHTML = `
    <button class="lightbox-close" aria-label="关闭">&times;</button>
    <img src="" alt="" />
    <div class="lightbox-caption"></div>
  `;
  document.body.appendChild(lightbox);

  const lbImg = lightbox.querySelector('img');
  const lbCap = lightbox.querySelector('.lightbox-caption');

  document.querySelectorAll('.still-card').forEach(card => {
    card.addEventListener('click', () => {
      const img = card.querySelector('img');
      const cap = card.querySelector('.still-caption');
      if (!img) return;
      lbImg.src = img.src;
      lbImg.alt = img.alt;
      lbCap.innerHTML = cap ? cap.innerHTML : '';
      lightbox.classList.add('open');
    });
  });

  lightbox.addEventListener('click', () => {
    lightbox.classList.remove('open');
  });
});
