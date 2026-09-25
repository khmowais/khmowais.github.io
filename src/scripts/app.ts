const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

function mobileNav() {
  const toggle = document.getElementById("nav-toggle");
  const panel = document.getElementById("nav-links");
  if (!toggle || !panel) return;
  toggle.addEventListener("click", () => {
    const open = panel.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Toggle menu");
  });
  panel.addEventListener("click", (e) => {
    if ((e.target as HTMLElement).tagName === "A") panel.classList.remove("open");
  });
}

function currentNav() {
  const path = window.location.pathname.replace(/\/$/, "") || "/";
  document.querySelectorAll(".nav-links a").forEach((a) => {
    const href = a.getAttribute("href") || "/";
    const clean = href.replace(/\/$/, "") || "/";
    if (clean === path) a.setAttribute("aria-current", "page");
  });
}

function reveals() {
  if (reduced) return;
  const els = document.querySelectorAll("[data-reveal]");
  if (!els.length || !("IntersectionObserver" in window)) return;
  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      }
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
  );
  els.forEach((el, i) => {
    if (i < 8) el.classList.add(`d${(i % 4) + 1}`);
    io.observe(el);
  });
}

function readingProgress() {
  const bar = document.querySelector<HTMLElement>(".progress-track .bar");
  if (!bar) return;
  let ticking = false;
  const update = () => {
    const doc = document.documentElement;
    const max = doc.scrollHeight - doc.clientHeight;
    bar.style.width = `${max > 0 ? (window.scrollY / max) * 100 : 0}%`;
    ticking = false;
  };
  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(update);
      }
    },
    { passive: true }
  );
  update();
}

document.addEventListener("DOMContentLoaded", () => {
  mobileNav();
  currentNav();
  reveals();
  readingProgress();
});