#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from diffie_hellman_module import diffie_hellman_KE

def main():
    if len(sys.argv) == 2:
        AES_KEY = diffie_hellman_KE(sys.argv[1])
    
    else:
        print(sys.argv)
        AES_KEY = diffie_hellman_KE()

    print(f"AES_KEY_DHKE: {AES_KEY}")
    

if __name__ == "__main__":
    main()
