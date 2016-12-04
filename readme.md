# Сборка скриптов для генерации отчетов + LaTeX заготовка

## Сбор всего исходного кода в docx

`src-to-doc.py` - рекурсивно конвертирует исходники в папке в docx. Требуется Pandoc.

Чтобы узнать подробнее:
```
py src-to-doc.py -h
```

## Вставка исходного кода в tex файл

Положение кода в файле определяется кодовым комметнарием `%code%`

Пример
```
python make.py -i lab-report.tex -o lab.pdf -d ../sample-source/ -p *.java
```

### Windows

Используется связка MikTeX 2.9 + Sublime Text 3 + LaTeXTools (плагин для ST3)

### Ubuntu

Вместо MikTex

```bash
sudo apt install texlive-xetex
sudo apt install texlive-lang-cyrillic
fmtutil --all
sudo apt install latexmk
```
Работать так же в Sublime text или как в примере выше