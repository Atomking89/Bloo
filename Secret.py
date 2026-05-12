for i in range(3):
    secret = 10987654321
    human = int(input("YOU WILL NEVER GUESS THE CORRECT NUMBER!!!"))
    if human == secret:
        print("How did you guess my secret code? You are correct! :D")
        break
    if human > secret:
        print("Way too big.")
    if human < secret:
        print("Too low.")
print("GAME OVER!")