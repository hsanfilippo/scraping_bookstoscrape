from urllib.parse import urljoin
from bs4 import Tag

def get_book_title(parsed_tag: Tag , css_selector: str, output_list: list, html_attribute: str):
  tag_pointer = parsed_tag.select_one(css_selector)
  tag_desired_attribute = tag_pointer[html_attribute]
  output_list.append(tag_desired_attribute)


def get_book_price(parsed_tag: Tag , css_selector: str, output_list: list):
  tag_pointer = parsed_tag.select_one(css_selector)
  tag_text = tag_pointer.text
  output_list.append(tag_text)


def stars_to_int(stars_str: str) -> int:
  if stars_str == 'One':
    return 1
  elif stars_str == 'Two':
    return 2
  elif stars_str == 'Three':
    return 3
  elif stars_str == 'Four':
    return 4
  elif stars_str == 'Five':
    return 5
  else:
    return 0


def get_book_rating(parsed_tag: Tag , css_selector: str, output_list: list):
  tag_pointer = parsed_tag.select_one(css_selector)
  tag_classes = tag_pointer['class']
  star_count_string = tag_classes[-1]

  rating = stars_to_int(stars_str=star_count_string)
  output_list.append(str(rating))


def get_book_url(parsed_tag: Tag , css_selector: str, output_list: list, base_url: str):
  tag_pointer = parsed_tag.select_one(css_selector)
  rel_url = f'catalogue/{tag_pointer['href']}'
  book_url = f'{base_url}{rel_url}'

  output_list.append(book_url)

def get_img_url(parsed_tag: Tag , css_selector: str, output_list: list, base_url: str):
  tag_pointer = parsed_tag.select_one(css_selector)
  tag_image = tag_pointer['src']
  img_url = urljoin(base_url, tag_image)
  
  output_list.append(img_url)
