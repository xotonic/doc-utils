# Сборка скриптов для генерации отчетов + LaTeX заготовка

`src-to-doc.py` - рекурсивно конвертирует исходники в папке в docx. Требуется Pandoc.

Чтобы узнать подробнее:
```
py src-to-doc.py -h
```

`src-to-latex-listings.py` - генерирует ссылки на файлы исходного кода для Latex (через  пакет `listings`). Предазначен для `lab-report.tex`. Просто выводит готовый код LaTeX


`lab-report.tex` - отчет по лабораторной на LaTeX

Используется связка MikTeX 2.9 + Sublime Text 3 + LaTeXTools (плагин для ST3)