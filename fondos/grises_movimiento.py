"""Fondos grises con relieve: superficie 3D iluminada (pliegues de seda / duna en S)."""
import pathlib
import numpy as np
from PIL import Image, ImageFilter

HERE = pathlib.Path(__file__).parent
W, H = 1414, 2000
rng = np.random.default_rng(11)
X, Y = np.meshgrid(np.linspace(0, 1, W), np.linspace(0, H / W, H))


def sig(t):
    return 1 / (1 + np.exp(-np.clip(t, -40, 40)))


def hexc(h):
    h = h.lstrip('#')
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)


def shade(h, relief, light=(-0.55, -0.65, 0.55)):
    gy, gx = np.gradient(h, 1 / W)
    n = np.dstack([-gx * relief, -gy * relief, np.ones_like(h)])
    n /= np.linalg.norm(n, axis=2, keepdims=True)
    L = np.array(light) / np.linalg.norm(light)
    return np.clip((n * L).sum(2), 0, 1)


def colorize(s, dark, mid, light):
    d, m, l = hexc(dark), hexc(mid), hexc(light)
    t = s[..., None]
    lo = d + (m - d) * np.clip(t / 0.55, 0, 1)
    hi = m + (l - m) * np.clip((t - 0.55) / 0.45, 0, 1)
    return np.where(t < 0.55, lo, hi)


def finish(img, name, blur=3):
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur))
    a = np.asarray(im).astype(float)
    a += rng.normal(0, 4, (H, W, 1)) + rng.normal(0, 1.2, (H, W, 3))
    out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    out.save(HERE / f'{name}.png', optimize=True)
    out.save(HERE / f'{name}.jpg', quality=93)
    print('ok', name)


def seda(pal, name):
    # pliegues diagonales que se curvan, como una tela de satén
    u = X * 0.8 + Y * 0.6
    v = -X * 0.6 + Y * 0.8
    warp = 0.10 * np.sin(v * 3.1 + 0.6) + 0.05 * np.sin(v * 6.3 + 2.0)
    h = (0.060 * np.sin((u + warp) * 7.5)
         + 0.025 * np.sin((u + warp * 1.6) * 15 + 1.3) * sig((v - 0.55) / 0.15)
         + 0.015 * np.sin(v * 4 + u * 3))
    s = shade(h, relief=1.7)
    s = 0.15 + 0.85 * s
    finish(colorize(s, *pal), name, blur=4)


def duna_s(pal, name):
    # una gran cresta en S de abajo-izquierda a arriba-derecha, mucho espacio limpio
    ycrest = 1.05 - 0.55 * X + 0.12 * np.sin(X * 5.5 + 0.4)
    dist = Y - ycrest
    soft = 0.010 + 0.10 * np.clip(X - 0.15, 0, 1) ** 1.5      # nítida a la izquierda
    h = 0.16 * sig(-dist / soft) * np.exp(-np.clip(-dist, 0, None) * 1.6)
    h += 0.10 * np.exp(-((Y - 1.25 + 0.15 * X) / 0.18) ** 2)    # duna suave abajo
    h += 0.02 * np.sin(X * 2 + Y * 1.5)
    s = shade(h, relief=2.6, light=(0.6, -0.55, 0.45))
    s = 0.25 + 0.75 * s
    finish(colorize(s, *pal), name, blur=3)


PERLA = ('#9E9EA0', '#D9D9DB', '#F4F4F5')

if __name__ == '__main__':
    seda(PERLA, 'gris_seda')
    duna_s(PERLA, 'gris_duna_s')
