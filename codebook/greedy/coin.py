n = 1260
count = 0

coin_types = [500, 100, 50 10]

for coin in coin_types:
    count += n//coin  # 해당 화폐로 거슬러 줄 수 있는 코인의 최대 갯수.
    n %= coin

print(count, n)
