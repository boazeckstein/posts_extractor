import re


def extract_html_elements(html: str, tag: str, attribute_type: str = None, attribute_value: str = None) -> list[str]:
    tag_open = f"<{tag}"
    tag_close = f"</{tag}>"

    def find_closing_tag_position(html: str, start_pos: int) -> int:
        stack = []
        pos = start_pos

        while pos < len(html):
            next_open_pos = html.find(tag_open, pos)
            next_close_pos = html.find(tag_close, pos)

            if next_open_pos == -1 and next_close_pos == -1:
                break

            if next_open_pos != -1 and (next_open_pos < next_close_pos or next_close_pos == -1):
                stack.append(next_open_pos)
                pos = next_open_pos + len(tag_open)
            elif next_close_pos != -1:
                stack.pop()
                if not stack:
                    return next_close_pos + len(tag_close)
                pos = next_close_pos + len(tag_close)

        return -1

    def extract_tags(html: str, tag: str, attribute_type: str, attribute_value: str) -> list[str]:
        results = []
        pos = 0

        while pos < len(html):
            if attribute_type and attribute_value:
                start_tag_pos = html.find(f'<{tag} {attribute_type}="{attribute_value}"', pos)
            else:
                start_tag_pos = html.find(tag_open, pos)

            if start_tag_pos == -1:
                break

            end_tag_pos = find_closing_tag_position(html, start_tag_pos)
            if end_tag_pos == -1:
                break

            content = html[start_tag_pos:end_tag_pos]
            if attribute_type and attribute_value:
                if re.search(rf'<{tag} {attribute_type}="{attribute_value}"', content):
                    results.append(content)
            else:
                results.append(content)
            pos = end_tag_pos

        return results

    return extract_tags(html, tag, attribute_type, attribute_value)


def strip_html_tags(html: str) -> str:
    text_only = re.sub(r"<.*?>", "", html, flags=re.DOTALL)
    text_only = re.sub(r"&.*?;", "", text_only)
    text_only = re.sub(r"\s+", " ", text_only).strip()
    text_only = re.sub(r"\bby\b", "", text_only, flags=re.IGNORECASE).strip()

    return text_only

