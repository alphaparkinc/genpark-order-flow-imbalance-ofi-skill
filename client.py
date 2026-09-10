class OrderFlowImbalance:
    """
    Cont et al. Order Flow Imbalance (OFI).
    Measures net volume changes at best bid and ask quotes between timestamps:
    e_n = I(P_b >= P_b_prev)*q_b - I(P_b <= P_b_prev)*q_b_prev - (I(P_a <= P_a_prev)*q_a - I(P_a >= P_a_prev)*q_a_prev)
    """
    def compute_ofi(self, prev_quote, curr_quote):
        p_b0, q_b0, p_a0, q_a0 = prev_quote
        p_b1, q_b1, p_a1, q_a1 = curr_quote

        if p_b1 > p_b0:
            delta_bid = q_b1
        elif p_b1 == p_b0:
            delta_bid = q_b1 - q_b0
        else:
            delta_bid = -q_b0

        if p_a1 < p_a0:
            delta_ask = q_a1
        elif p_a1 == p_a0:
            delta_ask = q_a1 - q_a0
        else:
            delta_ask = -q_a0

        return delta_bid - delta_ask
