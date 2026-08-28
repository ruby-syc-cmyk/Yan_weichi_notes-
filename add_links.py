import os
os.chdir('穿越札记/正文')
files = [f for f in os.listdir('.') if f.startswith('chapter_') and f.endswith('.md')]
files.sort()
for i, filename in enumerate(files):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if '上一章' in content and '下一章' in content:
        continue
    links = []
    if i > 0:
        prev_title = files[i-1].replace('.md','').split('_',2)[-1]
        links.append(f'[← 上一章：{prev_title}]({files[i-1]})')
    if i < len(files) - 1:
        next_title = files[i+1].replace('.md','').split('_',2)[-1]
        links.append(f'[下一章：{next_title} →]({files[i+1]})')
    with open(filename, 'a', encoding='utf-8') as f:
        f.write('\n\n---\n\n' + ' | '.join(links) + '\n')
print('章节导航更新完成！')
