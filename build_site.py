# -*- coding: utf-8 -*-
import os
import re
import html

md_path = r'd:\AImovie\qingyan\幻梦_季寒衣全景特辑.md'
out_path = r'd:\AImovie\qingyan\site\index.html'

with open(md_path, 'r', encoding='utf-8') as f:
    raw_md = f.read()

# Split into sections by '---'
blocks = [b.strip() for b in raw_md.split('---') if b.strip()]

# Block 0 is title + epigraph, Block 1 is prologue, Blocks 2..13 are Chapters 1..12
prologue_md = blocks[1]
chapter_mds = blocks[2:]

# Define rich visual mapping for Prologue + 12 Chapters
chapter_visuals = [
    {
        "id": "ch-prologue",
        "num": "引子",
        "subtitle": "血泊中央的旧梦",
        "tag": "PROLOGUE · 尘封前尘",
        "quote": "在那漫长冰冷的岁月之前，她应当度过一段这样的日子。否则，许多年以后，当她精通算计、视人心如草芥时，为什么偏偏会在屏风后，做起那样撕心裂肺的梦？",
        "images": [
            {"src": "assets/s01_silhouette.jpg", "cap": "S01 · 寒山逆光剪影：未入魔门前，谁不是寻常人家的女儿", "span": "wide"},
            {"src": "assets/s02_siblings.jpg", "cap": "S02 · 旧院递糕：记忆深处温暖的兄妹旧影", "span": "half"},
            {"src": "assets/s03_courtyard_rain.jpg", "cap": "S03 · 满庭冷雨：一夜覆灭的旧时庭院", "span": "half"}
        ]
    },
    {
        "id": "ch-01",
        "num": "壹",
        "subtitle": "杀尽亲眷，灭其门庭，使人天地无依",
        "tag": "CHAPTER 01 · 绝圣道与《天心智慧经》",
        "quote": "她掌握了让所有人无条件相信她的秘法，却再也找不回重新相信任何一个人的能力。",
        "images": [
            {"src": "assets/s09_fire_wall.jpg", "cap": "S09 · 魔窟火壁独立：在豺狼环伺的深渊里咽下所有血泪", "span": "wide"}
        ]
    },
    {
        "id": "ch-02",
        "num": "贰",
        "subtitle": "十六岁，法境宗师",
        "tag": "CHAPTER 02 · 神兽血肉与同门白骨",
        "quote": "在腥风血雨中跋涉过来的她太清楚了：力量从来不会施舍安宁。只要停下一步，只要稍露疲态，这得来不易的一切便会轰然坍塌。",
        "images": [
            {"src": "assets/s05_cold_mountain.jpg", "cap": "S05 · 孤行冷雨山阶：踩过同门枯骨，执剑独行于绝圣道", "span": "half"},
            {"src": "assets/s11_tea_master.jpg", "cap": "S11 · 幽殿垂眸奉茶：师徒之间尽是机锋，恨入骨髓亦笑唤师父", "span": "half"}
        ]
    },
    {
        "id": "ch-03",
        "num": "叁",
        "subtitle": "义枪与信拳：光与暗的残忍对照",
        "tag": "CHAPTER 03 · 五圣宗的凤凰明月",
        "quote": "一个“义”字，一个“信”字。这两个字，恰恰是季寒衣从童年起就被彻底剥夺、再也不敢去触碰的禁区。",
        "images": [
            {"src": "assets/s06_sunny_sect.jpg", "cap": "S06 · 五圣宗晴空山门：沐浴在浩荡正气与万千宠爱中的风亦宁", "span": "half"},
            {"src": "assets/s08_feng_spear.jpg", "cap": "S08 · 凤凰义枪破空：堂皇正道击碎《天心智慧经》的道心裂痕", "span": "half"},
            {"src": "assets/s15_sun_gate.jpg", "cap": "S15 · 山门问道：十九岁单枪匹马叩响五圣宗山门", "span": "wide"}
        ]
    },
    {
        "id": "ch-04",
        "num": "肆",
        "subtitle": "九恶妖女与市井小妹的化身",
        "tag": "CHAPTER 04 · 宗主王座与定江潜龙",
        "quote": "她施展神功，将全身骨骼肌肉逆向收缩，褪去了一身倾城绝艳的风华，化身为一个只有十四五岁、眉眼干净纯澈的市井小姑娘。她给自己取了个名字：丁轻烟。",
        "images": [
            {"src": "assets/s16_dark_hall.jpg", "cap": "S16 · 绝圣道幽暗大殿：俯瞰众生的执棋者", "span": "half"},
            {"src": "assets/s17_eyes_awakening.jpg", "cap": "S17 · 破庙初遇：异世游魂借尸还魂，一场脱轨的楚门世界", "span": "half"}
        ]
    },
    {
        "id": "ch-05",
        "num": "伍",
        "subtitle": "老榆钱树下的虚假一家人",
        "tag": "CHAPTER 05 · 城余巷一霸与两钱素银钗",
        "quote": "那个男人对丁轻烟所有的好，纯粹得近乎笨拙，只因为一个全天下最理所应当、却被季寒衣遗失了太久的理由——她是他的妹妹。",
        "images": [
            {"src": "assets/s18_ding_courtyard.jpg", "cap": "S18 · 城余巷丁家小院：老榆树下劈柴、梳头与摇扇的市井烟火", "span": "wide"},
            {"src": "assets/s20_gift_hairpin.jpg", "cap": "S20 · 二钱银子的素银钗：不经算计、不曾索要的无条件温存", "span": "half"},
            {"src": "assets/s21_mirror_young.jpg", "cap": "S21 · 铜镜初试银钗：十四岁双螺髻少女藏不住的欢喜", "span": "half"}
        ]
    },
    {
        "id": "ch-06",
        "num": "陆",
        "subtitle": "青城山下白素贞，一屏之隔的呼吸",
        "tag": "CHAPTER 06 · 麻布屏风与如豆油灯",
        "quote": "如果这扇屏风永远不要撤去，如果这场雨永远不要停，似乎……也挺好的。",
        "images": [
            {"src": "assets/s19_screen_story.jpg", "cap": "S19 · 屏风夜话：一盏油灯将兄妹二人的剪影交叠在粗麻布上", "span": "wide"}
        ]
    },
    {
        "id": "ch-07",
        "num": "柒",
        "subtitle": "雷雨夜的三重噩梦与“那我信你”",
        "tag": "CHAPTER 07 · 毁灭前夜的孤注一掷",
        "quote": "堂堂绝圣道宗主，一生被背叛、被杀戮淬炼成铁石心肠的妖女，竟然在一切即将毁灭的前夜，像一个凡俗孩童一般，把自己的余生押在了一个凡人随口许下的诺言上。",
        "images": [
            {"src": "assets/s24_screen_nightmare.jpg", "cap": "S24 · 屏风两侧的噩梦坦白：“二哥绝不会死，绝不会丢下小妹”", "span": "wide"}
        ]
    },
    {
        "id": "ch-08",
        "num": "捌",
        "subtitle": "玄铁门开，骨骼舒展的绝世魔主",
        "tag": "CHAPTER 08 · 甄府死牢与严永之死",
        "quote": "“可惜，不是我亲手杀了你。”——一个为了在夹缝中求存的凡人哥哥，阴差阳错，替她亲手画上了复仇的句点。",
        "images": [
            {"src": "assets/s28_dungeon.jpg", "cap": "S28 · 死牢现真身：双螺髻少女蜕变为青丝如瀑的绝圣道宗主", "span": "wide"}
        ]
    },
    {
        "id": "ch-09",
        "num": "玖",
        "subtitle": "戏台坍塌后，最后一声“二哥”",
        "tag": "CHAPTER 09 · 半空收回的素手",
        "quote": "她终究舍不得，让这世上唯一一个全心全意对过丁轻烟的哥哥，死在自己的剑下。",
        "images": [
            {"src": "assets/s31_rain_height.jpg", "cap": "S31 · 高檐俯瞰定江夜雨：素手微抬又骤然收回，化作惊鸿没入大雨", "span": "wide"}
        ]
    },
    {
        "id": "ch-10",
        "num": "拾",
        "subtitle": "短剑与银钗：两座假家庭的残酷镜像",
        "tag": "CHAPTER 10 · 恶鬼沉沦与人心余温",
        "quote": "齐潇湘拿起了短剑。季寒衣，拿起了那一根两钱银子的素银钗。",
        "images": [
            {"src": "assets/s33_aunt_fan.jpg", "cap": "S33 · 楼船残局：齐潇湘掐灭温情拔剑相向，映照出季寒衣截然不同的选择", "span": "wide"}
        ]
    },
    {
        "id": "ch-11",
        "num": "拾壹",
        "subtitle": "丁轻烟留在这个世间，最后的笑靥",
        "tag": "CHAPTER 11 · 西洋银镜与帝江遗骸",
        "quote": "那一笑，宛若穿透了漫天阴霾的初阳，融化了冰封千里的寒江。没有杀机，没有机锋，没有宗主的孤绝与霸道。",
        "images": [
            {"src": "assets/s34_box_hairpin.jpg", "cap": "S34 · 掌心素银钗：坐拥无尽宝库的魔门宗主视若稀世孤品的俗物", "span": "half"},
            {"src": "assets/s35_mirror_final.jpg", "cap": "S35 · 楼船镜前挽发：丁轻烟最后的嫣然一笑与季寒衣吞噬深渊的决绝", "span": "half"}
        ]
    },
    {
        "id": "ch-12",
        "num": "拾贰",
        "subtitle": "戴银钗，吞神物——当时年少春衫薄",
        "tag": "CHAPTER 12 · 大荒风起，江天辽阔",
        "quote": "幻梦终究会醒，戏台终究会塌。可只要那根素银钗还在发间，这场有家的梦，便不算全是一场空。",
        "images": [
            {"src": "assets/face_c_truesmile.jpg", "cap": "终幕 · 她头戴一束市井的温柔，孤身没入了无尽的风雨深处", "span": "wide"}
        ]
    }
]

def md_to_html_paragraphs(md_text):
    lines = md_text.strip().split('\n')
    title = "引子 · 血泊中央的旧梦"
    body_lines = []
    for line in lines:
        if line.startswith('## '):
            title = line[3:].strip()
        else:
            body_lines.append(line)
    body_text = '\n'.join(body_lines).strip()
    paras = [p.strip() for p in re.split(r'\n\s*\n', body_text) if p.strip()]
    html_paras = []
    for idx, p in enumerate(paras):
        # Convert bold and italic
        p_html = html.escape(p)
        p_html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p_html)
        p_html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', p_html)
        p_html = p_html.replace('\n', '<br>')
        cls = ' class="drop-cap"' if idx == 0 else ''
        html_paras.append(f'<p{cls}>{p_html}</p>')
    return title, '\n'.join(html_paras)

all_sections_md = [prologue_md] + chapter_mds
chapters_html_list = []
toc_items_html = []

for i, sec_md in enumerate(all_sections_md):
    meta = chapter_visuals[i]
    title, paras_html = md_to_html_paragraphs(sec_md)
    toc_items_html.append(f'''
        <a href="#{meta['id']}" class="toc-link" data-target="{meta['id']}">
            <span class="toc-num">{meta['num']}</span>
            <span class="toc-title">{title}</span>
        </a>
    ''')
    
    imgs_html = []
    for img in meta['images']:
        span_cls = 'fig-wide' if img['span'] == 'wide' else 'fig-half'
        imgs_html.append(f'''
            <figure class="chapter-fig {span_cls}" onclick="openLightbox('{img['src']}', '{html.escape(img['cap'])}')">
                <div class="fig-img-wrap">
                    <img src="{img['src']}" alt="{html.escape(img['cap'])}" loading="lazy">
                    <div class="fig-zoom-hint">点击展开画卷</div>
                </div>
                <figcaption>{img['cap']}</figcaption>
            </figure>
        ''')
    imgs_grid = f'<div class="chapter-gallery">{"".join(imgs_html)}</div>'
    
    chapters_html_list.append(f'''
        <article id="{meta['id']}" class="monograph-chapter reveal-on-scroll">
            <header class="chapter-header">
                <div class="chapter-meta-bar">
                    <span class="chapter-badge">{meta['num']}</span>
                    <span class="chapter-tag">{meta['tag']}</span>
                </div>
                <h3 class="chapter-title">{title}</h3>
                <p class="chapter-subtitle">{meta['subtitle']}</p>
                <blockquote class="chapter-pullquote">
                    <span class="quote-mark">“</span>{meta['quote']}<span class="quote-mark">”</span>
                </blockquote>
            </header>
            {imgs_grid}
            <div class="chapter-prose">
                {paras_html}
            </div>
        </article>
    ''')

print(f"Processed {len(chapters_html_list)} chapters successfully.")
