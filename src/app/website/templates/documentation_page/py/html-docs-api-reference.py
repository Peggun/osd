import pyhtmlify.HTMLTags.tags as tags

def index():
    return tags.html(
        tags.head(
            tags.meta(charset="utf-8"),
            tags.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            tags.title("API Reference - OSD"),
            tags.link(rel="stylesheet", href="/static/documentation_page/style.css"),
        ),
        tags.body(
            tags.header(
                tags.div(
                    tags.img(src="static/home_page/icons/osd-icon.jpeg", alt="OSD Logo"),
                    tags.nav(
                        tags.ul(
                            tags.li(tags.a("Home", href="/home")),
                            tags.li(tags.a("Getting Started", href="/docs/getting-started")),
                            tags.li(tags.a("Contributing", href="/contributing")),
                        )
                    ),
                    class_="top-bar"
                )
            ),
            tags.main(
                tags.section(
                    tags.h1("API Reference"),
                    tags.p("Detailed API documentation for OSD."),
                    tags.div(
                        tags.h2("Endpoints"),
                        tags.p("Description of various API endpoints..."),
                    ),
                    tags.div(
                        tags.h2("Authentication"),
                        tags.p("Details on how to authenticate requests..."),
                    )
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
