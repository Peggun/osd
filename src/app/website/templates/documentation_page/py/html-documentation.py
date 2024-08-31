import pyhtmlify.HTMLTags.tags as tags


def index():
    return tags.html(
        tags.head(
            tags.meta(charset="utf-8"),
            tags.meta(name="viewport", content="width=device, initial-scale=1.0"),
            tags.title("OSD Documentation"),
            tags.link(
                rel="stylesheet", href="../../../static/documentation_page/style.css"
            ),
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
                        tags.li(tags.a("API", href="/api")),
                        tags.li(tags.a("Documentation", href="#docs", id="nav-docs")),
                        tags.li(tags.a("Support", href="#support")),
                    )
                ),
            ),
            tags.main(
                tags.section(
                    tags.h2("Introduction"),
                    tags.p(
                        "Welcome to the official documentation for the OSD project. Here you'll find detailed information about our database, API usage, and how to contribute to the project."
                    ),
                    id="intro",
                ),
                tags.section(
                    tags.h2("Documentation"),
                    tags.div(
                        tags.h3("Getting Started"),
                        tags.p(
                            "This guide will help you quickly start using OSD, including setting up your environment and using the API."
                        ),
                        tags.a("Read More", href="/docs/getting-started", class_="btn"),
                        class_="doc-section",
                    ),
                    tags.div(
                        tags.h3("API Reference"),
                        tags.p(
                            "Explore our comprehensive API documentation to effectively integrate OSD into your applications."
                        ),
                        tags.a("Explore API", href="/docs/api-reference", class_="btn"),
                        class_="doc-section",
                    ),
                    tags.div(
                        tags.h3("Contributing"),
                        tags.p(
                            "Learn how you can contribute to the OSD project, from submitting data to improving our tools."
                        ),
                        tags.a("Contact Support", href="/contributing", class_="btn"),
                        class_="doc-section",
                    ),
                    id="docs",
                ),
                tags.section(
                    tags.h2("Need Help?"),
                    tags.p(
                        "If you have any questions or need assistance, please reach out to our support team or join our community on Discord."
                    ),
                    tags.a("Contact Support", href="/support", class_="btn"),
                    id="support",
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
        ),
    )
