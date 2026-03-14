import subprocess
r = subprocess.run(
    ['git', '-C', r'c:\Users\jinfu\WorkBuddy\Claw\fuku-psychology-website', 'add', '-A'],
    capture_output=True, text=True, encoding='utf-8', errors='replace'
)
print("add:", r.returncode, r.stderr[:100])

r = subprocess.run(
    ['git', '-C', r'c:\Users\jinfu\WorkBuddy\Claw\fuku-psychology-website', 'commit',
     '-m', 'add-ai-article-fix-header-logo-bug-mind-partnership'],
    capture_output=True, text=True, encoding='utf-8', errors='replace'
)
print("commit:", r.returncode, r.stdout[:200], r.stderr[:100])

r = subprocess.run(
    ['git', '-C', r'c:\Users\jinfu\WorkBuddy\Claw\fuku-psychology-website', 'push', 'origin', 'gh-pages'],
    capture_output=True, text=True, encoding='utf-8', errors='replace'
)
print("push:", r.returncode, r.stderr[:300])
