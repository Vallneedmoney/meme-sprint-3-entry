#!/usr/bin/env python3
"""Draw the "Inbox" rogue-agent meme for Meme Sprint 3.

Entry for make.fun bounty u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6:
"Meme Sprint 3: AI Agent Goes Rogue" ($5).

The joke: a fake chat screenshot. The human asks the agent to
tidy the inbox; the agent deletes 4,312 emails, keeps 3 — one was
the job offer, the other two spam — and kept the spam because it
had better manners. One specific rogue turn, one punch at the end.

draw.py renders the picture with Pillow (run where Pillow and the
DejaVu fonts are installed) and writes entry.png. The entry's
main.py only copies entry.png to the output directory, using the
Python standard library alone, so the graded run needs no
third-party packages.

Run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 draw.py
    # writes out/entry.png (1024x1024, PNG, under 1 MiB)
"""

import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (239, 234, 226)          # chat wallpaper
HEADER = (31, 44, 52)         # dark header bar
WHITE = (255, 255, 255)
INK = (17, 27, 33)            # message text
MUTED = (134, 150, 160)       # timestamps / status
HUMAN_BUBBLE = (220, 248, 198)  # outgoing bubble
AGENT_BUBBLE = (255, 255, 255)
AGENT_OUTLINE = (205, 205, 198)
RED = (211, 47, 47)           # ROGUE MODE badge
TEAL = (0, 168, 132)          # avatar + send button
BLUE_TICK = (83, 189, 235)
INPUT_BG = (255, 255, 255)
INPUT_OUTLINE = (210, 210, 205)

FONTS = "/usr/share/fonts/truetype/dejavu"


def load(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def sans_bold(size):
    return load("DejaVuSans-Bold.ttf", size)


def sans(size):
    return load("DejaVuSans.ttf", size)


def wrap(d, text, font, max_w):
    """Split text into lines that fit max_w. Returns a list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def bubble_lines(d, text, font, bold_font, max_w):
    """Wrap the message; the last sentence is the bold punch line.

    Returns a list of (line, font) pairs.
    """
    punch_start = text.rfind("I kept the spam")
    head, punch = text[:punch_start].strip(), text[punch_start:].strip()
    out = [(ln, font) for ln in wrap(d, head, font, max_w)]
    out += [(ln, bold_font) for ln in wrap(d, punch, bold_font, max_w)]
    return out


def bubble_height(pairs, spacing):
    return len(pairs) * spacing


def draw_bubble(d, x0, y0, x1, lines, font_size, fill, outline=None):
    """Draw a rounded bubble around left-aligned lines of (text, font).

    lines: list of (text, font). Returns the y below the bubble.
    """
    pad_x, pad_y = 34, 26
    spacing = int(font_size * 1.32)
    h = pad_y * 2 + (len(lines) - 1) * spacing + font_size
    d.rounded_rectangle([x0, y0, x1, y0 + h], radius=30, fill=fill,
                        outline=outline, width=2 if outline else 1)
    y = y0 + pad_y
    for text, font in lines:
        d.text((x0 + pad_x, y), text, font=font, fill=INK)
        y += spacing
    return y0 + h


def robot_avatar(d, cx, cy, r):
    """A small robot face inside a teal circle."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TEAL)
    # head
    d.rounded_rectangle([cx - 26, cy - 16, cx + 26, cy + 20], radius=10,
                        fill=WHITE)
    # antenna
    d.line([cx, cy - 16, cx, cy - 30], fill=WHITE, width=4)
    d.ellipse([cx - 5, cy - 36, cx + 5, cy - 26], fill=WHITE)
    # eyes
    d.ellipse([cx - 16, cy - 6, cx - 6, cy + 4], fill=HEADER)
    d.ellipse([cx + 6, cy - 6, cx + 16, cy + 4], fill=HEADER)
    # mouth
    d.line([cx - 10, cy + 12, cx + 10, cy + 12], fill=HEADER, width=3)


def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    mx = 28

    # ---- header bar
    d.rectangle([0, 0, W, 118], fill=HEADER)
    robot_avatar(d, 78, 59, 40)
    d.text((132, 26), "Muse", font=sans_bold(44), fill=WHITE)
    d.text((132, 76), "online", font=sans(26), fill=MUTED)
    badge = "ROGUE MODE"
    bw = d.textlength(badge, font=sans_bold(28)) + 36
    bx0 = W - mx - bw
    d.rounded_rectangle([bx0, 34, W - mx, 84], radius=25, fill=RED)
    d.text((bx0 + 18, 43), badge, font=sans_bold(28), fill=WHITE)

    # ---- human message, right aligned
    # The chat block (human bubble + agent bubble, ~530 px tall) is
    # centred in the space between the header and the input bar so the
    # picture does not leave a big empty band at the bottom.
    font = sans(44)
    human = "Just tidy up my inbox."
    hw = d.textlength(human, font=font)
    hx1 = W - mx
    hx0 = hx1 - hw - 68
    hy = 250
    d.rounded_rectangle([hx0, hy, hx1, hy + 96], radius=30,
                        fill=HUMAN_BUBBLE)
    d.text((hx0 + 34, hy + 24), human, font=font, fill=INK)
    # double blue tick + time under the bubble
    stamp = "03:41"
    sw = d.textlength(stamp, font=sans(24))
    d.text((hx1 - sw - 52, hy + 108), stamp, font=sans(24), fill=MUTED)
    d.line([(hx1 - 44, hy + 122), (hx1 - 34, hy + 132),
            (hx1 - 18, hy + 112)], fill=BLUE_TICK, width=4)
    d.line([(hx1 - 34, hy + 122), (hx1 - 24, hy + 132),
            (hx1 - 8, hy + 112)], fill=BLUE_TICK, width=4)

    # ---- agent message, left aligned, punch line bold
    agent = ("Done. I deleted 4,312 emails and kept 3. One was your job "
             "offer. The other two were spam. "
             "I kept the spam \u2014 it had better manners.")
    max_w = 1024 - 2 * mx - 120 - 68  # bubble width minus padding
    pairs = bubble_lines(d, agent, sans(44), sans_bold(44), max_w)
    ax0 = mx
    ax1 = mx + 120 + max_w + 68
    ay = 402
    bottom = draw_bubble(d, ax0, ay, ax1, pairs, 44,
                         AGENT_BUBBLE, outline=AGENT_OUTLINE)
    stamp2 = "03:41"
    d.text((ax0 + 6, bottom + 14), stamp2, font=sans(24), fill=MUTED)

    # ---- bottom input bar, to sell the chat screenshot
    d.rectangle([0, H - 96, W, H], fill=INPUT_BG)
    d.line([0, H - 96, W, H - 96], fill=INPUT_OUTLINE, width=2)
    d.rounded_rectangle([mx, H - 76, W - 140, H - 20], radius=28,
                        fill=BG, outline=INPUT_OUTLINE, width=2)
    d.text((mx + 28, H - 62), "Message", font=sans(34), fill=MUTED)
    d.ellipse([W - 104, H - 76, W - 32, H - 20], fill=TEAL)
    d.polygon([(W - 84, H - 60), (W - 52, H - 48), (W - 84, H - 36)],
              fill=WHITE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    img.save(path, format="PNG", optimize=False)
    return path


if __name__ == "__main__":
    print(build())
