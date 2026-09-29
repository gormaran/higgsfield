"""Shot list for the low-budget build: one still per shot (+ which refs to attach)."""
import json, re, pathlib

STYLE = ("2D flat vector cartoon illustration, educational YouTube explainer style like Bright Side, "
         "clean outlines, bright saturated colors, 16:9, no text, no letters, no subtitles. ")
LAURA = "The woman is exactly the character from the reference sheet (brown wavy hair in a loose bun, mustard-yellow cardigan, white t-shirt). "
NOVA = "The AI mascot is exactly the glowing blue bubble character from the reference sheet. "
SHOP = "Setting: the candle workshop from the reference image. "

# (shot, refs, scene description for a single still frame)
SHOTS = [
 (1, "L", "Dark bedroom at dawn, blue light through curtains. The woman wakes up in bed rubbing her eyes while her phone on the nightstand lights up with many notification bubbles popping out."),
 (2, "L", "Close-up: the woman holds a glowing phone, eyes wide with shock, jaw dropping; shopping bag and heart icons rain out of the screen. Comic surprise."),
 (3, "N", "The glowing blue bubble AI mascot pops out of a phone screen in a burst of sparkles, floating in a dark room and waving cheerfully at the viewer, soft blue light."),
 (4, "", "A giant wall calendar with 30 squares; red cross marks on days 1 to 29, day 30 glowing gold with a big question mark."),
 (5, "LS", "The woman sits at the workbench typing on her laptop with a skeptical expression, one eyebrow raised; steam rises from a coffee mug. Medium shot."),
 (6, "NL", "The blue AI mascot floats above the laptop and releases three large empty speech bubbles with question marks toward the woman, who leans back, confused."),
 (7, "N", "The AI mascot flies through a swirling tunnel of floating customer review cards with five-star ratings; some cards glow and fly toward it like magnets."),
 (8, "", "Split scene: left, a happy person unwrapping a gift box with a candle; right, a tired person relaxing in a bubble bath with a lit candle."),
 (9, "N", "The AI mascot juggles colorful cards shaped like social media posts, short video frames and envelopes flying around it in a circle, sparkles."),
 (10, "", "Three cartoon ad cards with little legs racing on a running track like athletes; one card pulls far ahead of the others. Comedic side view."),
 (11, "", "Two large blank framed posters side by side on a stage under spotlights, a big pause symbol floating between them, audience silhouettes in the foreground."),
 (12, "", "The right poster on a stage lights up with golden confetti and a trophy above it; beside it a calm candlelit bathroom with soft steam."),
 (13, "L", "Night bedroom lit by moonlight, a wall clock at 3 o'clock; the woman sleeps peacefully while her phone on the nightstand glows with an incoming message bubble."),
 (14, "N", "The AI mascot zooms out of a phone and types super fast on a tiny keyboard with speed lines; a green checkmark and a shopping bag icon pop up."),
 (15, "LN", "Morning kitchen in warm sunlight: the woman sips coffee reading her phone and nods approvingly; the small AI mascot floats beside her shoulder giving a thumbs-up."),
 (16, "N", "The scene turns red with a spinning alarm light; a loud, over-the-top cartoon billboard with flashing stars and exclamation shapes rises; the AI mascot looks proud but clueless."),
 (17, "", "A rain of angry and confused emoji faces and thumbs-down icons pours from the sky onto a shaking smartphone. Low-angle dramatic shot."),
 (18, "LN", "The woman and the AI mascot sit facing each other across a small table like a meeting; the mascot looks embarrassed and small; she smiles kindly and opens a notebook."),
 (19, "LN", "The woman writes in a notebook; glowing ribbons of light flow from the pages into the AI mascot, which glows calm blue and smiles. Magical mood."),
 (20, "", "A treasure chest open on a wooden table with five glowing golden orbs floating out into the air, golden light rays."),
 (21, "S", "A single amber jar candle in the center of the frame, the background split into five panels: kitchen table, snowy forest, sunset beach, spa bathroom, Christmas living room."),
 (22, "", "A printed photo of a candle lying on a desk transforms into a vertical smartphone playing a video of the flickering candle."),
 (23, "", "A cartoon globe with small parcel boxes and paper planes flying from one spot to several countries, leaving dotted trails."),
 (24, "", "A big cartoon clock at night showing 9 o'clock, a moon rising over a city skyline where many apartment windows show small glowing shopping bag icons."),
 (25, "", "An envelope with a red wax heart seal landing in a cartoon mailbox; a happy person opens a letter and hugs it. Soft pastel colors."),
 (26, "L", "Confetti falls; the woman looks at a laptop showing a cartoon bar chart rising steeply; she covers her mouth with both hands, amazed. Medium close-up."),
 (27, "L", "A giant hourglass beside the woman; instead of sand, golden clock-shaped coins flow up into her open hands. Magical light."),
 (28, "LNS", "The woman happily pours wax into new candle jars in the workshop; the tiny AI mascot sits on her shoulder like a pet; warm sunset light through the window."),
 (29, "N", "The AI mascot floats next to a clipboard with four checkboxes, all ticked with green checkmarks and sparkles. Clean light background."),
 (30, "LN", "The woman and the AI mascot stand side by side in the candle workshop waving goodbye to the viewer, warm soft light."),
]

def prompt(shot):
    n, refs, desc = shot
    p = STYLE
    if "L" in refs: p += LAURA
    if "N" in refs: p += NOVA
    if "S" in refs: p += SHOP
    return p + desc

def vo_lines(readme="README.md"):
    t = pathlib.Path(readme).read_text()
    return re.findall(r'^VO: \*(.+?)\*\s*$', t, re.M)

if __name__ == "__main__":
    print(json.dumps([{"shot": s[0], "refs": s[1], "prompt": prompt(s)} for s in SHOTS], ensure_ascii=False, indent=1))
