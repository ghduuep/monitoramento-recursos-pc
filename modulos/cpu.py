import psutil
import asyncio

async def monitorar_cpu():
    p = psutil.Process()
    nucleos = psutil.cpu_count()
    threads = p.num_threads()

    return nucleos, threads
