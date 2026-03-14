import os
pages = [
    "spirit/index.html","mind/index.html","body/index.html",
    "partnership/index.html","ai/index.html",
    "spirit/张成谈内勒斯影响/index.html","mind/存在主义心理治疗的基本概念/index.html",
    "body/推拿疗愈身体的力量/index.html","partnership/伴侣关系中的沟通艺术/index.html",
]
base = "c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/"
ok = 0
for f in pages:
    h = open(base+f, encoding="utf-8").read()
    sticky   = "position: sticky" in h or "position:sticky" in h
    glass_hd = "blur(20px)" in h
    glass_nv = "inset 0 1px 0 rgba(255, 255, 255, 0.2)" in h
    modal    = 'id="qrModal"' in h
    small_img= "qr-img-wrap" in h
    status = "OK" if sticky and glass_hd and glass_nv and modal and not small_img else "FAIL"
    if status == "OK":
        ok += 1
    print(f"[{status}] {f}")
    if status == "FAIL":
        print(f"       sticky={sticky} glass_hd={glass_hd} glass_nv={glass_nv} modal={modal} small_img={small_img}")
print(f"\n{ok}/{len(pages)} 通过")
