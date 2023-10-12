import asyncio


async def fun(n: int) -> list[int]:
    sequence = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


async def app():
    sequences = await asyncio.gather(fun(7), fun(11), fun(17), fun(37))
    print(sequences)

asyncio.run(app())
