#! /usr/bin/env python3

'''
Gordon Ramsay Insult Generator.
Credit: Some image throughly reposted and in the internet, to the point where
JPEG artefacts are larger than the text itself, and watermarks are put over 
watermarks to no end.

2017-03-29T09:52-03:00
'''
from random import seed, choice
from time import time
from codecs import encode
def insult():
    a = ['Shpx Bss!', 'Fuhg gur shpx hc!', 'Cvff bss', 'Trg bhg!', "VG' ENNNJ!",
        "Vg'f oheag!", 'Jung gur shpx ner lbh qbvat!?', 'Zbir lbhe nff!', 
        'Zber fnhpr!', 'Jnxr hc!', 'Trg n tevc!', 'Tvzzr lbhe wnpxrg!', 
        'Tbbq Wrfhf!']
    b = ['Lbh fghcvq', 'Lbh ynml ', 'Lbh cngurgvp', 'Lbh hfryrff', 'Lbh fvyyl', 
        'Lbh vtabenag', 'Lbh sng', 'Lbh qhzo', 'Lbh yvggyr', 'Lbh shpxvat', 
        'Lbh oybbql', 'Lbh htyl', 'Lbh jrveq', 'Lbh ubcryrff', 'Lbh jvzcl', 
        'Lbh tbqqnz', 'Lbh oenvayrff', 'Lbh fybj', 'Lbh cebhq', 
        'Lbh sng-zbhgurq', 'Lbh oynfgrq', 'Lbh jnfgrf', 'Lbh qbcrl', 
        'Lbh evtug', 'Lbh jbeguyrff', 'Lbh fgvaxl']
    c = ['cvrpr bs fuvg!', 'nffubyr!', 'qbahg!', 'vqvbg!', 'wrex!', 'cvt!', 
        'qbaxrl!', 'shpxsnpr!', 'jnaxre!', 'pbj!', 'qhzob!', 'vzorpvyr!', 
        'ovgpu!', 'zhccrg!', 'onanan!', 'qvpxsnpr!', 'terzyva!', 'obmb!', 
        'shpxre!', 'sngnff!', 'qbt!', 'cynax!', 'qvpx!', 'tvenssr!', 'gbffre!', 
        'pelonol!', 'fnaqjvpu!']

    seed(time())
    return encode(choice(a), 'rot13'), encode(choice(b), 'rot13'), encode(choice(c), 'rot13')

if __name__=="__main__":
    print("Gordon Ramsay says:")
    print("\t-", *insult())