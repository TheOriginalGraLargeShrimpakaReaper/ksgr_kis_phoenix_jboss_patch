%! Class = CLASS_NAME
%! Author = itgramic
%! Date = 22.11.23
\usepackage[skip=0cm plus 0cm,indent=0cm]{parskip}
\usepackage{fancyhdr}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{book}[2023/11/08 v0.1 Klasse fuer Michael Graber ibw Diplomarbeit Disposition]
%\LoadClass[11pt,a4paper,bibliography=totoc,listof=totoc]{scrreprt}
%\input{ibw_disposition_secondclass.cls}
\ProcessOptions\relax
%\documentclass{ibw_disposition}
%\LoadClass[a4paper]{book}
%\LoadClass[11pt,a4paper,bibliography=totoc,listof=totoc]{book}
\LoadClass[11pt,a4paper,bibliography=totoc,listof=totoc, twosite]{scrreprt}
\RequirePackage[T1]{fontenc}
\RequirePackage{graphicx}
\RequirePackage{varwidth}

\RequirePackage{setspace}
\onehalfspacing

%\RequirePackage[left=3cm, right=3cm]{geometry}
\RequirePackage[left=2cm, right=2cm, top=1.25cm,bottom=2cm,hmargin=2cm,includeheadfoot,head=40pt,headsep=0cm,foot=0.75cm,footskip=1.3989999cm]{geometry}

\RequirePackage{helvet}
\renewcommand{\familydefault}{\sfdefault}

\RequirePackage[english,ngerman]{babel}

\RequirePackage{layout}

\newenvironment{managementsummary}{
\begingroup
\let\clearpage\relax
\chapter*{Management Summary}
\endgroup
\noindent{}}

\newenvironment{abkuerzungen}[1][WWWWW]{\chapter*{Abk\"urzungen}
\addcontentsline{toc}{chapter}{Abk\"urzungen}
\begin{labeling}{#1}}{\end{labeling}}


\setcounter{secnumdepth}{5}

\renewcommand\thechapter{\arabic{chapter}}
\renewcommand\thesection{\arabic{chapter}.\arabic{section}}
\renewcommand\thesubsection{\arabic{chapter}.\arabic{section}.\arabic{subsection}}
\renewcommand\thesubsubsection{\arabic{chapter}.\arabic{section}.\arabic{subsection}.\arabic{subsubsection}}
\renewcommand\theparagraph{\arabic{chapter}.\arabic{section}.\arabic{subsection}.\arabic{subsubsection}.\arabic{paragraph}}
\renewcommand\thesubparagraph{\arabic{chapter}.\arabic{section}.\arabic{subsection}.\arabic{subsubsection}.\arabic{paragraph}.\arabic{subparagraph}}

% Value Commands
\newcommand{\@dokuemnttitel}{}
\newcommand{\dokuemnttitel}[1]{\gdef\@dokuemnttitel{#1}}
\newcommand{\@toptitel}{}
\newcommand{\toptitel}[1]{\gdef\@toptitel{#1}}
\newcommand{\@datum}{}
\newcommand{\datum}[1]{\gdef\@datum{#1}}


\pagestyle{fancy}
\thispagestyle{fancy}
\markright{\protect\@fancypagestyle}
\setlength{\skip\footins}{0.119cm}
\renewcommand\footnoterule{\vspace*{-0.018cm}\setlength\leftskip{0pt}\setlength\rightskip{0pt plus 1fil}\noindent\textcolor{black}{\rule{0.25\columnwidth}{0.018cm}}\vspace*{0.101cm}}

% Title Page
\pagestyle{fancy}

\renewcommand{\dedication}[1]{\gdef\@dedication{\ \vfill\begin{center}#1\end{center}\vfill\vfill\ \newpage}}

\renewcommand\maketitle{
\setcounter{page}{0}

\begin{titlepage}
\thispagestyle{FirstPage}
\markright{\protect\@titlehead}

\textbf{}\\
\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip
\textcolor[HTML]{000000}{ \ \huge\@toptitel}\newline
\bigskip

\bigskip
\textbf{\textcolor[HTML]{000000}{ \ \Huge\@dokuemnttitel}}
\bigskip


\bigskip


\bigskip
\textcolor[HTML]{000000}{\ \LARGE\@datum}
\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip

\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip
\textbf{ }

\clearpage

\end{titlepage}
\@dedication
}

\pagestyle{headings}
\pagenumbering{roman}
\newcommand{\startThesis}{\newpage\pagenumbering{arabic}\setcounter{page}{1}\pagestyle{headings}}



