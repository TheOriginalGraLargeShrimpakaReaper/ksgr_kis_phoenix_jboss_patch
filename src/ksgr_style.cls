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

%\renewenvironment{abstract}{\selectlanguage\english
%\begingroup
%\let\clearpage\relax
%\chapter*{Abstract}
%\endgroup
%\noindent}{}

\newenvironment{abkuerzungen}[1][WWWWW]{\chapter*{Abk\"urzungen}
\addcontentsline{toc}{chapter}{Abk\"urzungen}
\begin{labeling}{#1}}{\end{labeling}}


\setcounter{secnumdepth}{5}
%\begin{minipage}
%\pagestyle{fancy}
%\fancypagestyle{Standard}{\fancyhf{}
%%  \fancyhead[L]{}
%  \fancyfoot[C]{\thepage{}}
%  \renewcommand\headrulewidth{0pt}
%  \renewcommand\footrulewidth{0pt}
%  \renewcommand\thepage{\arabic{page}}
%  \rhead{\includegraphics[width=1cm]{source/main/ibw}}
%
%  \fancyhead[L]{\fontsize{11.5pt}{13.8ptpt} \selectfont\rmfamily\bfseries\color[HTML]{2F5496}Disposition Diplomarbeit}
%}
%\fancypagestyle{FirstPage}{\fancyhf{}
%  \fancyhead[L]{}
%  \fancyfoot[L]{}
%  \renewcommand\headrulewidth{0pt}
%  \renewcommand\footrulewidth{0pt}
%  \renewcommand\thepage{\arabic{page}}
%  \rhead{\includegraphics[width=1cm]{source/main/ibw}}
%}

%    % Headings
%
%\titleformat{\chapter}[block]{\filright\normalfont\normalsize\normalcolor\fontsize{11.5pt}{13.8pt}\selectfont\rmfamily\bfseries\color[HTML]{2F5496}}{{\fontsize{12pt}{14.400001pt}\selectfont \makebox[2.5cm][l]{\thechapter}}}{0pt}{#1}[]
%\titlespacing*{\chapter}{0pt}{0.847cm plus 0.1694cm minus 0.0847cm}{0.212cm plus 0.0424cm minus 0.0212cm}
%
%\titleformat{\section}[block]{\filright\normalfont\normalsize\normalcolor\fontsize{11.5pt}{13.8pt}\selectfont\rmfamily\bfseries\color[HTML]{2F5496}}{{\fontsize{11pt}{14.400001pt}\selectfont \makebox[2.5cm][l]{\thesection}}}{0pt}{#1}[]
%\titlespacing*{\section}{0pt}{0.847cm plus 0.1694cm minus 0.0847cm}{0.212cm plus 0.0424cm minus 0.0212cm}
%\titleformat{\subsection}[block]{\filright\normalfont\normalsize\normalcolor\fontsize{10pt}{13.8pt}\selectfont\rmfamily\bfseries\color[HTML]{2F5496}}{{\fontsize{11pt}{14.400001pt}\selectfont \makebox[2.5cm][l]{\thesubsection}}}{0pt}{#1}[]
%\titlespacing*{\subsection}{0pt}{0.847cm plus 0.1694cm minus 0.0847cm}{0.212cm plus 0.0424cm minus 0.0212cm}
%\titleformat{\subsubsection}[block]{\filright\normalfont\normalsize\normalcolor\fontsize{10pt}{13.8pt}\selectfont\rmfamily\bfseries\color[HTML]{2F5496}}{{\fontsize{11pt}{14.400001pt}\selectfont \makebox[2.5cm][l]{\thesubsubsection}}}{0pt}{#1}[]
%\titlespacing*{\subsubsection}{0pt}{0.847cm plus 0.1694cm minus 0.0847cm}{0.212cm plus 0.0424cm minus 0.0212cm}
%\titleformat{\subsubsection}[block]{\filright\normalfont\normalsize\normalcolor\fontsize{10pt}{13.8pt}\selectfont\rmfamily\bfseries\color[HTML]{2F5496}}{{\fontsize{11pt}{14.400001pt}\selectfont \makebox[2.5cm][l]{\thesubsubsection}}}{0pt}{#1}[]
%\titlespacing*{\subsubsection}{0pt}{0.847cm plus 0.1694cm minus 0.0847cm}{0.212cm plus 0.0424cm minus 0.0212cm}
%\titleformat{\paragraph}[block]{\filright\normalfont\normalsize\normalcolor\fontsize{10pt}{13.8pt}\selectfont\rmfamily\bfseries\color[HTML]{2F5496}}{{\fontsize{11pt}{14.400001pt}\selectfont \makebox[2.5cm][l]{\theparagraph}}}{0pt}{#1}[]
%\titlespacing*{\paragraph}{0pt}{0.847cm plus 0.1694cm minus 0.0847cm}{0.212cm plus 0.0424cm minus 0.0212cm}
%\titleformat{\subparagraph}[block]{\filright\normalfont\normalsize\normalcolor\fontsize{10pt}{13.8pt}\selectfont\rmfamily\bfseries\color[HTML]{2F5496}}{{\fontsize{11pt}{14.400001pt}\selectfont \makebox[2.5cm][l]{\thesubparagraph}}}{0pt}{#1}[]
%\titlespacing*{\subparagraph}{0pt}{0.847cm plus 0.1694cm minus 0.0847cm}{0.212cm plus 0.0424cm minus 0.0212cm}

%\end{minipage}

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
%\newcommand{\@department}{}
%\newcommand{\department}[1]{\gdef\@department{#1}}
%\newcommand{\@abteilung}{}
%\newcommand{\abteilung}[1]{\gdef\@abteilung{#1}}
%\newcommand{\@vorname}{}
%\newcommand{\vorname}[1]{\gdef\@vorname{#1}}
%\newcommand{\@nachname}{}
%\newcommand{\nachname}[1]{\gdef\@nachname{#1}}
%\newcommand{\@funktion}{}
%\newcommand{\funktion}[1]{\gdef\@funktion{#1}}
%\newcommand{\@mail}{}
%\newcommand{\mail}[1]{\gdef\@mail{#1}}
%\newcommand{\@telefon}{}
%\newcommand{\telefon}[1]{\gdef\@telefon{#1}}
%\newcommand{\@footertitel}{}
%\newcommand{\footertitel}[1]{\gdef\@footertitel{#1}}

\pagestyle{fancy}
\thispagestyle{fancy}
\markright{\protect\@fancypagestyle}
\setlength{\skip\footins}{0.119cm}
\renewcommand\footnoterule{\vspace*{-0.018cm}\setlength\leftskip{0pt}\setlength\rightskip{0pt plus 1fil}\noindent\textcolor{black}{\rule{0.25\columnwidth}{0.018cm}}\vspace*{0.101cm}}
%\title{ibW Höhere Fachschule Südostschweiz}
%\author{Thomas Leemann}
%\date{2023-08-17}

% Title Page
\pagestyle{fancy}

%\pagehead{
%\thispagestyle{Standard}
%\begin{varwidth}[t][2cm][c]{5cm}
%\begin{flushright}
%\includegraphics[height=2cm]{source/main/ibw}
%\end{flushright}
%\end{varwidth}
%\hfill
%\begin{varwidth}[t][2cm][c]{7cm}
%\begin{flushright}
%\normalfont
%%Fernfachhochschule Schweiz\\
%%Studiengang \@studiengang
%\vfill\phantom{.}
%\end{flushright}
%\end{varwidth}
%}

%\newcommand{\@dokumentTyp}{Entwurf}
%\newcommand{\dokumentTyp}[1]{\gdef\@dokumentTyp{#1}}
%
%\newcommand{\@studiengang}{INF/WI}
%\newcommand{\studiengang}[1]{\gdef\@studiengang{#1}}
%
%\newcommand{\@wohnort}{}
%\newcommand{\wohnort}[1]{\gdef\@wohnort{#1}}
%
%
%
%\newcommand{\@dozent}{}
%\newcommand{\@dozent@in}{Dozent(in)}
%\newcommand{\dozent}[1]{\gdef\@dozent@in{Dozent} \gdef\@dozent{#1}}
%\newcommand{\dozentin}[1]{\gdef\@dozent@in{Dozentin} \gdef\@dozent{#1}}
%
%
%\newcommand{\@titelbild}{}
%\newcommand{\titelbild}[2][]{\gdef\@titelbild{\includegraphics[#1]{#2}}}
%
%\newcommand{\@eingereichtBei}{}
%\newcommand{\eingereichtBei}[1]{\gdef\@eingereichtBei{#1}}

\renewcommand{\dedication}[1]{\gdef\@dedication{\ \vfill\begin{center}#1\end{center}\vfill\vfill\ \newpage}}

\renewcommand\maketitle{
\setcounter{page}{0}

\begin{titlepage}
%\thispagestyle{headings}
\thispagestyle{FirstPage}
\markright{\protect\@titlehead}

%\textbf{ibW Höhere Fachschule Südostschweiz}
\textbf{}\\
\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip


\bigskip
%\textbf{\textcolor[HTML]{000000}\fontsize{13pt}{{\@toptitel}}
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



