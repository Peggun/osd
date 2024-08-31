import pyhtmlify.HTMLTags.tags as tags


def index():
    return tags.html(
        tags.head(
            tags.meta(charset="UTF-8"),
            tags.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            tags.title("Getting Started - OSD"),
            tags.link(rel="stylesheet", href="../../../static/home_page/style.css"),
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
                tags.h1("OSD Documentation"),
                tags.nav(
                    tags.ul(
                        tags.li(tags.a("Home", href="/home")),
                        tags.li(tags.a("Database", href="/database")),
                        tags.li(tags.a("API", href="/api-reference")),
                        tags.li(tags.a("Documentation", href="#docs", id="nav-docs")),
                        tags.li(tags.a("Support", href="#support")),
                    )
                ),
            ),
            tags.main(
                tags.section(
                    tags.h1("Getting Started"),
                    tags.p("Welcome to the OSD documentation. This guide will help you get started with OSD quickly and easily."),
                    tags.div(
                        tags.div(
                            tags.h2("Step 1: Installation"),
                            tags.p("Instructions on how to install OSD on your system."),
                            class_="guide-box"
                        ),
                        tags.div(
                            tags.h2("Step 2: Basic Usage"),
                            tags.p("Learn the basics of using OSD."),
                            class_="guide-box"
                        ),
                        tags.div(
                            tags.h2("Step 3: Configuration"),
                            tags.p("How to configure OSD to fit your needs."),
                            class_="guide-box"
                        ),
                        class_="guide-sections"
                    )
                ),
                class_="content"
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
