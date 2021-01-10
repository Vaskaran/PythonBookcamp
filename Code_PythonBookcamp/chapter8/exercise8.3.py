try:
    raise BaseException('BaseException raised.')
except Exception as e:
    print(f"Error Details:{e}")

