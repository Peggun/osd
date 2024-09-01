import pyhtmlify.HTMLTags.tags as tags

def index():
    return tags.html(
        tags.head(
            tags.meta(charset="UTF-8"),
            tags.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            tags.title("Database Search"),
            tags.link(rel="stylesheet", href="../../../static/database_page/style.css"),
            tags.script(src="/static/scripts/database_page/search.js")
        ),
        tags.body(
            tags.header(
                tags.div(
                    tags.img(
                        src="../../../static/home_page/icons/osd-icon.jpeg",
                        alt="OSD Logo",
                    ),
                    class_="logo-container",
                ),
                tags.h1("OSD Database"),
                tags.nav(
                        tags.ul(
                            tags.li(tags.a("Home", href="/home")),
                            tags.li(tags.a("Getting Started", href="/docs/getting-started")),
                            tags.li(tags.a("API", href="/api")),
                            tags.li(tags.a("Contributing", href="/contributing")),
                            tags.li(tags.a("Community", href="/community")),
                        )
                    ),
            ),
            tags.main(
                tags.section(
                    tags.h1("Database Search"),
                    tags.input(type="text", id="search-bar", placeholder="Search..."),
                    tags.div(id="results", _class="results-container"),
                    _class="content"
                )
            ),
            tags.footer(
                tags.p("© 2024 OSD Project", class_="text-container"),
                tags.ul(
                    tags.li(
                        tags.a(
                            tags.img(
                                src="../../../static/home_page/icons/github-mark-white.png",
                                alt="GitHub",
                                class_="image-container",
                            ),
                            href="https://github.com/Peggun/osd",
                        )
                    ),
                    tags.li(
                        tags.a(
                            tags.img(
                                src="../../../static/home_page/icons/discord-mark-white.png",
                                alt="Discord",
                                class_="image-container",
                            ),
                            href="https://discord.gg/wYYj32TuQW",
                        )
                    ),
                    tags.li(tags.a("Contact", href="#contact")),
                    class_="horizontal-list",
                ),
                id="contact",
            ),
        )
    )