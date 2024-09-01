import pyhtmlify.HTMLTags.tags as tags

def index():
    return tags.html(
        tags.head(
            tags.meta(charset="UTF-8"),
            tags.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            tags.title("Contributing - OSD"),
            tags.link(rel="stylesheet", href="../../../static/documentation_page/style.css"),
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
                tags.h1("Contributing"),
                tags.nav(
                    tags.ul(
                        tags.li(tags.a("Home", href="/home")),
                        tags.li(tags.a("Getting Started", href="/docs/getting-started")),
                        tags.li(tags.a("API Reference", href="/docs/api-reference")),
                    )
                ),
            ),
            tags.main(
                tags.section(
                    tags.h1("Contributing"),
                    tags.p("Thank you for your interest in contributing to OSD! Your help is appreciated, whether you are reporting bugs, suggesting features, or submitting pull requests."),
                    tags.div(
                        tags.div(
                            tags.h2("How to Contribute"),
                            tags.p("Learn the different ways you can contribute to the OSD project."),
                            class_="contributing-box"
                        ),
                        tags.div(
                            tags.h2("Code of Conduct"),
                            tags.p("Please read and follow our code of conduct to ensure a welcoming environment for everyone."),
                            class_="contributing-box"
                        ),
                        tags.div(
                            tags.h2("Submitting Pull Requests"),
                            tags.p("Guidelines on how to submit pull requests to the project."),
                            class_="contributing-box"
                        ),
                        class_="contributing-sections"
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