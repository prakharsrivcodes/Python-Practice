credit_card_numbeer = "1234-5678-9012-3456"
print(credit_card_numbeer[0:4])  # Output: 1234
print(credit_card_numbeer[:4]) #assumses starting from index 0, Output: 1234
print(credit_card_numbeer[5:9])  # Output: 5678
print(credit_card_numbeer[5:]) #assumes starting from index 5 to the end of the string, Output: 5678-9012-3456

print(credit_card_numbeer[10:14])  # Output: 9012
print(credit_card_numbeer[15:19])  # Output: 3456   

print(credit_card_numbeer[-4:])  # Output: 3456
print(credit_card_numbeer[::3])  # Output: 147-0-2-4


# reverse the charactes im stirng
print(credit_card_numbeer[::-1])  # Output: 6543-2109-8765-4321

