import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())
#template: async def f1: for-loop:[ await asyncio.sleep(1234), mathstuff(), ...], return xyz
#template: async def f2: L = await asyncio.gather( f1(...),f1(abc), f1(def))
#template: asyncio.run(f2())
