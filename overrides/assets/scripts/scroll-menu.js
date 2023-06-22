function isInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <=
            (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <=
            (window.innerWidth || document.documentElement.clientWidth)
    );
}

document$.subscribe(() => {
    setTimeout(() => {
        const activeLink = document.querySelectorAll("a.md-nav__link--active");
        const scrollWrap = document.querySelector(".md-sidebar__scrollwrap");
        scrollWrap.scrollTo(0, activeLink[0].getBoundingClientRect().top - scrollWrap.offsetHeight/2 - 100)
    }, 0);
});
