def find_coins_greedy(amount: int) -> dict:
    """
    Жадібний алгоритм для розрахунку решти.
    Обирає найбільші доступні номінали на кожному кроці.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
            
    return result


def find_min_coins(amount: int) -> dict:
    """
    Алгоритм динамічного програмування для пошуку мінімальної кількості монет.
    Побудова розв'язку "знизу-вгору" (bottom-up).
    """
    coins = [1, 2, 5, 10, 25, 50]
    
    # dp[i] зберігатиме мінімальну кількість монет для суми i
    dp = [0] + [float('inf')] * amount
    # last_coin[i] зберігатиме останню використану монету для відновлення відповіді
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # Відновлення складу монет за допомогою масиву last_coin
    result = {}
    curr_amount = amount
    while curr_amount > 0:
        coin = last_coin[curr_amount]
        result[coin] = result.get(coin, 0) + 1
        curr_amount -= coin

    return result

if __name__ == "__main__":

    amount = 113
    greedy_result = find_coins_greedy(amount)
    min_coins_result = find_min_coins(amount)

    print(f"Жадібний алгоритм для суми {amount}: {greedy_result}")
    print(f"Мінімальна кількість монет для суми {amount}: {min_coins_result}")