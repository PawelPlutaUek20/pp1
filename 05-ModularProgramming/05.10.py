import QuadraticEquation as qe

wspolczynniki = qe.czytajWspolczynniki()
delta = qe.obliczDelte(wspolczynniki)
pierwiastki = qe.obliczPierwiastki(wspolczynniki,delta)
qe.wyswietlPierwiastki(wspolczynniki,pierwiastki)