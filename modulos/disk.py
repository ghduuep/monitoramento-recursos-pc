import psutil
import asyncio

async def monitorar_disco():
    disco = psutil.disk_usage('/')
    disco_total = disco.total
    disco_usado = disco.used
    disco_livre = disco.free
    disco_porcentagem = disco.percent

    return disco_total, disco_livre, disco_usado, disco_porcentagem
