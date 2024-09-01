import pyhtmlify.HTMLTags.tags as tags

def index():
    return tags.html(
        tags.head(
            tags.meta(charset="UTF-8"),
            tags.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            tags.title("API - OSD"),
            tags.link(rel="stylesheet", href="../../../static/api_page/style.css")
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
                tags.h1("OSD - API"),
                tags.nav(
                    tags.ul(
                        tags.li(tags.a("Home", href="/home")),
                        tags.li(tags.a("Getting Started", href="/docs/getting-started")),
                        tags.li(tags.a("API Documentation", href="/docs/api-reference")),
                    )
                ),
            ),
            tags.main(
                tags.section(
                    tags.h1("OSD API"),
                    tags.p("Welcome to the OSD API. You can use our API to access a wide range of data, integrate it into your applications, and build amazing things."),
                    _class="content"
                ),
                tags.section(
                    tags.div(
                        tags.h2("Sign Up for our API."),
                        tags.p("If you don't already have a OSD Account, sign up for one today!"),
                        tags.a("Sign Up for the API", href="/sign-up", _class="btn"),
                        _class="content"
                    ),
                ),
                tags.section(
                    tags.div(
                        tags.h2("API Documentation"),
                        tags.p("If you want to learn how to use our API, please read the documentation to get you started!"),
                        tags.a("API Documentation", href="/docs/api-reference", _class="btn"),
                        _class="content"
                    ),
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