import ac2_lp2 as animais

Cobra = animais.Cobra('Jararaca', 'verde', 2, True)

print(Cobra.botar_ovo())
print(Cobra.trocar_pele())
print(Cobra.rastejar())
print(Cobra.__dict__)

Jacare = animais.Jacare('Papo Amarelo', 'amarelado', 3, 30)

print(Jacare.botar_ovo())
print(Jacare.atacar())
print(Jacare.dormir())
print(Jacare.__dict__)

Cavalo = animais.Cavalo(
  'Pé de pano',
  'branco',
  8,
  'casco',
  'amarelo'
)

print(Cavalo.correr())
print(Cavalo.mamar())
print(Cavalo.galopar())
print(Cavalo.relinchar())
print(Cavalo.__dict__)

Cachorro = animais.Cachorro(
  'Rex',
  'caramelo',
  2,
  'pata',
  'vira-lata'
)

print(Cachorro.correr())
print(Cachorro.mamar())
print(Cachorro.latir())
print(Cachorro.rosnar())
print(Cachorro.__dict__)

Gato = animais.Gato(
  'Frajola',
  'preto',
  1,
  'fofinha'
)

print(Gato.correr())
print(Gato.mamar())
print(Gato.miar())
print(Gato.morrer())
print(Gato.morrer())
print(Gato.morrer())
print(Gato.morrer())
print(Gato.morrer())
print(Gato.morrer())
print(Gato.morrer())
print(Gato.morrer())
print(Gato.__dict__)
