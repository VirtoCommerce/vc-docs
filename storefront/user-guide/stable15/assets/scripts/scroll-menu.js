// Centers the active primary-nav item in the sidebar viewport on every page render.
// Stock mkdocs-material 9.5.4 does not auto-scroll the sidebar to the active page,
// so deeply-nested entries land outside the visible area on first load.
document$.subscribe(() => {
    requestAnimationFrame(() => {
        const sidebar = document.querySelector(
            '[data-md-component="sidebar"][data-md-type="navigation"]'
        );
        if (!sidebar) return;

        const scrollWrap = sidebar.querySelector(".md-sidebar__scrollwrap");
        if (!scrollWrap) return;

        // md-nav__link--active is also applied to in-page TOC anchors injected
        // inside the current page's <li>. Exclude those — we want the nav-tree page link.
        const activeLinks = Array.from(
            scrollWrap.querySelectorAll("a.md-nav__link--active")
        ).filter((a) => !a.closest('[data-md-component="toc"]'));
        const target = activeLinks[activeLinks.length - 1];
        if (!target) return;

        const wrapRect = scrollWrap.getBoundingClientRect();
        const targetRect = target.getBoundingClientRect();

        if (
            targetRect.top >= wrapRect.top &&
            targetRect.bottom <= wrapRect.bottom
        ) {
            return;
        }

        const offsetTop =
            targetRect.top - wrapRect.top + scrollWrap.scrollTop;
        scrollWrap.scrollTo({
            top: offsetTop - scrollWrap.clientHeight / 2 + targetRect.height / 2,
            behavior: "auto",
        });
    });
});
