import pyhtmlify.HTMLTags.tags as tags


def index():
    return tags.html(
        tags.head(
            tags.meta(charset="utf-8"),
            tags.meta(content="width=device-width, initial-scale=1.0", name="viewport"),
            tags.title("OSD - Open Source Data"),
            tags.link(href="../../../static/home_page/style.css", rel="stylesheet"),
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
                tags.h1("OSD"),
                tags.div(
                    tags.nav(
                        tags.ul(
                            tags.li(
                                tags.a("Database", href="/database", id="nav-database")
                            ),
                            tags.li(
                                tags.a("Features", href="#features", id="nav-features")
                            ),
                            tags.li(
                                tags.a(
                                    "Documentation",
                                    href="/docs",
                                    id="nav-documentation",
                                )
                            ),
                            tags.li(
                                tags.a(
                                    "Community", href="/community", id="nav-community"
                                )
                            ),
                            tags.li(tags.a("News", href="#news", id="nav-news")),
                            tags.li(
                                tags.a("Contact", href="#contact", id="nav-contact")
                            ),
                            tags.li(tags.a("API", href="/api", id="nav-api")),
                        )
                    ),
                    id="buttons",
                ),
            ),
            tags.main(
                tags.section(
                    tags.h2("Welcome to OSD"),
                    tags.p(
                        "Your go-to resource for open-source data. Explore plenty of different data types and datasets to suit your need. Can't find what your looking for, please request it to our Discord where our team will try our best to add your data."
                    ),
                    tags.if_tag(
                        "show_get_started",
                        tags.div(
                            tags.button(
                                "Get Started", id="get-started-button", class_="btn"
                            )
                        ),
                    ),
                    id="hero",
                ),
                tags.section(
                    tags.h2("Key Features"),
                    tags.div(
                        tags.h3("API"),
                        tags.p(
                            "Use the offical API of osd to pull any type of data! However, you will need to sign up for an api key to use for pulling data, but thats easy to do."
                        ),
                        class_="feature",
                    ),
                    tags.div(
                        tags.h3("A BIG database"),
                        tags.p(
                            "The osd database is full of data from contributors and suggestions from our discord. You too could request to add some data, or add it yourself through contributing to our project!"
                        ),
                        class_="feature",
                    ),
                    id="features",
                ),
                tags.section(
                    tags.h2("Recent Updates"),
                    tags.p(
                        "Stay updated with the latest news and releases of the OSD Database, OSD API, and pyhtmlify."
                    ),
                    tags.div(
                        tags.h3("Website development is a go!"),
                        tags.p(
                            "Development of the osd website has offically started! The website will go up and running with the first stable release. (Which is hopefully soon!)"
                        ),
                    ),
                    tags.div(
                        tags.h3("Pyhtmlify Pre-Release 0.1.7a1"),
                        tags.p(
                            "pyhtmlify 0.1.7a1 just got released! It features new improvements to the code side of things, and bug fixes, along with more tag support."
                        ),
                    ),
                    id="news",
                ),
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
            tags.script(src="/static/scripts/home_page/get_started.js"),
            tags.div(class_="overlay"),
        ),
    )
