"""
Genera vigil.ico — icono del tray app
"""
from PIL import Image, ImageDraw
import math

def make_vigil_icon(size):
    img  = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    s    = size
    pad  = s * 0.06

    # ── Fondo: círculo oscuro ─────────────────────────────────────────────────
    draw.ellipse([pad, pad, s - pad, s - pad], fill=(18, 18, 18, 255))

    # ── Anillo exterior verde ─────────────────────────────────────────────────
    ring = s * 0.045
    draw.ellipse([pad, pad, s - pad, s - pad],
                 outline=(0, 228, 117, 255), width=max(1, int(ring)))

    # ── Ojo (forma de almendra) ───────────────────────────────────────────────
    cx, cy = s / 2, s / 2
    ew = s * 0.52   # ancho del ojo
    eh = s * 0.28   # alto del ojo

    # Puntos de la almendra (curvas bezier aproximadas con polígono)
    steps = 60
    top_pts = []
    bot_pts = []
    for i in range(steps + 1):
        t   = i / steps
        ang = math.pi * t
        # curva superior más pronunciada
        x = cx + ew / 2 * math.cos(math.pi - ang)
        y = cy - eh / 2 * math.sin(ang) * 1.1
        top_pts.append((x, y))
        y2 = cy + eh / 2 * math.sin(ang) * 1.1
        bot_pts.append((x, y2))

    poly = top_pts + list(reversed(bot_pts))
    draw.polygon(poly, fill=(0, 228, 117, 40))   # fill translúcido
    draw.line(top_pts, fill=(0, 228, 117, 255), width=max(1, int(s * 0.045)))
    draw.line(bot_pts, fill=(0, 228, 117, 255), width=max(1, int(s * 0.045)))

    # ── Pupila ────────────────────────────────────────────────────────────────
    pr = s * 0.13
    draw.ellipse([cx - pr, cy - pr, cx + pr, cy + pr],
                 fill=(0, 228, 117, 255))

    # ── Reflejo en la pupila ──────────────────────────────────────────────────
    rr = pr * 0.38
    rx = cx - pr * 0.28
    ry = cy - pr * 0.28
    draw.ellipse([rx - rr, ry - rr, rx + rr, ry + rr],
                 fill=(255, 255, 255, 200))

    return img


if __name__ == "__main__":
    sizes  = [16, 24, 32, 48, 64, 128, 256]
    frames = [make_vigil_icon(s) for s in sizes]

    # Guardar como .ico con múltiples tamaños
    frames[0].save(
        "vigil.ico",
        format="ICO",
        sizes=[(s, s) for s in sizes],
        append_images=frames[1:],
    )
    # Preview en PNG
    frames[-1].save("vigil_preview.png")
    print("vigil.ico generado OK")
    print("vigil_preview.png — preview del icono")
