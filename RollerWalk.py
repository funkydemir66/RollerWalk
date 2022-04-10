import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction

extension_info = {
    "title": "RollerWalk",
    "description": ":rw on&off, c: ",
    "version": "1.0",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

sec_c0d = False
ssec_cod2 = False
sec_cod = False
sec_kod = False
sc = False

def konusma(msj):
    global sc, sec_kod, kod2, kod3, KASAR, cod2, codd2, sec_cod, cod3, codd3, ssec_cod2, sec_c0d


    text = msj.packet.read_string()


    if text == ':rw on':
        msj.is_blocked = True
        sec_cod = True
        ssec_cod2 = True
        sc = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: on "}{i:0}{i:30}{i:0}{i:0}')


    if text == ':rw off':
        msj.is_blocked = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: off "}{i:0}{i:30}{i:0}{i:0}')
        sec_cod = False
        ssec_cod2 = False
        sc = False


    if text == ':c':
        if sc:
            msj.is_blocked = True
            ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: off "}{i:0}{i:30}{i:0}{i:0}')
            sec_kod = True


def yukle_kod(p):
    global kod, sec_kod, kod2, kod3, sec_cod

    if sec_kod:
        _, kod2, kod3, _ = p.packet.read("iiii")
        p.is_blocked = False
        ext.send_to_client('{in:Chat}{i:123456789}{s:"İdd: Saved v/ (code1: '+str(kod2)+') (code2: '+str(kod3)+') "}{i:0}{i:30}{i:0}{i:0}')
        sec_kod = False


def yukle_kod2(d):
    global cod, sec_cod, cod2, cod

    if sec_cod:
        cod2, cod3 = d.packet.read("ii")
        d.is_blocked = False

def SASAR(f):
    global ccod, ssec_cod2, ccod2, ccod3, kod2, kod3, efekt

    if ssec_cod2:
        ccod2, ccod3, _, _, _, _, _, efekt, _, _ = f.packet.read("iiiiiiiiii")
        ext.send_to_server('{out:MoveAvatar}{i:'+str(kod2)+'}{i:'+str(kod3)+'}')
        kod2 = 0
        kod3 = 0
        f.is_blocked = False

ext.intercept(Direction.TO_SERVER, konusma, 'Chat')
ext.intercept(Direction.TO_SERVER, yukle_kod, 'MoveObject')
ext.intercept(Direction.TO_SERVER, yukle_kod2, 'MoveAvatar')
ext.intercept(Direction.TO_CLIENT, SASAR, 'SlideObjectBundle')

