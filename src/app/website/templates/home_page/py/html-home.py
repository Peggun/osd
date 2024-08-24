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
                    tags.img(src="../../../static/home_page/icons/osd-icon.jpeg", alt="OSD Logo"),
                    class_="logo-container",
                ),
                tags.h1("OSD"),
                tags.nav(
                    tags.ul(
                        tags.li(tags.a("Database", href="#database")),
                        tags.li(tags.a("Features", href="#features")),
                        tags.li(tags.a("Documentation", href="#documentation")),
                        tags.li(tags.a("Community", href="#community")),
                        tags.li(tags.a("News", href="#news")),
                        tags.li(tags.a("Contact", href="#contact")),
                    )
                ),
            ),
            tags.main(
                tags.section(
                    tags.h2("Welcome to OSD"),
                    tags.p("Your go-to resource for open-source data."),
                    tags.a("Get Started", class_="btn", href="#get-started"),
                    id="hero"
                ),
                tags.section(
                    tags.h2("Key Features"),
                    tags.div(
                        tags.h3("Feature 1"),
                        tags.p("Description here."),
                        class_="feature",
                    ),
                    tags.div(
                        tags.h3("Feature 2"),
                        tags.p("Description here."),
                        class_="feature",
                    ),
                    id="features",
                ),
                tags.section(
                    tags.h2("Recent Updates"),
                    tags.p("Stay updated with the latest news and releases"),
                    id="news",
                )
            ),
            tags.footer(
                tags.p("© 2024 OSD Project", class_="text-container"),
                tags.ul(
                    tags.li(tags.a(tags.img(src="../../../static/home_page/icons/github-mark-white.png", alt="GitHub", class_="image-container"), href="https://github.com/Peggun/osd")),
                    tags.li(tags.a(tags.img(src="../../../static/home_page/icons/discord-mark-white.png", alt="Discord", class_="image-container"), href="https://discord.gg/wYYj32TuQW")),
                    tags.li(tags.a("Contact", href="#contact")),
                    class_="horizontal-list"
                )
            )
        )
    )