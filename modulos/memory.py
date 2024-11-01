import psutil
import asyncio

async def monitorar_memoria():
    memoria = psutil.virtual_memory()
    memoria_total = memoria.total
    memoria_usada = memoria.used
    memoria_livre = memoria.free
    memoria_porcentagem = memoria.percent

    return memoria_total, memoria_usada, memoria_livre, memoria_porcentagem

