from modulos.cpu import monitorar_cpu
from modulos.memory import monitorar_memoria
from modulos.disk import monitorar_disco
import asyncio

nucleos, threads = asyncio.run(monitorar_cpu())
memoria_total, memoria_usada, memoria_livre, memoria_porcentagem = asyncio.run(monitorar_memoria())
disco_total, disco_livre, disco_usado, disco_porcentagem = asyncio.run(monitorar_disco())
print('=> cpu')
print(f'nucleos: {nucleos}')
print(f'threads: {threads}')

print('=' * 30)
print('\n=> memoria')
print(f'memoria total: {memoria_total / 1024}')
print(f'memoria livre: {memoria_livre / 1024}')
print(f'memoria usada: {memoria_usada / 1024} - {memoria_porcentagem}%')

print('=' * 30)
print('\n=> disco')
print(f'disco total: {disco_total / 1024}')
print(f'disco livre: {disco_livre/ 1024}')
print(f'disco usada: {disco_usado/ 1024} - {disco_porcentagem}%')



