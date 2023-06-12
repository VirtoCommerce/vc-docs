function isInViewport (el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

document$.subscribe(() => {
    setTimeout(() => {
        const activeLink = document.querySelectorAll("a.md-nav__link--active");
        if (!isInViewport(activeLink[0])) {
            const scrollWrap = document.querySelector('.md-sidebar__scrollwrap')
            scrollWrap.scrollTo({top: activeLink[0].getBoundingClientRect().top - scrollWrap.offsetHeight, behavior: 'smooth'})
        }
    }, 0);
})



