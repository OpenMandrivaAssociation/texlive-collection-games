%global tl_name collection-games
%global tl_revision 79849

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Games typesetting
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-games
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-games.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(bartel-chess-fonts)
Requires:	texlive(cardgame)
Requires:	texlive(carom-billiards)
Requires:	texlive(chess)
Requires:	texlive(chess-problem-diagrams)
Requires:	texlive(chessboard)
Requires:	texlive(chessfss)
Requires:	texlive(chinesechess)
Requires:	texlive(collection-latex)
Requires:	texlive(crossword)
Requires:	texlive(crosswrd)
Requires:	texlive(customdice)
Requires:	texlive(egameps)
Requires:	texlive(eigo)
Requires:	texlive(gamebook)
Requires:	texlive(gamebooklib)
Requires:	texlive(go)
Requires:	texlive(hanoi)
Requires:	texlive(havannah)
Requires:	texlive(hexboard)
Requires:	texlive(hexgame)
Requires:	texlive(hmtrump)
Requires:	texlive(horoscop)
Requires:	texlive(jeuxcartes)
Requires:	texlive(jigsaw)
Requires:	texlive(labyrinth)
Requires:	texlive(logicpuzzle)
Requires:	texlive(magicthegathering)
Requires:	texlive(mahjong)
Requires:	texlive(mahjong-tiles)
Requires:	texlive(mathador)
Requires:	texlive(maze)
Requires:	texlive(multi-sudoku)
Requires:	texlive(musikui)
Requires:	texlive(nimsticks)
Requires:	texlive(onedown)
Requires:	texlive(othello)
Requires:	texlive(othelloboard)
Requires:	texlive(pas-crosswords)
Requires:	texlive(pgf-go)
Requires:	texlive(playcards)
Requires:	texlive(psgo)
Requires:	texlive(quizztex)
Requires:	texlive(realtranspose)
Requires:	texlive(reverxii)
Requires:	texlive(rouequestions)
Requires:	texlive(rpgicons)
Requires:	texlive(rubik)
Requires:	texlive(schwalbe-chess)
Requires:	texlive(scrabble)
Requires:	texlive(sgame)
Requires:	texlive(skak)
Requires:	texlive(skaknew)
Requires:	texlive(soup)
Requires:	texlive(sudoku)
Requires:	texlive(sudokubundle)
Requires:	texlive(tangramtikz)
Requires:	texlive(thematicpuzzle)
Requires:	texlive(tictactoe)
Requires:	texlive(tikz-catan)
Requires:	texlive(tikz-triminos)
Requires:	texlive(trivialpursuit)
Requires:	texlive(twoxtwogame)
Requires:	texlive(wargame)
Requires:	texlive(weiqi)
Requires:	texlive(wordle)
Requires:	texlive(xq)
Requires:	texlive(xskak)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Setups for typesetting various games, including chess.

