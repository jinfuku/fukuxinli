import shutil, os
p = os.path.join(r'c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/mind', '\u6df1\u5ea6\u5fc3\u7406\u6cbb\u7597\u6848\u4f8b\u5206\u4eab')
if os.path.isdir(p):
    shutil.rmtree(p)
    print('deleted')
else:
    print('not found:', p)
