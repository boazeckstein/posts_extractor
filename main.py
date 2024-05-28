from utils import get_html, get_domain_name
from handle_posts import extract_posts_from_html, write_posts_to_file



PAGE_URL_1 = "https://www.phpbb.com/community/viewtopic.php?f=46&t=2159437"
PAGE_URL_2 = "https://forum.vbulletin.com/forum/vbulletin-3-8/vbulletin-3-8-questions-problems-and-troubleshooting/414325-www-vs-non-www-url-causing-site-not-to-login"


if __name__ == "__main__":
    try:

        # Process page 1
        html_content_page_1 = get_html(PAGE_URL_1)
        if not html_content_page_1:
            print(f"Failed to get HTML content from {PAGE_URL_1}")
            exit(1)
        
        posts_from_page_1 = extract_posts_from_html(
            html_content_page_1,
            ("div", "class", "postbody"),
            ("h3", None, None),
            ("div", "class", "content"),
            ("time", None, None),
            ("p", "class", "author"),
            nested_author_info=("span", "class", "responsive-hide"),
            date_format="%a %b %d, %Y %I:%M %p"

        )
        write_posts_to_file(posts_from_page_1, get_domain_name(PAGE_URL_1))
        
        # Process page 2
        html_content_page_2 = get_html(PAGE_URL_2)
        if not html_content_page_2:
            print(f"Failed to get HTML content from {PAGE_URL_2}")
            exit(1)
        
        posts_from_page_2 = extract_posts_from_html(
            html_content_page_2,
            ("div", "class", "b-post__grid-container"),
            ("h2", "class", "b-post__title js-post-title b-post__hide-when-deleted"),
            ("div", "class", "js-post__content-text restore h-wordwrap"),
            ("time", "itemprop", "dateCreated"),
            ("span", "itemprop", "name"),
            date_format="%a %d %b '%y, %I:%M%p"
        )
        write_posts_to_file(posts_from_page_2, get_domain_name(PAGE_URL_2))

        
    except Exception as e:
        print("An error occurred: ", e)
