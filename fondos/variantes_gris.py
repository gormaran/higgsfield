import sys
sys.path.insert(0, 'fondos')
import generar_fondos as g
from PIL import Image

V = {
 # A: gris perla muy luminoso, sombra suave
 'gris_A_perla': dict(sky_top='#DCDCDE', sky_bot='#EEEEF0', ribbon='#FAFAFC', ribbon_a=0.8,
   dune_top='#D6D6D9', dune_bot='#E8E8EA', dune_light='#F7F7F8', shadow='#B6B6BA',
   fore_top='#F3F3F4', fore_bot='#E2E2E4'),
 # B: gris cálido tipo piedra/arena (como la referencia 3 pero más claro)
 'gris_B_calido': dict(sky_top='#D3D0CB', sky_bot='#E7E4DF', ribbon='#F6F3EE', ribbon_a=0.75,
   dune_top='#CCC8C1', dune_bot='#E0DCD5', dune_light='#F2EFEA', shadow='#A9A39A',
   fore_top='#EEEBE6', fore_bot='#DAD6CF'),
 # C: gris azulado frío y suave
 'gris_C_azulado': dict(sky_top='#CDD3D8', sky_bot='#E3E7EB', ribbon='#F4F7F9', ribbon_a=0.75,
   dune_top='#C6CDD3', dune_bot='#DCE1E6', dune_light='#EEF2F5', shadow='#9EA8B1',
   fore_top='#EAEEF1', fore_bot='#D5DBE0'),
}
for k, p in V.items():
    g.render(p, k)
ims = [Image.open(f'fondos/{k}.png') for k in V]
w, h = ims[0].size
c = Image.new('RGB', (w * 3 + 80, h), 'white')
for i, im in enumerate(ims):
    c.paste(im, (i * (w + 40), 0))
pass
