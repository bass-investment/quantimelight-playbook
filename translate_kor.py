import os
import tqdm
from bs4 import BeautifulSoup
from googletrans import Translator


def translate_rich_text(html_content, src='en', dest='ko'):
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html_content, 'html.parser')

    # 번역기 초기화
    translator = Translator()

    # rich text 요소들 가져오기 (예: <p>, <span>, <div> 등)
    rich_text_tags = ['p', 'span', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'em', 'th', 'strong', 'td']

    for tag in rich_text_tags:
        for element in soup.find_all(tag):
            if element.string:  # 요소에 문자열이 있는 경우에만 번역
                try:
                    translated = translator.translate(element.string, src=src, dest=dest)
                except TypeError:
                    continue
                except Exception as e:
                    # print("Error : ", e)
                    continue
                element.string.replace_with(translated.text)

    return str(soup)


if not os.path.exists('src_kor'):
    os.mkdir('src_kor')

for html_file in tqdm.tqdm(os.listdir('src')[60:]):
    if not html_file.endswith('html'):
        continue

    # 예제 HTML 파일 읽기
    with open('src/' + html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # rich text 번역
    translated_html = translate_rich_text(html_content)

    # 번역된 HTML 파일 저장
    with open(f'src_kor/{html_file}', 'w', encoding='utf-8') as file:
        file.write(translated_html)

    print(html_file, " 번역 완료")
