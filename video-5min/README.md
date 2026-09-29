# Vídeo 5 min — "¿Qué pasaría si una IA llevara tu marketing 30 días?"

Canal faceless · estilo BRIGHT SIDE / GENIAL · **Seedance 2.0 · 1080p · 16:9 · 24 fps**

- **Duración total:** 30 planos × 10 s = **5:00**
- **Narración:** ~560 palabras en español, 1 línea por plano (7–8 s de voz + 2–3 s de respiro para música/SFX); voz en off, sin presentador en cámara
- **Audio de Seedance:** genera cada plano **sin diálogo**; la voz en off se graba aparte (TTS o locutor) para que el ritmo sea uniforme. Deja activado el sonido ambiente/SFX o desactívalo y usa una pista de música (ver `assemble.sh`).

---

## Paso 0 — Referencias de personaje (obligatorio para la coherencia)

Genera primero estas 3 imágenes (texto a imagen, 16:9, 1080p) y adjúntalas como **imágenes de referencia** en cada plano donde aparezcan. Seedance 2.0 admite varias imágenes de referencia; sin ellas, Laura y Nova cambiarán de aspecto entre planos.

| Ref | Prompt |
|---|---|
| `REF_LAURA` | Character turnaround sheet, 30-year-old woman, warm brown wavy hair in a loose bun, mustard-yellow cardigan over white t-shirt, friendly expressive face, 2D flat vector cartoon style like an educational YouTube animation, clean outlines, soft shading, plain light background, front / side / 3-4 view |
| `REF_NOVA` | Character sheet of a cute AI mascot: small floating glowing blue bubble with a simple smiling face (two oval eyes, curved mouth), soft cyan glow, tiny sparkle particles, 2D flat vector cartoon style, plain light background, happy / thinking / surprised expressions |
| `REF_SHOP` | Cozy small candle workshop interior, wooden shelves full of handmade candles in amber jars, laptop on a workbench, warm lamp light, 2D flat vector cartoon background, no people |

**Prefijo de estilo** (pégalo al inicio de *cada* prompt de vídeo):

> `2D flat vector cartoon animation, educational YouTube explainer style, clean outlines, bright saturated colors, smooth motion, 16:9, no text, no subtitles, no dialogue.`

> Los rótulos de texto se añaden en edición, no en Seedance (los modelos de vídeo escriben mal el texto).

---

## Paso 1 — Lista de planos

Formato: **# · tiempo · refs** → *narración (VO)* → `prompt de Seedance` → **rótulo en pantalla** (opcional, en edición).

### GANCHO (0:00–0:40)

**01 · 0:00 · REF_LAURA**
VO: *Son las siete de la mañana. Todavía no has tomado café… y tu tienda ya ha vendido más que en toda la semana pasada.*
`Dark bedroom at dawn, blue light through curtains. The woman from the reference wakes up in bed as her phone on the nightstand lights up and buzzes repeatedly, notification bubbles popping out of it. She rubs her eyes. Slow push-in.`

**02 · 0:10 · REF_LAURA**
VO: *No has publicado nada. No has respondido ningún mensaje. Alguien lo ha hecho por ti.*
`Close-up: the woman holds the glowing phone, eyes wide with shock, jaw dropping; icons of shopping bags and hearts rain out of the screen. Quick zoom in on her face, comic surprise.`

**03 · 0:20 · REF_NOVA**
VO: *Ese "alguien" no es una persona. Es una inteligencia artificial. Y no, esto ya no es ciencia ficción.*
`The glowing blue bubble AI mascot pops out of the phone screen with a burst of sparkles, floats in the air and waves cheerfully at the camera. Soft blue light fills the dark room.`

**04 · 0:30 · —**
VO: *Hoy vas a ver qué pasaría si una IA llevara tu marketing durante treinta días. Y lo del día treinta es lo que casi nadie espera.*
`A giant wall calendar with 30 squares; red cross marks appear rapidly one after another from day 1 to day 29, then day 30 glows gold with a question mark. Camera dolly right.`
**Rótulo:** `30 DÍAS · 1 IA`

### DÍA 1 — ESCUCHAR (0:40–1:20)

**05 · 0:40 · REF_LAURA, REF_SHOP**
VO: *Día uno. Laura tiene una pequeña tienda de velas y le hace a la IA la pregunta de siempre: ¿cómo vendo más?*
`In the cozy candle workshop, the woman sits at the workbench and types on her laptop, skeptical expression, one eyebrow raised. Steam rises from a coffee mug. Medium shot.`

**06 · 0:50 · REF_NOVA, REF_LAURA**
VO: *Pero la IA no le da consejos. Le hace preguntas. ¿Quién es tu cliente? ¿Por qué compra? ¿Cuándo?*
`The blue AI mascot floats above the laptop and releases three large empty speech bubbles with question marks that drift toward the woman; she leans back, blinking, confused.`
**Rótulo:** `¿QUIÉN? ¿POR QUÉ? ¿CUÁNDO?`

**07 · 1:00 · REF_NOVA**
VO: *Así que la IA lee todas las reseñas de sus clientes. Y descubre algo curioso: casi nadie compra velas para decorar.*
`The AI mascot flies through a swirling tunnel of floating review cards with five-star ratings; some cards glow and fly toward it like magnets. Dynamic tracking shot.`

**08 · 1:10 · —**
VO: *Las compran para regalar… y para desconectar después del trabajo. Tus clientes ya te están diciendo qué vender.*
`Split scene: left, a person happily unwrapping a gift box with a candle; right, a tired person relaxing in a bubble bath with a lit candle, shoulders dropping. Gentle camera pan between them.`
**Rótulo:** `REGALO · RELAX`

### DÍAS 2–7 — PROBAR (1:20–2:00)

**09 · 1:20 · REF_NOVA**
VO: *Durante la primera semana, la IA convierte eso en contenido: posts, vídeos cortos, emails. Y siempre, tres versiones de cada cosa.*
`The AI mascot spins like a juggler as colorful cards shaped like social posts, short video frames and envelopes shoot out around it in a circle. Energetic motion, sparkles.`

**10 · 1:30 · —**
VO: *¿Por qué tres? Porque nadie sabe qué va a funcionar hasta que lo prueba. Ni siquiera los expertos.*
`Three cartoon ad cards line up on a race track as runners; a starter pistol puffs smoke; they sprint and one card pulls far ahead of the others. Side tracking shot, comedic.`
**Rótulo:** `TEST A/B`

**11 · 1:40 · —**
VO: *Pausa un segundo: ¿qué anuncio crees que ganó? ¿"Velas de soja 100 % natural"… o "Tu baño del domingo merece esto"?*
`Two large blank framed posters side by side on a stage under spotlights, a big pulsing pause icon floating between them, audience silhouettes in the foreground. Static wide shot.`
**Rótulo:** `A) Velas 100 % soja · B) Tu baño del domingo merece esto`

**12 · 1:50 · —**
VO: *Ganó la B. Las emociones casi siempre ganan a las características. No vendas velas: vende la calma.*
`The right poster lights up with golden confetti and a trophy pops above it; the scene then dissolves into a calm candlelit bathroom with soft steam. Slow push-in.`
**Rótulo:** `NO VENDAS VELAS. VENDE LA CALMA.`

### DÍAS 8–14 — 24/7 (2:00–2:30)

**13 · 2:00 · REF_LAURA**
VO: *Segunda semana. Tres de la madrugada. Un cliente escribe: "¿Tenéis velas sin olor para alguien alérgico?"*
`Night, bedroom lit by moonlight, a wall clock shows 3:00; the woman sleeps peacefully while her phone on the nightstand glows with an incoming message bubble. Slow dolly.`

**14 · 2:10 · REF_NOVA**
VO: *Antes, ese cliente se habría ido a otra tienda. Esta vez, la IA responde en segundos, recomienda un producto… y cierra la venta.*
`The AI mascot zips out of the phone, types super fast on a tiny keyboard with blur lines, then a green checkmark and a shopping bag icon pop up with a burst. Fast, playful.`

**15 · 2:20 · REF_LAURA, REF_NOVA**
VO: *Pero Laura revisa cada respuesta por la mañana. La IA atiende. Ella decide.*
`Morning kitchen, the woman sips coffee reading her phone and nods approvingly; the small AI mascot floats beside her shoulder, giving a thumbs-up. Warm sunlight, medium shot.`
**Rótulo:** `LA IA RESPONDE · TÚ SUPERVISAS`

### DÍA 15 — EL GIRO (2:30–3:10)

**16 · 2:30 · REF_NOVA**
VO: *Y justo cuando todo iba perfecto… el día quince, la IA publica un anuncio raro. Exagerado. Frío.*
`The scene suddenly turns red; an alarm light spins; a loud, over-the-top cartoon billboard with flashing stars and exclamation shapes rises from the ground; the AI mascot looks proud but clueless.`

**17 · 2:40 · —**
VO: *Y la gente lo nota. "¿Esto lo ha escrito un robot?"*
`A rain of angry and confused emoji bubbles and thumbs-down icons pours down from the sky onto a smartphone screen; the phone shakes. Low-angle shot, dramatic.`
**Rótulo:** `"¿Esto lo ha escrito un robot?"`

**18 · 2:50 · REF_LAURA, REF_NOVA**
VO: *Aquí está la lección más importante: la IA es tan buena como las instrucciones que le das.*
`The woman and the AI mascot sit facing each other across a small table like a meeting; the mascot looks embarrassed and shrinks slightly; she smiles kindly and opens a notebook.`

**19 · 3:00 · REF_LAURA, REF_NOVA**
VO: *Juntas crean una guía de marca: cómo habla Laura y qué palabras nunca usaría. Desde ese día, todo suena a ella… solo que más rápido.*
`The woman writes in a notebook; glowing lines of light flow from the pages into the AI mascot, which changes from red to calm blue and smiles. Magical, gentle camera orbit.`
**Rótulo:** `GUÍA DE MARCA = EL ADN DE TU IA`

### DÍAS 16–29 — SUPERPODERES (3:10–4:10)

**20 · 3:10 · —**
VO: *En las dos semanas siguientes, Laura descubre cinco superpoderes que antes solo tenían las grandes marcas.*
`A treasure chest opens on a wooden table and five glowing numbered orbs float out one by one into the air, golden light rays. Push-in.`
**Rótulo:** `5 SUPERPODERES`

**21 · 3:20 · REF_SHOP**
VO: *Uno: fotos de producto sin estudio. Una foto con el móvil se convierte en diez escenarios distintos.*
`A single amber jar candle stays fixed in the center while the background morphs smoothly: kitchen table, snowy forest, sunset beach, spa bathroom, Christmas living room. Locked-off camera.`
**Rótulo:** `1 · FOTOS SIN ESTUDIO`

**22 · 3:30 · —**
VO: *Dos: vídeos a partir de una imagen. Esa foto quieta cobra vida para Reels y TikTok.*
`A flat printed photo of a candle lying on a desk; the flame in the photo starts flickering, the photo lifts off the desk and expands into a vertical phone screen playing a video. Smooth motion.`
**Rótulo:** `2 · FOTO → VÍDEO`

**23 · 3:40 · —**
VO: *Tres: hablar el idioma de todos. Y de repente, llegan pedidos de otros países.*
`A cartoon globe spins slowly; small parcel boxes with paper planes fly from one spot to several countries leaving dotted trails. Camera orbits the globe.`
**Rótulo:** `3 · MULTIDIOMA`

**24 · 3:50 · —**
VO: *Cuatro: publicar en el momento justo. Sus clientes compran de noche, cuando por fin se relajan.*
`A big cartoon clock at night; the hands spin quickly and stop at 9; a moon rises and many small shopping bag icons light up in apartment windows of a city skyline.`
**Rótulo:** `4 · EL MOMENTO JUSTO`

**25 · 4:00 · —**
VO: *Y cinco: emails que parecen escritos a mano, con el nombre de cada cliente y lo que de verdad le gusta.*
`An envelope with a wax heart seal flies across the screen and lands in a cartoon mailbox; a happy person opens it and hugs the letter. Soft pastel colors.`
**Rótulo:** `5 · PERSONALIZACIÓN`

### DÍA 30 — LA REVELACIÓN (4:10–4:40)

**26 · 4:10 · REF_LAURA**
VO: *Día treinta. Laura abre sus estadísticas. Las ventas han subido. Pero eso no es lo más sorprendente.*
`Confetti falls; the woman looks at a laptop showing a cartoon bar chart rising steeply; she covers her mouth with both hands, amazed. Medium close-up.`

**27 · 4:20 · REF_LAURA**
VO: *Lo que de verdad ha cambiado es su tiempo. Antes el marketing le comía el día. Ahora le dedica una hora.*
`A giant hourglass beside the woman; instead of sand, golden clock-shaped coins flow back up into her open hands. Magical light, slow camera pull back.`

**28 · 4:30 · REF_LAURA, REF_NOVA, REF_SHOP**
VO: *Y la IA no la reemplazó. La multiplicó. Ahora Laura tiene tiempo para crear, pensar… y hablar con sus clientes.*
`In the workshop, the woman happily pours wax into new jars; the tiny AI mascot sits on her shoulder like a pet; warm sunset light through the window. Gentle dolly in.`
**Rótulo:** `LA IA NO TE REEMPLAZA. TE REEMPLAZA QUIEN SEPA USARLA.`

### CIERRE (4:40–5:00)

**29 · 4:40 · REF_NOVA**
VO: *Resumen: deja que la IA escuche, prueba varias versiones, escribe tu guía de marca… y supervisa siempre.*
`The AI mascot floats next to a clipboard; four checkboxes on it get ticked one after another with green sparkles. Clean light background, static shot.`
**Rótulo:** `ESCUCHA · PRUEBA · GUÍA · SUPERVISA`

**30 · 4:50 · REF_LAURA, REF_NOVA**
VO: *Y ahora te toca a ti: si una IA llevara tu marketing mañana, ¿qué le pedirías primero? Te leo en los comentarios.*
`The woman and the AI mascot stand side by side in the workshop and wave goodbye to the camera; camera pulls back slowly and the scene gently fades to white.`
**Rótulo final:** tarjeta de suscripción + vídeo recomendado (los últimos 5–20 s, añade la pantalla final en YouTube Studio)

---

## Paso 2 — Ajustes en Seedance 2.0 (Higgsfield)

| Ajuste | Valor |
|---|---|
| Modelo | Seedance 2.0 |
| Resolución | 1080p |
| Relación de aspecto | 16:9 |
| Duración | 10 s por plano |
| Entrada | Texto + imágenes de referencia (las `REF_*` indicadas en cada plano) |
| Semilla | Fija la misma semilla en todos los planos si la herramienta lo permite (ayuda a mantener el estilo) |
| Audio | Sin voz; SFX/ambiente opcional |

Consejos:
- Genera **2 variantes** de los planos con personajes (01, 02, 05, 15, 18, 19, 26–28, 30) y quédate con la más fiel a las referencias.
- Si una mano o una cara salen deformes, vuelve a generar ese plano: no hace falta rehacer los demás.
- Nombra las descargas `01.mp4` … `30.mp4` y colócalas en `clips/`.

## Paso 3 — Voz en off
Graba o genera cada línea de VO (voz cálida, curiosa, español neutro o de España según tu audiencia) como **un archivo por plano**: `vo/01.mp3` … `vo/30.mp3`. Cada línea dura 7–8 s a ritmo normal; el script de montaje la rellena con silencio hasta 10 s (o la corta si se pasa), así voz e imagen nunca se desincronizan. Si una línea pasa de 10 s, acórtala o habla un poco más rápido.

## Paso 4 — Montaje
```bash
./assemble.sh            # clips/NN.mp4 + vo/NN.mp3 (+ music.mp3 opcional) → ia-marketing-5min.mp4
```
Después añade los rótulos en CapCut, Premiere o DaVinci (fuente gruesa, amarillo/blanco con borde negro, al estilo Bright Side) y subtítulos automáticos.

## Paso 5 — Publicación (canal faceless)
- **Título:** ¿Qué pasaría si una IA llevara tu marketing durante 30 días? (El día 30 lo cambia todo)
- **Miniatura:** Laura sorprendida frente al portátil + Nova sonriendo con un gráfico que se dispara; texto grande **"¿30 DÍAS?"** en amarillo.
- **Capítulos:** 0:00 Gancho · 0:40 Día 1 · 1:20 Días 2–7 · 2:00 Días 8–14 · 2:30 Día 15 · 3:10 Superpoderes · 4:10 Día 30 · 4:40 Resumen
- **Divulgación:** YouTube pide marcar el contenido realista generado o alterado con IA. Este vídeo es animación claramente ficticia, pero revisa la casilla de "contenido alterado" al subirlo si tienes dudas.
