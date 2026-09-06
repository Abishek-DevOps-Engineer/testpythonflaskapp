(function () {
  const key = 'site-theme';
  const toggle = document.getElementById('theme-toggle');
  function applyTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
      toggle && toggle.setAttribute('aria-pressed', 'true');
      toggle && (toggle.textContent = '☀️');
    } else {
      document.documentElement.classList.remove('dark');
      toggle && toggle.setAttribute('aria-pressed', 'false');
      toggle && (toggle.textContent = '🌙');
    }
  }

  // initialize
  try {
    const stored = localStorage.getItem(key);
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    applyTheme(stored || (prefersDark ? 'dark' : 'light'));
  } catch (e) {
    applyTheme('light');
  }

  // wire up toggle
  if (toggle) {
    toggle.addEventListener('click', function () {
      const isDark = document.documentElement.classList.contains('dark');
      const next = isDark ? 'light' : 'dark';
      try { localStorage.setItem(key, next); } catch (e) {}
      applyTheme(next);
    });
  }
})();
