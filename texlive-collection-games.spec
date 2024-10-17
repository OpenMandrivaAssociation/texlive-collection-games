Name:		texlive-collection-games
Epoch:		1
Version:	71129
Release:	1
Summary:	Games typesetting
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-games.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-latex
Requires:	texlive-bartel-chess-fonts
Requires:	texlive-chess
Requires:	texlive-chess-problem-diagrams
Requires:	texlive-chessboard
Requires:	texlive-chessfss
Requires:	texlive-crossword
Requires:	texlive-crosswrd
Requires:	texlive-egameps
Requires:	texlive-gamebook
Requires:	texlive-go
Requires:	texlive-hanoi
Requires:	texlive-hexgame
Requires:	texlive-horoscop
Requires:	texlive-labyrinth
Requires:	texlive-logicpuzzle
Requires:	texlive-othello
Requires:	texlive-othelloboard
Requires:	texlive-pas-crosswords
Requires:	texlive-psgo
Requires:	texlive-reverxii
Requires:	texlive-rubik
Requires:	texlive-schwalbe-chess
Requires:	texlive-sgame
Requires:	texlive-skak
Requires:	texlive-skaknew
Requires:	texlive-sudoku
Requires:	texlive-sudokubundle
Requires:	texlive-xq
Requires:	texlive-xskak

%description
Setups for typesetting various games, including chess.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
