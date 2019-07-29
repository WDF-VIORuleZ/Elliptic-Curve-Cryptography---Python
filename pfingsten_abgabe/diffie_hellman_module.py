
import gf2_arithmetics_module as gf2
import ecc_arithmetics_moudle as ecc


"""
    Calculating the AES key based on the secret T_AB
    Aufgabe 3.
"""
def calc_key(T_AB):
    T_AB_bin = bin(T_AB)[2:]
    #0's padding
    T_AB_bin = (256 - len(T_AB_bin)) * '0' + T_AB_bin if len(T_AB_bin) < 256 else print("[+] no paddnig required")

    T_AB_bin_1, T_AB_bin_2 = T_AB_bin[0:128], T_AB_bin[128:256]
    len00 = len(T_AB_bin)
    len11 = len(T_AB_bin_1)
    len22 = len(T_AB_bin_2)

    res_hex = hex(( int(T_AB_bin_1, base=2)) ^ int(T_AB_bin_2, base=2))

    return res_hex

"""
    Integration of all subtasks into the generation of the AES key used for deciphering the
    given hex file
"""
def diffie_hellman_KE(mode:str="fermat"):

    k_priv_A = 0x20A5B20E076E77984380CB49173F6ED7FDED87E645747133F63888907245E5D8
    k_priv_B = 0x63690612179A5742A7DB7003F0545E866CAF9DE086BF272A0E1827165381B399

    p        = 0xA9FB57DBA1EEA9BC3E660A909D838D726E3BF623D52620282013481D1F6E5377
    a        = 0x7D5A0975FC2C3057EEF67530417AFFE7FB8055C126DC5C6CE94A4B44F330B5D9
    b        = 0x26DC5C6CE94A4B44F330B5D9BBD77CBF958416295CF7E1CE6BCCDC18FF8C07B6
    x        = 0x8BD2AEB9CB7E57CB2C4B482FFC81B7AFB9DE27E1E3BD23C23A4453BD9ACE3262
    y        = 0x547EF835C3DAC4FD97F8461A14611DC9C27745132DED8E545C1D54C72F046997
    q        = 0xA9FB57DBA1EEA9BC3E660A909D838D718C397AA3B561A6F7901E0E82974856A7    

 
    # Initialsizing the primitive element P and the elliptic curve E using the given values 
    P = ecc.ecc_point(x,y)
    E = ecc.ecc_curve(a, b, p)


    # Calculating A's and B's public keys using 
    k_pub_A = ecc.mul_point(k_priv_A, P, E, mode)
    k_pub_B = ecc.mul_point(k_priv_B, P, E, mode)

    T_AB_a = ecc.mul_point(k_priv_A, k_pub_B, E, mode)
    T_AB_b = ecc.mul_point(k_priv_B, k_pub_A, E, mode)

    if T_AB_a == T_AB_b:
        Xi = calc_key(T_AB_a.x)
        return Xi
    
    else: return None
