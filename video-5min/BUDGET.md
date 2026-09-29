# Presupuesto Higgsfield — vídeo 5 min (límite duro: 50 créditos)

Proyecto Higgsfield: **IA Marketing 30 dias - 5min** (`f9383c8c-bcfc-4576-b32d-d33fa4a0d844`).
Precios consultados con `get_cost` el 2026-09-29 antes de generar nada.

## Precios comparados

| Tipo | Modelo | Ajustes | Créditos |
|---|---|---|---|
| Imagen | Z Image | 16:9 (sin referencias) | 0.15 |
| Imagen | **GPT Image 2.5 (Flare)** | 1k, low, 16:9, admite referencias | **0.25** |
| Imagen | Seedream 5.0 Flash | 2K, 16:9 (falló con error 422, no cobró) | 0.5 |
| Imagen | GPT Image 2 | 1k, low | 0.5 |
| Imagen | Nano Banana / NB2 Lite | 1k | 1 |
| Vídeo | **Seedance 2.0 Mini** | 480p, 10 s, sin audio | **5** |
| Vídeo | Seedance 2.0 Mini | 720p, 10 s, sin audio | 10 |
| Vídeo | Kling 3.0 Turbo / Grok Video | 3 s | 4.5 |
| Vídeo | Veo 3.1 Lite | 4 s | 6 |
| Vídeo | Seedance 2.5 | 480p, 4 s | 12 |
| Voz | Seed Audio 1.0 | por longitud (~0.8 por línea) | ~24 total |
| Voz | **TTS V2 · ElevenLabs** | por línea (≤132 caracteres) | **≤0.45** |
| Voz | TTS V2 · Cozy Voice | por línea | 0.15 |

TTS gratis local (edge-tts, gTTS) no disponible: la red del entorno bloquea sus servidores.

## Resultado (gasto real, verificado con `balance` y `transactions`)

Saldo inicial 572.98 → saldo final 537.43 = **35.55 créditos gastados** (límite: 50).

| Partida | Modelo | Cantidad | Créditos |
|---|---|---|---|
| Referencias REF_LAURA / REF_NOVA / REF_SHOP | GPT Image 2.5 low 1k | 3 × 0.25 | 0.75 |
| Imagen fija por plano (01–30), con referencias | GPT Image 2.5 low 1k | 30 × 0.25 | 7.50 |
| Voz en off (30 líneas, voz "Marisol") | TTS V2 · ElevenLabs | 30 × 0.30–0.45 | 11.40 |
| Reintento de 2 líneas atascadas en cola (16, 25) | TTS V2 · ElevenLabs | 2 × 0.45 | 0.90 |
| Animación IA planos 01, 16 y 26 | Seedance 2.0 Mini 480p 10 s, sin audio | 3 × 5 | 15.00 |
| **Total** | | | **35.55** |

Planos 02–15, 17–25 y 27–30: imagen fija con movimiento Ken Burns (zoom/paneo alterno) hecho con ffmpeg — 0 créditos.
Rótulos en pantalla (amarillo con borde negro) quemados con ffmpeg drawtext — 0 créditos. Sin música de fondo.

## Montaje

La red de este entorno bloquea la CDN de Higgsfield, así que el montaje se hace en el sandbox de Higgsfield
(`remote/build.sh` + `remote/manifest.tsv` + `remote/captions.tsv`), y el MP4 final se sube a la biblioteca de
medios de Higgsfield (media id `d42f05bb-c662-482d-97a4-b282a5b80ac0`).

Salida verificada con ffprobe: 300.0 s, 1920×1080, 24 fps, H.264 + AAC, 97 MB.
