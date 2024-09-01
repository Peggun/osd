import pyhtmlify.HTMLTags.tags as tags

def index():
    return tags.html(
        tags.head(
            tags.meta(charset="UTF-8"),
            tags.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            tags.title("OSD Community"),
            tags.link(rel="stylesheet", href="../../../static/community_page/style.css")
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
                tags.h1("OSD Community"),
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
                    tags.h1("Join the OSD Community"),
                    tags.p("The OSD Community is a vibrant group of developers, designers, and enthusiasts working together to build open-source projects. Join us to collaborate, learn, and grow together."),
                    _class="content"
                ),
                tags.section(
                    tags.h2("OSD-Community Discord"),
                    tags.p("Join our active discord group to get help, request changes and much more!"),
                    tags.a("Join Us on Discord", href="https://discord.gg/wYYj32TuQW", _class="btn"),
                    _class="content"
                ),
                tags.section(
                    tags.h2("OSD GitHub"),
                    tags.p("If you made any changes and think that it is for the best for our app, please contribute to our GitHub repository"),
                    tags.a("Contribute on GitHub", href="https://github.com/Peggun/osd", _class="btn"),
                    _class="content"
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
        )
    )
