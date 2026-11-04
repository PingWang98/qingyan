document.addEventListener('DOMContentLoaded', () => {
  const progressBar = document.getElementById('progress-bar');

  // 1. View Tabs Switcher (二创人物志 vs 图文剧情)
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
      window.scrollTo({ top: document.querySelector('.hero').offsetHeight - 60, behavior: 'smooth' });
    });
  });

  // 2. Scroll Progress & Active Chapter Spy
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
      link.classList.toggle('active', link.getAttribute('href') === `#${currentId}`);
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
});
