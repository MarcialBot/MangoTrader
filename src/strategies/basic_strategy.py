def should_buy(last_price, threshold=50000):
    if last_price > threshold:
        return True
    return False
