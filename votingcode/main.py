print("VOTE COUNT FOR YES")
yes = int(input())
print("VOTE COUNT FOR NO")
no = int(input())
result = yes / (yes + no)
result_percentage = result * 100
print("Result percentage: %", result_percentage)
if result_percentage < 50:
    print("REJECTED")
elif result_percentage > 50:
    print("ACCEPTED")
else:
    print("INVALID VOTE")
