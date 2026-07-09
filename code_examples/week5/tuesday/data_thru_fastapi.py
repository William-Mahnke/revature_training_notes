# app.py
from contextlib import asynccontextmanager
from pathlib import Path
import io
import pandas as pd
from fastapi import FastAPI, Query, HTTPException

DF: pd.DataFrame | None = None

# A tiny inline dataset so this runs with zero setup.
# In the demo this is a real CSV loaded via read_csv.
SAMPLE_CSV = """order_id,dept,region,amount
1,Web,East,120.50
2,Data,West,300.00
3,Web,West,90.25
4,Ops,East,45.00
5,Data,East,275.75
6,Web,East,60.00
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    global DF
    DF = pd.read_csv(io.StringIO(SAMPLE_CSV))   # load ONCE at startup
    yield

app = FastAPI(title="DataFrame API", lifespan=lifespan)

def clean(df: pd.DataFrame) -> list[dict]:
    """NaN -> None so the JSON is valid, then to records."""
    return df.where(df.notna(), None).to_dict(orient="records")

@app.get("/health")
def health():
    return {"status": "ok", "rows": len(DF)}  # pyright: ignore[reportArgumentType]

@app.get("/records")
def records(limit: int = Query(50, ge=1, le=500),
            offset: int = Query(0, ge=0),
            dept: str | None = None):
    df = DF if dept is None else DF[DF["dept"] == dept]  # pyright: ignore[reportOptionalSubscript]
    page = df.iloc[offset : offset + limit]  # pyright: ignore[reportOptionalMemberAccess]
    return {"total": len(df), "limit": limit, "offset": offset,  # pyright: ignore[reportArgumentType]
            "results": clean(page)}

@app.get("/summary")
def summary():
    """Overall stats — like SELECT COUNT(*), SUM(amount), AVG(amount)."""
    return {
        "orders": int(len(DF)),  # pyright: ignore[reportArgumentType]
        "total_amount": round(float(DF["amount"].sum()), 2),  # pyright: ignore[reportOptionalSubscript, reportArgumentType]
        "avg_amount": round(float(DF["amount"].mean()), 2),  # pyright: ignore[reportArgumentType, reportOptionalSubscript]
    }

@app.get("/by-dept")
def by_dept():
    """Aggregate per department -> JSON. GROUP BY dept."""
    agg = (DF.groupby("dept")  # pyright: ignore[reportOptionalMemberAccess]
             .agg(orders=("order_id", "count"),
                  total_amount=("amount", "sum"),
                  avg_amount=("amount", "mean"))
             .round(2)
             .reset_index())            # <- turn the group key back into a column
    return {"results": clean(agg)}

@app.get("/by-dept/{dept}")
def one_dept(dept: str):
    sub = DF[DF["dept"] == dept]  # pyright: ignore[reportOptionalSubscript]
    if sub.empty:
        raise HTTPException(status_code=404, detail=f"No orders for dept '{dept}'")
    return {"dept": dept, "orders": clean(sub)}  # pyright: ignore[reportArgumentType]