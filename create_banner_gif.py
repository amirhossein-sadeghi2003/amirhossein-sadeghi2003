from PIL import Image, ImageDraw, ImageFont
import math
from pathlib import Path

OUT_DIR = Path("assets")
OUT_DIR.mkdir(exist_ok=True)

WIDTH = 1200
HEIGHT = 320
FRAMES = 48

BG = (7, 12, 28)
GRID = (18, 28, 52)
WHITE = (235, 242, 250)
MUTED = (145, 165, 190)
CYAN = (80, 220, 255)
BLUE = (70, 120, 255)
GREEN = (90, 230, 170)
ORANGE = (255, 160, 80)
SOFT = (35, 75, 110)

try:
    title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)
    subtitle_font = ImageFont.truetype("DejaVuSans.ttf", 22)
    small_font = ImageFont.truetype("DejaVuSans.ttf", 18)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    small_font = ImageFont.load_default()


def draw_centered(draw, text, y, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((WIDTH - w) / 2, y), text, font=font, fill=fill)


def draw_satellite(draw, x, y):
    body_w, body_h = 34, 18

    draw.rounded_rectangle(
        [x - body_w / 2, y - body_h / 2, x + body_w / 2, y + body_h / 2],
        radius=4,
        fill=(190, 205, 225),
        outline=CYAN,
        width=2,
    )

    draw.rectangle(
        [x - 50, y - 7, x - 21, y + 7],
        fill=(40, 95, 175),
        outline=CYAN,
    )
    draw.rectangle(
        [x + 21, y - 7, x + 50, y + 7],
        fill=(40, 95, 175),
        outline=CYAN,
    )

    draw.line([(x, y - 9), (x + 16, y - 28)], fill=WHITE, width=2)
    draw.ellipse([x + 13, y - 31, x + 19, y - 25], fill=GREEN)


def draw_rocket(draw, x, y, flame_h):
    draw.polygon(
        [(x, y - 18), (x - 12, y + 10), (x + 12, y + 10)],
        fill=WHITE,
        outline=CYAN,
    )
    draw.rectangle([x - 8, y + 8, x + 8, y + 26], fill=(170, 185, 205), outline=CYAN)
    draw.polygon([(x - 8, y + 24), (x - 18, y + 38), (x - 2, y + 28)], fill=BLUE)
    draw.polygon([(x + 8, y + 24), (x + 18, y + 38), (x + 2, y + 28)], fill=BLUE)

    # flame pulse only
    draw.polygon(
        [(x - 6, y + 28), (x + 6, y + 28), (x, y + 28 + flame_h)],
        fill=ORANGE,
    )


def main():
    frames = []

    orbit_cx = 935
    orbit_cy = 155
    orbit_rx = 185
    orbit_ry = 72

    for i in range(FRAMES):
        t = i / FRAMES
        img = Image.new("RGB", (WIDTH, HEIGHT), BG)
        draw = ImageDraw.Draw(img)

        # background grid
        for gx in range(0, WIDTH, 60):
            draw.line([(gx, 0), (gx, HEIGHT)], fill=GRID, width=1)
        for gy in range(0, HEIGHT, 40):
            draw.line([(0, gy), (WIDTH, gy)], fill=GRID, width=1)

        # subtle stars / data points with pulse
        for k in range(26):
            px = (k * 139 + 17) % WIDTH
            py = (k * 67 + 29) % HEIGHT
            pulse = 0.5 + 0.5 * math.sin(2 * math.pi * (t + k * 0.09))
            r = 1 + int(2 * pulse)
            c = int(145 + 75 * pulse)
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(c, c + 10, c + 20))

        # rocket arc (static)
        draw.arc([70, 145, 380, 325], start=205, end=330, fill=ORANGE, width=3)

        # fixed rocket, animated flame only
        flame_h = int(10 + 7 * (0.5 + 0.5 * math.sin(2 * math.pi * t)))
        draw_rocket(draw, 185, 232, flame_h)

        # orbit line
        orbit_box = [
            orbit_cx - orbit_rx,
            orbit_cy - orbit_ry,
            orbit_cx + orbit_rx,
            orbit_cy + orbit_ry,
        ]
        draw.ellipse(orbit_box, outline=CYAN, width=2)

        # glowing sweep on orbit for more life
        sweep_center_deg = (360 * t) % 360
        for off in (-10, 0, 10):
            start = sweep_center_deg + off
            end = start + 18
            draw.arc(orbit_box, start=start, end=end, fill=WHITE, width=2)

        # smoothly moving satellite
        theta = 2 * math.pi * t
        sx = orbit_cx + orbit_rx * math.cos(theta)
        sy = orbit_cy + orbit_ry * math.sin(theta)
        draw_satellite(draw, sx, sy)

        # subtle telemetry line with pulsing nodes (no jumping dot)
        line_y = 268
        draw.line([(420, line_y), (785, line_y)], fill=SOFT, width=2)
        for n in range(4):
            nx = 470 + n * 95
            pulse = 0.5 + 0.5 * math.sin(2 * math.pi * (t + n * 0.15))
            rr = 4 + int(2 * pulse)
            color = GREEN if n % 2 == 0 else CYAN
            draw.ellipse([nx - rr, line_y - rr, nx + rr, line_y + rr], fill=color)

        # title block: no personal name here
        draw_centered(draw, "Intelligent Physical Systems", 92, title_font, WHITE)
        draw_centered(
            draw,
            "Control · Sensing · State Estimation · Embedded AI",
            145,
            subtitle_font,
            CYAN,
        )
        draw_centered(
            draw,
            "Aerospace-inspired systems, sensing, and embedded intelligence",
            185,
            small_font,
            MUTED,
        )

        frames.append(img)

    out_path = OUT_DIR / "intelligent-physical-systems-banner.gif"
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=90,
        loop=0,
        optimize=True,
    )

    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
