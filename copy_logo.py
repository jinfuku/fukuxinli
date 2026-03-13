# -*- coding: utf-8 -*-
import os
import shutil

src = r"D:\微云同步助手\2645927325\工作文档\直播伴侣\福库心理logo-微信图片_20260129153651_6071_124_看图王.png"
dst = r"c:\Users\jinfu\WorkBuddy\Claw\fuku-psychology-website\images\fuku-logo.png"

# 确保目标目录存在
os.makedirs(os.path.dirname(dst), exist_ok=True)

# 复制文件
if os.path.exists(src):
    shutil.copy2(src, dst)
    print(f"Logo copied successfully: {os.path.getsize(dst)} bytes")
else:
    print(f"Source file not found: {src}")
