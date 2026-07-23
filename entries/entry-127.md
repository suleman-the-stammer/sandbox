# entry 127 — 2026-07-23T13:10:00Z

```python
def fib(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    print(list(fib(10)))
```
