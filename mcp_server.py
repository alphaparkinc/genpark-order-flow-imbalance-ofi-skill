import sys
import json
from client import OrderFlowImbalance

ofi = OrderFlowImbalance()

def handle_call(name, arguments):
    if name == "compute_ofi":
        q0 = tuple(arguments["prev_quote"])
        q1 = tuple(arguments["curr_quote"])
        return {"ofi": ofi.compute_ofi(q0, q1)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
