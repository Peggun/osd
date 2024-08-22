from inscriptis import get_text


# This runs as expected, dont know why pytest doesnt work. Add test_ at the start of function for run_tests.py to pick it up.


def html_parsing():
    html = """<div class="body"><p><strong></strong></p>
    <p><strong></strong>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa</p>
    <p>Consectetuer adipiscing elit. <a href="http://example.com/" target="_blank" class="source">Some Link</a> Aenean commodo ligula eget dolor. Aenean massa</p>
    <p>Aenean massa.Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa</p>
    <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa</p>
    <p>Consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa</p></div>"""

    text = get_text(html)
    print(text)

    assert (
        text
        == """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa

                Consectetuer adipiscing elit. Some Link Aenean commodo ligula eget dolor. Aenean massa

                Aenean massa.Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa

                Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa

                Consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa"""
    )
