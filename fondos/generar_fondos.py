"""Fondos abstractos tipo duna desenfocada (amarillo y gris claro), A4 vertical."""
import pathlib
import numpy as np
from PIL import Image, ImageFilter

W, H = 1414, 2000
OUT = pathlib.Path(__file__).parent
rng = np.random.default_rng(7)

x = np.linspace(0, 1, W)[None, :]
y = np.linspace(0, 1, H)[:, None]


def hexc(h):
    h = h.lstrip('#')
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)


def sig(t):
    return 1 / (1 + np.exp(-np.clip(t, -40, 40)))


def vgrad(c_top, c_bot, y0, y1):
    t = np.clip((y - y0) / (y1 - y0), 0, 1)[..., None]
    return hexc(c_top) * (1 - t) + hexc(c_bot) * t


def hgrad(base, c, amount):
    return base * (1 - amount[..., None]) + hexc(c) * amount[..., None]


def render(p, name):
    # 1. Cielo / fondo superior
    img = vgrad(p['sky_top'], p['sky_bot'], 0.0, 0.55) * np.ones((H, W, 1))

    # 2. Cinta curva suave en la parte alta (como la referencia 1), muy difusa
    cx, cy, r = 0.78, 0.06, 0.34
    d = np.sqrt((x - cx) ** 2 + ((y - cy) * 0.9) ** 2) - r
    ribbon = np.exp(-(d / 0.06) ** 2) * sig((0.60 - y) / 0.08) * sig((x - 0.25) / 0.08)
    img = img * (1 - ribbon[..., None] * p['ribbon_a']) + hexc(p['ribbon']) * ribbon[..., None] * p['ribbon_a']

    # 3. Gran duna: borde que cruza de izquierda a derecha
    c1 = 0.50 + 0.03 * np.sin(x * 2.4) + 0.05 * x
    soft1 = 0.004 + 0.05 * x ** 1.6           # nítido a la izquierda, desenfocado a la derecha
    dune = sig((y - c1) / soft1)
    face = vgrad(p['dune_top'], p['dune_bot'], 0.5, 0.95) * np.ones((H, W, 1))
    face = hgrad(face, p['dune_light'], np.clip((x - 0.35) * 1.3, 0, 1) * 0.8 * np.ones_like(y))
    img = img * (1 - dune[..., None]) + face * dune[..., None]

    # 4. Sombra en cuña bajo la cresta (lado izquierdo)
    c2 = 0.74 - 0.30 * x ** 1.3
    wedge = dune * sig((c2 - y) / 0.03) * sig((0.62 - x) / 0.10)
    img = img * (1 - wedge[..., None] * 0.85) + hexc(p['shadow']) * wedge[..., None] * 0.85

    # 5. Duna del primer plano
    c3 = 0.80 - 0.10 * x + 0.025 * np.sin(x * 5)
    fore = sig((y - c3) / (0.008 + 0.03 * x))
    fcol = vgrad(p['fore_top'], p['fore_bot'], 0.75, 1.0) * np.ones((H, W, 1))
    img = img * (1 - fore[..., None]) + fcol * fore[..., None]

    # 6. Desenfoque general, viñeta y grano
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(5))
    a = np.asarray(im).astype(float)
    vig = 1 - 0.10 * ((x - 0.5) ** 2 * 2 + (y - 0.5) ** 2 * 1.5)
    a *= vig[..., None]
    grain = rng.normal(0, 4.5, (H, W, 1)) + rng.normal(0, 1.5, (H, W, 3))
    a = np.clip(a + grain, 0, 255).astype(np.uint8)
    Image.fromarray(a).save(OUT / f'{name}.png', optimize=True)
    Image.fromarray(a).save(OUT / f'{name}.jpg', quality=93)
    print('ok', name)


AMARILLO = dict(
    sky_top='#F1CF6E', sky_bot='#F7E2A0', ribbon='#FFF1C4', ribbon_a=0.75,
    dune_top='#E9BE55', dune_bot='#F3D58A', dune_light='#FBEBB8',
    shadow='#B98A2E', fore_top='#FAE9B6', fore_bot='#F0CF82',
)
GRIS = dict(
    sky_top='#CBCBC9', sky_bot='#E2E2E0', ribbon='#F4F4F2', ribbon_a=0.75,
    dune_top='#C4C4C2', dune_bot='#DCDCDA', dune_light='#EFEFED',
    shadow='#9C9C9A', fore_top='#EEEEEC', fore_bot='#D9D9D7',
)

if __name__ == '__main__':
    render(AMARILLO, 'fondo_amarillo')
    render(GRIS, 'fondo_gris_claro')
