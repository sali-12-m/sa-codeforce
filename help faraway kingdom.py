s = input().strip()
intt, fra= s.split('.')
if intt[-1] == '9':
    print("GOTO Vasilisa.")
else:
    if fra[0] >= '5':
        intt = str(int(intt) + 1)
    print(intt)