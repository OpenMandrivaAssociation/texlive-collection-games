# revision 25963
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-games
Epoch:		1
Version:	20120810
Release:	1
Summary:	Games typesetting
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-games.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
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
Requires:	texlive-othello
Requires:	texlive-othelloboard
Requires:	texlive-psgo
Requires:	texlive-reverxii
Requires:	texlive-schwalbe-chess
Requires:	texlive-sgame
Requires:	texlive-skak
Requires:	texlive-skaknew
Requires:	texlive-sudoku
Requires:	texlive-sudokubundle
Requires:	texlive-xq
Requires:	texlive-xskak
Requires:	texlive-collection-latex

%description
Setups for typesetting various games, including chess.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813905
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780312
- Update to latest release.
- Import texlive-collection-games
- Import texlive-collection-games

