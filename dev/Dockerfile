FROM python:slim

ARG pandoc_version=2.19.2

RUN pip install --no-cache md2cf python-frontmatter \
    && apt-get update -y -qq \
    && apt-get install -y --no-install-recommends \
        zip \
        wget \
        curl \
        build-essential \
    && apt-get clean \
    && wget -q https://github.com/jgm/pandoc/releases/download/${pandoc_version}/pandoc-${pandoc_version}-1-amd64.deb \
    && dpkg -i pandoc-${pandoc_version}-1-amd64.deb \
    && rm pandoc-${pandoc_version}-1-amd64.deb
