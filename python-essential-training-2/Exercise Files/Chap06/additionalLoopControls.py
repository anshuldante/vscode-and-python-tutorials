#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
count = 0
auth = False
max_attempt = 5


while pw != secret:
    count += 1
    if count > 5: break
    if count == 3: continue
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

print("Authorized" if auth else "Calling the FBI!")
