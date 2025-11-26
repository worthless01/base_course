import constant_module as cm

def mechanical_energy():
    ep = cm.m * cm.g * cm.h
    ek = (cm.m * cm.v ** 2) / 2
    e = ep / ek

    return e

print(f'энергия: {mechanical_energy()} ')
