import os
pages = ["mind/index.html","partnership/index.html","body/index.html","ai/index.html","spirit/index.html","about/index.html"]
base = "c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/"
for f in pages:
    h = open(base+f, encoding="utf-8").read()
    has_brand_css = ".header-brand" in h
    has_logo_css  = ".header-logo" in h
    has_h1_css    = "header h1" in h
    print(f"{f}: brand_css={has_brand_css}  logo_css={has_logo_css}  h1_css={has_h1_css}")
