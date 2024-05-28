from html_extractor import extract_html_elements, strip_html_tags
from utils import reformat_date
from post import Post


def extract_posts_from_html(html_content: str, post_container_info: tuple[str, str, str], title_info: tuple[str, str, str], text_info: tuple[str, str, str], published_info: tuple[str, str, str],
                             author_info: tuple[str, str, str], nested_author_info: tuple[str, str, str]=None, date_format: str=None) -> list[Post]:
    posts = []
    post_container_tag, post_container_attr, post_container_class = post_container_info
    title_tag, title_attr, title_class = title_info
    text_tag, text_attr, text_class = text_info
    published_tag, published_attr, published_class = published_info
    author_tag, author_attr, author_class = author_info

    post_containers = extract_html_elements(html_content, post_container_tag, post_container_attr, post_container_class)
    
    for p in post_containers:
        title_html = extract_html_elements(p, title_tag, title_attr, title_class)
        title_text = strip_html_tags(title_html[0]) if title_html else "No title found"
        
        text_html = extract_html_elements(p, text_tag, text_attr, text_class)
        text_text = strip_html_tags(text_html[0]) if text_html else "No content found"
        
        published_html = extract_html_elements(p, published_tag, published_attr, published_class)
        published_text = reformat_date(strip_html_tags(published_html[0]), input_format=date_format) if published_html else "No date found"
        
        author_html = extract_html_elements(p, author_tag, author_attr, author_class)
        if author_html:
            if nested_author_info:
                nested_tag, nested_attr, nested_class = nested_author_info
                inner_author_html = extract_html_elements(author_html[0], nested_tag, nested_attr, nested_class)
                if inner_author_html:
                    author_text = strip_html_tags(inner_author_html[0])
                else:
                    author_text = "No author found in nested element"
            else:
                author_text = strip_html_tags(author_html[0])
        else:
            author_text = "No author found"
        
        post = Post(title_text, text_text, published_text, author_text)
        posts.append(post)
    
    return posts


def write_posts_to_file(posts_objects: list, filename: str) -> None:
    with open(filename, "w") as file:
        for index, post in enumerate(posts_objects, start=1):
            file.write(f"{index}. {post.to_json()}\n\n")
