from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


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
PURPLE = (168, 110, 255)
SOFT = (35, 75, 110)

try:
    title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 38)
    subtitle_font = ImageFont.truetype("DejaVuSans.ttf", 20)
    small_font = ImageFont.truetype("DejaVuSans.ttf", 17)
    label_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 16)
except OSError:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    small_font = ImageFont.load_default()
    label_font = ImageFont.load_default()


def draw_centered(draw, text, y, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - text_width) / 2, y),
        text,
        font=font,
        fill=fill,
    )


def draw_sensor_node(draw, x, y, pulse):
    glow = int(25 + 35 * pulse)

    draw.rounded_rectangle(
        [x - 42, y - 32, x + 42, y + 32],
        radius=8,
        fill=(12, 28, 48),
        outline=CYAN,
        width=2,
    )

    draw.rectangle(
        [x - 22, y - 18, x + 8, y + 12],
        outline=BLUE,
        width=2,
    )

    draw.ellipse(
        [x + 13, y - 12, x + 35, y + 10],
        outline=GREEN,
        width=2,
    )

    draw.line(
        [(x - 35, y + 22), (x + 35, y + 22)],
        fill=(glow, 150, 210),
        width=2,
    )

    draw.text(
        (x - 27, y + 38),
        "DEVICES",
        font=label_font,
        fill=CYAN,
    )


def draw_mqtt_cloud(draw, x, y, pulse):
    outline = (
        int(70 + 60 * pulse),
        int(120 + 80 * pulse),
        255,
    )

    draw.ellipse(
        [x - 50, y - 12, x - 8, y + 28],
        fill=(13, 25, 52),
        outline=outline,
        width=2,
    )

    draw.ellipse(
        [x - 22, y - 28, x + 24, y + 28],
        fill=(13, 25, 52),
        outline=outline,
        width=2,
    )

    draw.ellipse(
        [x + 7, y - 10, x + 52, y + 28],
        fill=(13, 25, 52),
        outline=outline,
        width=2,
    )

    draw.rectangle(
        [x - 38, y, x + 38, y + 28],
        fill=(13, 25, 52),
    )

    draw.text(
        (x - 23, y - 1),
        "MQTT",
        font=label_font,
        fill=PURPLE,
    )

    draw.text(
        (x - 50, y + 38),
        "CONNECTIVITY",
        font=label_font,
        fill=BLUE,
    )


def draw_database(draw, x, y, pulse):
    glow = int(120 + 80 * pulse)

    draw.ellipse(
        [x - 40, y - 28, x + 40, y - 5],
        outline=GREEN,
        width=3,
    )

    draw.rectangle(
        [x - 40, y - 17, x + 40, y + 28],
        outline=(40, glow, 150),
        width=3,
    )

    draw.arc(
        [x - 40, y + 5, x + 40, y + 29],
        start=0,
        end=180,
        fill=GREEN,
        width=3,
    )

    draw.arc(
        [x - 40, y - 6, x + 40, y + 18],
        start=0,
        end=180,
        fill=GREEN,
        width=2,
    )

    draw.text(
        (x - 52, y + 38),
        "REAL-TIME DATA",
        font=label_font,
        fill=GREEN,
    )


def draw_monitor(draw, x, y, phase):
    draw.rounded_rectangle(
        [x - 58, y - 35, x + 58, y + 32],
        radius=6,
        fill=(10, 24, 43),
        outline=ORANGE,
        width=2,
    )

    draw.line(
        [
            (x - 40, y + 12),
            (x - 15, y - 3),
            (x + 5, y + 5),
            (x + 33, y - 18),
        ],
        fill=CYAN,
        width=3,
    )

    marker_x = x - 40 + int((73 * phase) % 73)
    marker_y = y + 12 - int(
        22 * (0.5 + 0.5 * math.sin(2 * math.pi * phase))
    )

    draw.ellipse(
        [
            marker_x - 4,
            marker_y - 4,
            marker_x + 4,
            marker_y + 4,
        ],
        fill=ORANGE,
    )

    draw.line(
        [(x - 20, y + 39), (x + 20, y + 39)],
        fill=ORANGE,
        width=3,
    )

    draw.text(
        (x - 43, y + 49),
        "MONITORING",
        font=label_font,
        fill=ORANGE,
    )


def draw_ai_node(draw, x, y, pulse):
    radius = 29 + int(3 * pulse)

    draw.ellipse(
        [
            x - radius,
            y - radius,
            x + radius,
            y + radius,
        ],
        fill=(24, 18, 50),
        outline=PURPLE,
        width=3,
    )

    draw.text(
        (x - 11, y - 12),
        "AI",
        font=label_font,
        fill=WHITE,
    )

    for angle in range(0, 360, 60):
        theta = math.radians(angle)

        x1 = x + radius * math.cos(theta)
        y1 = y + radius * math.sin(theta)

        x2 = x + (radius + 16) * math.cos(theta)
        y2 = y + (radius + 16) * math.sin(theta)

        draw.line(
            [(x1, y1), (x2, y2)],
            fill=PURPLE,
            width=2,
        )

        draw.ellipse(
            [x2 - 3, y2 - 3, x2 + 3, y2 + 3],
            fill=CYAN,
        )

    draw.text(
        (x - 38, y + 48),
        "APPLIED AI",
        font=label_font,
        fill=PURPLE,
    )


def draw_packet(draw, x, y, color, radius=5):
    draw.ellipse(
        [
            x - radius,
            y - radius,
            x + radius,
            y + radius,
        ],
        fill=color,
    )


def main():
    frames = []

    nodes = [130, 350, 585, 820, 1060]
    flow_y = 222

    for frame_index in range(FRAMES):
        t = frame_index / FRAMES

        image = Image.new(
            "RGB",
            (WIDTH, HEIGHT),
            BG,
        )

        draw = ImageDraw.Draw(image)

        # Background grid
        for grid_x in range(0, WIDTH, 60):
            draw.line(
                [(grid_x, 0), (grid_x, HEIGHT)],
                fill=GRID,
                width=1,
            )

        for grid_y in range(0, HEIGHT, 40):
            draw.line(
                [(0, grid_y), (WIDTH, grid_y)],
                fill=GRID,
                width=1,
            )

        # Pulsing background points
        for point_index in range(24):
            point_x = (point_index * 149 + 29) % WIDTH
            point_y = (point_index * 71 + 17) % HEIGHT

            pulse = 0.5 + 0.5 * math.sin(
                2 * math.pi * (t + point_index * 0.08)
            )

            radius = 1 + int(pulse)
            brightness = int(120 + 90 * pulse)

            draw.ellipse(
                [
                    point_x - radius,
                    point_y - radius,
                    point_x + radius,
                    point_y + radius,
                ],
                fill=(
                    brightness,
                    brightness + 10,
                    min(255, brightness + 30),
                ),
            )

        # Banner text
        draw_centered(
            draw,
            "Networked Embedded & IoT Systems",
            58,
            title_font,
            WHITE,
        )

        draw_centered(
            draw,
            "Devices · Connectivity · Real-Time Data · Monitoring · Applied AI",
            108,
            subtitle_font,
            CYAN,
        )

        draw_centered(
            draw,
            "From sensor data to reliable, observable systems",
            143,
            small_font,
            MUTED,
        )

        # Main data-flow line
        draw.line(
            [(nodes[0], flow_y), (nodes[-1], flow_y)],
            fill=SOFT,
            width=3,
        )

        # Moving telemetry packets
        packet_colors = [CYAN, BLUE, GREEN, ORANGE]

        for packet_index, packet_color in enumerate(packet_colors):
            packet_t = (t + packet_index * 0.19) % 1.0

            packet_x = (
                nodes[0]
                + (nodes[-1] - nodes[0]) * packet_t
            )

            draw_packet(
                draw,
                packet_x,
                flow_y,
                packet_color,
                radius=4 + packet_index % 2,
            )

        pulses = [
            0.5 + 0.5 * math.sin(
                2 * math.pi * (t + offset)
            )
            for offset in (
                0.00,
                0.12,
                0.24,
                0.36,
                0.48,
            )
        ]

        draw_sensor_node(
            draw,
            nodes[0],
            flow_y,
            pulses[0],
        )

        draw_mqtt_cloud(
            draw,
            nodes[1],
            flow_y,
            pulses[1],
        )

        draw_database(
            draw,
            nodes[2],
            flow_y,
            pulses[2],
        )

        draw_monitor(
            draw,
            nodes[3],
            flow_y,
            t,
        )

        draw_ai_node(
            draw,
            nodes[4],
            flow_y,
            pulses[4],
        )

        frames.append(image)

    output_path = (
        OUT_DIR
        / "networked-embedded-iot-banner.gif"
    )

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=90,
        loop=0,
        optimize=True,
    )

    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
