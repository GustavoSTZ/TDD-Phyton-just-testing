from src.leilao.dominio import Leilao, Usuario, Lance, Avaliador


gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('celular')

leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

print(f'Lance do usuario {gui.nome} com o valor de {lance_do_gui.valor}')
print(f'Lance do usuario {yuri.nome} com o valor de {lance_do_yuri.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'Maior lance: {avaliador.maior_lance}')
print(f'Menor lance: {avaliador.menor_lance}')