"""Coche en escena de estudio: suelo, sombra de contacto, sombra ambiente, reflejo y luz."""
import pathlib
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
from scipy import ndimage as nd

HERE = pathlib.Path(__file__).parent
W, H = 1414, 2000
rng = np.random.default_rng(3)
x = np.linspace(0, 1, W)[None, :]
y = np.linspace(0, 1, H)[:, None]


def hexc(h):
    h = h.lstrip('#')
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)


def sig(t):
    return 1 / (1 + np.exp(-np.clip(t, -40, 40)))


def lerp(a, b, t):
    return a * (1 - t[..., None]) + b * t[..., None]


def backdrop(p, horizon):
    one = np.ones((H, W))
    t_wall = np.clip(y / horizon, 0, 1) * np.ones((1, W))
    wall = lerp(hexc(p['wall_top']) * one[..., None], hexc(p['wall_bot']) * one[..., None], t_wall)
    # arco suave en la pared (firma de los fondos)
    d = np.sqrt((x - 0.78) ** 2 + ((y - 0.04) * 0.9) ** 2) - 0.34
    arc = np.exp(-(d / 0.06) ** 2) * sig((horizon - 0.04 - y) / 0.06) * sig((x - 0.25) / 0.08)
    wall = lerp(wall, hexc(p['arc']) * one[..., None], arc * 0.7)
    # suelo con curva de ciclorama
    t_floor = np.clip((y - horizon) / (1 - horizon), 0, 1) * np.ones((1, W))
    floor = lerp(hexc(p['floor_near']) * one[..., None], hexc(p['floor_far']) * one[..., None], t_floor ** 0.8)
    a = sig((y - horizon) / 0.035) * np.ones((1, W))
    img = lerp(wall, floor, a)
    return img


def render(p, name, car_path=HERE / 'coche_recorte.png', car_w=1180, base_y=1420):
    horizon = 0.56
    img = backdrop(p, horizon)

    car = Image.open(car_path).convert('RGBA')
    s = car_w / car.width
    car = car.resize((car_w, round(car.height * s)), Image.LANCZOS)
    cw, ch = car.size
    ox, oy = (W - cw) // 2, base_y - ch
    alpha = np.asarray(car)[..., 3] / 255.0

    # Luz puntual cenital sobre el suelo, centrada en el coche
    cx, cy = (ox + cw / 2) / W, base_y / H
    pool = np.exp(-(((x - cx) / 0.55) ** 2 + ((y - cy) / 0.16) ** 2))
    img = img * (1 + 0.10 * pool[..., None])

    # Sombras: huella de las 4 ruedas sobre el suelo (coordenadas del recorte original,
    # 1126 px de ancho). Delanteras/traseras visibles + las ocultas tras la carrocería.
    k = cw / 1126
    def P(px, py):
        return ox + px * k, oy + py * k
    front, rear = P(522, 513), P(1022, 427)
    front_far, rear_far = P(250, 468), P(790, 400)
    from PIL import ImageDraw
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).polygon([front, rear, rear_far, front_far], fill=255)
    foot = np.asarray(m, float) / 255
    sh = 0.55 * nd.gaussian_filter(foot, 18) + 0.35 * nd.gaussian_filter(foot, 55)
    for (X, Y), r, o in ((front, 52, 0.95), (rear, 40, 0.9), (front_far, 50, 0.45)):
        blob = np.exp(-(((x * W - X) / r) ** 2 + ((y * H - Y) / (r * 0.16)) ** 2))
        sh = sh + o * blob
    sh = np.clip(sh, 0, 0.9)
    img = lerp(img, hexc(p['shadow']) * np.ones((H, W, 1)), sh)

    # Ajuste de luz del coche: algo más de contraste, oclusión en la parte baja
    car_rgb = ImageEnhance.Contrast(car.convert('RGB')).enhance(1.06)
    c = np.asarray(car_rgb).astype(float)
    ao = 1 - 0.18 * np.clip((np.arange(ch) / ch - 0.78) / 0.22, 0, 1)[:, None]
    top = 1 + 0.05 * np.clip(1 - np.arange(ch) / (ch * 0.35), 0, 1)[:, None]
    c = np.clip(c * (ao * top)[..., None] * hexc(p['car_tint'])[None, None] / 255, 0, 255)
    # borde suave
    a = nd.gaussian_filter(nd.grey_erosion(alpha, size=5), 0.8)[..., None]
    region = img[oy:oy + ch, ox:ox + cw]
    img[oy:oy + ch, ox:ox + cw] = region * (1 - a) + c * a

    # Viñeta y grano
    img *= (1 - 0.12 * ((x - 0.5) ** 2 * 2 + (y - 0.5) ** 2 * 1.4))[..., None]
    img += rng.normal(0, 3.5, (H, W, 1))
    out = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    out.save(HERE / f'{name}.png', optimize=True)
    out.save(HERE / f'{name}.jpg', quality=93)
    print('ok', name)


AMARILLO = dict(wall_top='#EBC45E', wall_bot='#F5DC93', arc='#FCEDBF',
                floor_near='#F6DE98', floor_far='#EAC466', shadow='#5E4512',
                car_tint='#FFFCF4')

if __name__ == '__main__':
    render(AMARILLO, 'coche_estudio_amarillo')
