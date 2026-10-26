"""Genera index.html (app instalable para GitHub Pages) a partir de fuente/agenda-fisio.artifact.html.

Uso:  python3 fuente/build.py
La fuente es la misma app que corre como artifact en Claude; fuera de Claude guarda los datos en el navegador.
"""
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
src = (raiz / "fuente" / "agenda-fisio.artifact.html").read_text(encoding="utf-8")

corte = src.index("</style>") + len("</style>")
cabeza, cuerpo = src[:corte], src[corte:]
cabeza = cabeza.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")

reset = ('<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);'
         'padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font-size:14px;'
         'font-family:system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>')

head = "\n".join([
    '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
    '<link rel="manifest" href="manifest.webmanifest">',
    '<link rel="icon" type="image/png" href="icon-192.png">',
    '<link rel="apple-touch-icon" href="apple-touch-icon.png">',
    '<meta name="theme-color" content="#0d6a61">',
    '<meta name="apple-mobile-web-app-capable" content="yes">',
    '<meta name="mobile-web-app-capable" content="yes">',
    '<meta name="apple-mobile-web-app-title" content="Agenda Fisio">',
    reset,
    cabeza,
])
sw = ('<script>if("serviceWorker" in navigator && location.protocol.startsWith("http")){'
      'window.addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}));}</script>')

html = f'<!doctype html>\n<html lang="es">\n<head>\n{head}\n</head>\n<body>{cuerpo}\n{sw}\n</body>\n</html>\n'
(raiz / "index.html").write_text(html, encoding="utf-8")
print("index.html generado:", len(html), "bytes")
