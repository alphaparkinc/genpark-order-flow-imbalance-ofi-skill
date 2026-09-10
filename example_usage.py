from client import OrderFlowImbalance

def main():
    print("=== Testing Order Flow Imbalance (OFI) Predictor ===")
    ofi = OrderFlowImbalance()

    q_t0 = (100.0, 50, 101.0, 50)
    q_t1 = (100.0, 80, 101.0, 30) # +30 bids, -20 asks -> aggressive buying

    signal = ofi.compute_ofi(q_t0, q_t1)
    print("Calculated OFI net buying flow:", signal)
    assert signal == 50
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
