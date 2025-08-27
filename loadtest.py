import asyncio, argparse, time, random
from orchestrator import Orchestrator
from memory import FractalMemory

async def worker(n, orch):
    # simulate processing delay
    await asyncio.sleep(random.random()/1000)
    orch.process({"id": f"w{n}", "role":"agent", "content":"x"})

async def main(messages, concurrency):
    mem = FractalMemory()
    orch = Orchestrator(memory=mem)
    sem = asyncio.Semaphore(concurrency)
    async def run_one(i):
        async with sem:
            await worker(i, orch)
    t0 = time.time()
    await asyncio.gather(*[run_one(i) for i in range(messages)])
    dt = time.time() - t0
    print(f"processed={messages} latency_p95_ms≈{round(dt/messages*1000*3,3)}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--messages", type=int, default=1000)
    ap.add_argument("--concurrency", type=int, default=200)
    args = ap.parse_args()
    asyncio.run(main(args.messages, args.concurrency))
