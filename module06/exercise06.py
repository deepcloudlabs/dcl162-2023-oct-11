from concurrent.futures import ThreadPoolExecutor


def fun(n: int) -> list[int]:
    print(f"fun({n}) is just started!")
    sequence = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    print(f"fun({sequence[0]}) is about to complete!")
    return sequence


sequences = []
with ThreadPoolExecutor(max_workers=16) as tp1:
    futures = []
    print("before: for i in range(11, 10_000)")
    for i in range(11, 10_000):
        futures.append(tp1.submit(fun, i))
    print("after: for i in range(11, 10_000)")
    for future in futures:
        sequences.append(future.result())
"""
for sequence in sequences:
    print(sequence)
"""
