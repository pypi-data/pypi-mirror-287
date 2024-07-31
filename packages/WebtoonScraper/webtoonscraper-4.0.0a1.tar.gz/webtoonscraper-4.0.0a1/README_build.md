**Check latest version [here](https://github.com/ilotoki0804/WebtoonScraper).**
# WebtoonScraper

[![GitHub Downloads (all assets, latest release)](https://img.shields.io/github/downloads/ilotoki0804/WebtoonScraper/latest/total?label=executable%20downloads)](https://github.com/ilotoki0804/WebtoonScraper/releases)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/WebtoonScraper)](https://pypi.org/project/WebtoonScraper/)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Filotoki0804%2FWebtoonScraper&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://github.com/ilotoki0804/WebtoonScraper)
[![Sponsoring](https://img.shields.io/badge/Sponsoring-Toss-blue?logo=GitHub%20Sponsors&logoColor=white)](https://toss.me/ilotoki)

**English documentation is available [here](https://github.com/ilotoki0804/WebtoonScraper/blob/master/docs/README_eng.md).**

최대 규모 오픈 소스 웹툰 스크래퍼입니다.

**네이버 웹툰(베스트 도전, 도전만화 포함), webtoons.com, 버프툰, 네이버 포스트, 네이버 게임, 레진 코믹스, 카카오페이지, 네이버 블로그, 티스토리, 카카오 웹툰**을 지원하고, 계속해서 지원 목록을 확대할 계획입니다.

저작권과 책임에 대한 내용을 더욱 자세히 알고 싶다면 [이 문서](https://github.com/ilotoki0804/WebtoonScraper/blob/master/docs/copyright.md)를 참고해 주세요.

## 실행 파일로 이용하기

이 패키지는 Windows, macOS, Linux에서 실행 파일 형태로 사용할 수 있습니다.

1. [릴리즈 페이지](https://github.com/ilotoki0804/WebtoonScraper/releases)로 가세요.
1. 최신 릴리즈 아래에서 자신의 운영 체제와 일치하는 이름이 적힌 zip 파일을 클릭해 다운로드하세요.
1. zip파일을 풀고 사용하세요.

> [!WARNING]
> 윈도우의 경우 "Windows의 PC 보호" 창이 뜨면서 실행이 안 될 수 있습니다. 그런 경우에는 `추가 정보`(왼쪽 중간에 있습니다.)를 클릭하고 `실행`을 누르세요.

## Installation

1. 파이썬(3.10 이상, 최신 버전 권장)을 설치합니다. 꼭 PATH에 파이썬이 포함되도록 설치하세요.
1. 터미널에서 다음과 같은 명령어를 실행합니다.

    ```console
    pip install -U WebtoonScraper[full]
    ```

잘 설치되었는지를 확인하려면 다음의 명령어를 사용해 보세요.

```console
webtoon --version
```

> 만약 `webtoon` 명령어가 잘 실행되지 않는다면 다음의 코드를 사용해 보세요.
>
> ```console
> python -m WebtoonScraper --version
> ```
>
> 자신의 환경에 따라 `python` 대신 `python3`나 `py -3.12`과 같은 코드를 적절히 사용해야 할 수 있습니다.

아래와 같거나 비슷한 메시지가 출력된다면 제대로 설치된 것입니다.

```console
WebtoonScraper 3.2.2 of Python 3.11.4 ... at ...
✅ All extra dependencies are installed!
```

> 다음과 같은 경고 메시지가 나올 수 있습니다.
>
> ```console
> WebtoonScraper 3.2.2 of Python 3.11.4 ... at ...
> ⚠️  Extra dependencies 'kakao_webtoon', 'lezhin_comics', 'naver_post' are not installed.
> You won't be able to download webtoons from following platforms: 'Kakao Webtoon', 'Lezhin Comics (partially)', 'Naver Post'.
> ```
>
> 이 경우 표시된 플랫폼들(이 오류 메시지의 경우 카카오 웹툰, 레진 코믹스(부분적), 네이버 포스트)에 대한 추가적인 의존성이 설치되지 않는 것인데, 따라서 이 플랫폼들의 웹툰을 다운로드할 수 없게 됩니다.
>
> 다음과 같이 명령어를 짜면 모든 플랫폼에서 웹툰을 다운로드할 수 있습니다.
>
> ```console
> pip install -U WebtoonScraper[full]
> ```

## How to use

대부분의 웹툰은 다음과 같이 터미널에 `webtoon download`를 치고 큰따옴표로 감싼 URL을 뒤에 위치하면 작동합니다.

```console
webtoon download "https://comic.naver.com/webtoon/list?titleId=819217"
```

만약 더 많은 WebtoonScraper의 기능(범위 설정 다운로드, 모아서 보기, 다운로드할 디렉토리 설정, 에피소드 리스팅, 파이썬으로 사용 등)을 알고 싶거나 위에서 소개한 방식으로는 잘 작동하지 않는 경우(특히 버프툰, 레진코믹스의 경우 추가적인 설정이 필수적입니다.)에는 [`사용 방법` 문서](https://github.com/ilotoki0804/WebtoonScraper/blob/master/docs/how_to_use.md)를 참고해 주세요.

## 다운로드 가능한 웹툰/에피소드의 종류

[다운로드 가능한 웹툰/에피소드의 종류 문서](https://github.com/ilotoki0804/WebtoonScraper/blob/master/docs/download_availability.md)를 참고하세요.

## Build from source

우선 git과 python을 설치하고 레포지토리를 클론하고 해당 디렉토리로 이동하세요.

```console
git clone https://github.com/ilotoki0804/WebtoonScraper.git
cd WebtoonScraper
```

그런 다음 가상 환경을 생성하고 활성화하세요.

```console
echo 윈도우의 경우
py -3.12 -m venv .venv
.venv\Scripts\activate

echo UNIX인 경우
python3.12 -m venv .venv
.venv/bin/activate
```

poetry를 설치하고 의존성을 설치하세요.

```console
pip install poetry
poetry install --extras full --no-root
```

`simplebuilder`를 실행하세요.

```console
python -m simplebuilder
```

이제 `dist`에 빌드된 `whl` 파일과 `tar.gz` 파일이 나타납니다.

## Release Note

[Release Note 문서](https://github.com/ilotoki0804/WebtoonScraper/blob/master/docs/releases.md)를 참고하세요.
