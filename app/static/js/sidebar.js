/* ==========================================
   Sidebar
   Project Zebra
========================================== */

document.addEventListener("DOMContentLoaded", () => {

    const sections = document.querySelectorAll(".sidebar-section");

    sections.forEach(section => {

        const targetId = section.dataset.target;
        const group = document.getElementById(targetId);

        if (!group) return;

        const storageKey = `sidebar-${targetId}`;

        /* Restore State */

        const savedState = localStorage.getItem(storageKey);

        if (savedState === "collapsed") {

            section.classList.add("collapsed");
            section.setAttribute("aria-expanded", "false");

            group.classList.add("collapsed");

        }

        /* Toggle */

        section.addEventListener("click", () => {

            const collapsed = section.classList.toggle("collapsed");

            group.classList.toggle("collapsed");

            section.setAttribute(
                "aria-expanded",
                (!collapsed).toString()
            );

            localStorage.setItem(
                storageKey,
                collapsed ? "collapsed" : "expanded"
            );

        });

    });

});