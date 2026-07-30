# LaTeX Preambles for Case Briefs

## Article Preamble

```latex
\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{setspace}
\setlength{\parindent}{2em}
\setlength{\parskip}{1.25em}
\renewcommand{\baselinestretch}{1.0}
\usepackage{titling}
\newcommand{\subtitle}[1]{%
  \posttitle{%
    \par\end{center}
    \begin{center}\large#1\end{center}
    \vskip0.5em}%
}

\title{[Case Name]}
\subtitle{Case Brief}
\author{}
\date{}

\begin{document}
\maketitle
```

## Beamer Presentation Preamble

```latex
\documentclass{beamer}
\usetheme{Madrid} % Modern theme with gradient headers
\usecolortheme{seahorse} % Professional blue-gray tones
\setbeamertemplate{itemize items}[circle] % Clean circular bullet points
\usepackage{graphicx} % For icons
\usepackage{xcolor}

% Custom colors
\definecolor{lawblue}{RGB}{0,51,102}
\definecolor{lawgold}{RGB}{204,153,0}
\setbeamercolor{title}{fg=lawblue}
\setbeamercolor{frametitle}{fg=lawblue}
\setbeamercolor{itemize item}{fg=lawgold}

\usepackage{booktabs}

\title{[Case Name]}
\subtitle{Case Brief}
\author{}
\date{}

\begin{document}
\frame{\titlepage}
```

## Beamer Slide Guidelines

- Target ~5 main items per slide
- Each item should have at most 2 subitems
- Maximum 9 total items and subitems per slide
- Use `\begin{frame}[allowframebreaks]` for longer content that must stay together

### Example Slide Structure

```latex
\begin{frame}{Section Title}
\begin{itemize}
    \item First main point
        \begin{itemize}
            \item Supporting detail
        \end{itemize}
    \item Second main point
    \item Third main point
        \begin{itemize}
            \item Supporting detail A
            \item Supporting detail B
        \end{itemize}
    \item Fourth main point
    \item Fifth main point
\end{itemize}
\end{frame}
```

## Chapter Brief Format (No Preamble)

For chapter briefs intended for inclusion in a larger casebook project, do NOT include any preamble. Start directly with:

```latex
\chapter{Case Name, Citation}

\section{Detailed Case Facts}
...
```

The parent document will handle all formatting and package imports.
