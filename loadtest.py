# Charge concurrente (simplifiée)
import asyncio, random, time, json
async def task():
    await asyncio.sleep(random.random()/1000)
async def main(n=1000, c=200):
    sem = asyncio.Semaphore(c)
    async def run_one():
        async with sem:
            await task()
    t0=time.time()
    await asyncio.gather(*[run_one() for _ in range(n)])
    dt=time.time()-t0
    print(json.dumps({'n':n,'approx_p95_ms': round((dt/n)*1000*3,3)}))
if __name__=='__main__':
    asyncio.run(main())
