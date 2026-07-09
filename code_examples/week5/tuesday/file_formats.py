import pandas as pd, numpy as np, os, time

# ~100k rows — big enough to see the gap, fast enough to run in seconds
n = 100_000
rng = np.random.default_rng(42)
df = pd.DataFrame({
    "id": np.arange(n),
    "name": [f"user_{i}" for i in range(n)],
    "dept": rng.choice(["Web", "Kernel", "Data", "Ops"], n),
    "salary": rng.uniform(30_000, 150_000, n).round(2),
    "active": rng.choice([True, False], n),
})

os.makedirs("out", exist_ok=True)   # never assume the dir exists

def timed_write(label, path, fn):
    t = time.perf_counter()
    fn(path)
    secs = time.perf_counter() - t
    mb = os.path.getsize(path) / 1024 / 1024
    print(f"{label:<8} {mb:7.2f} MB   {secs:6.3f} s")

print(f"{'format':<8} {'size':>7}      {'write':>6}")
timed_write("CSV",     "out/d.csv",     lambda p: df.to_csv(p, index=False))
timed_write("JSONL",   "out/d.jsonl",   lambda p: df.to_json(p, orient="records", lines=True))
timed_write("Parquet", "out/d.parquet", lambda p: df.to_parquet(p, compression="snappy"))

# Typical result: Parquet is the smallest file AND competitive/fastest to write,
# while CSV/JSONL are several times larger. The gap widens with more rows.