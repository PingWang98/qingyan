import re
from pathlib import Path

md_path = Path(r"d:\AImovie\qingyan\幻梦_丁轻烟季寒衣_当前稿.md")
out_path = Path(r"d:\AImovie\qingyan\site\index.html")

raw = md_path.read_text(encoding="utf-8")
sections = [s.strip() for s in re.split(r"\n(?=##\s)", raw) if s.strip()]

chapters_meta = []
chapters_html = []

warm_chapters = {5, 6, 9, 10, 11}

title_override = {
    1: "一、 断俗缘",
    2: "二、 十六岁的宗师",
    3: "三、 风亦宁",
    4: "四、 执掌魔门",
    5: "五、 城余巷的晴雨",
    6: "六、 屏风后的夏夜",
    7: "七、 幻梦成殇",
    8: "八、 尘埃落定",
    9: "九、 附耳低语",
    10: "十、 镜前挽发",
    11: "尾声：幻梦的重量",
}

for idx, sec in enumerate(sections[1:], start=1):
    lines = [l.strip() for l in sec.splitlines() if l.strip()]
    if not lines:
        continue
    title_line = title_override.get(idx, lines[0].lstrip("#").strip())
    body_lines = lines[1:]

    chapters_meta.append((idx, title_line))

    paras_html = []
    for p in body_lines:
        p_formatted = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
        p_formatted = re.sub(r"\*(.+?)\*", r"<em>\1</em>", p_formatted)

        if p.startswith("**") and p.endswith("**"):
            paras_html.append(f'<p class="quote-highlight">{p_formatted}</p>')
        else:
            paras_html.append(f"<p>{p_formatted}</p>")

    tone_cls = "warm-tone" if idx in warm_chapters else "cold-tone"
    chapters_html.append(f"""
    <article class="chapter-block {tone_cls}" id="ch-{idx}">
      <span class="chapter-num">CHAPTER {idx:02d}</span>
      <h2 class="chapter-title">{title_line}</h2>
      <div class="chapter-prose">
        {"".join(paras_html)}
      </div>
    </article>
    """)

toc_html = "\n".join(
    f'<li><a class="toc-link {"active" if i==1 else ""}" href="#ch-{i}">{t}</a></li>'
    for i, t in chapters_meta
)

def grid(cols, items):
    cards = []
    for img, code, desc in items:
        cards.append(f"""
        <figure class="still-card">
          <img src="assets/story/{img}.jpg" alt="{code} {desc}" loading="lazy" />
          <figcaption class="still-caption"><strong>{code}</strong>{desc}</figcaption>
        </figure>""")
    return f'<div class="stills-grid cols-{cols}">{"".join(cards)}</div>'

story_html = f"""
<article class="chapter-block cold-tone" id="act-1">
  <span class="chapter-num">ACT 01 · CHAPTER ONE</span>
  <h2 class="chapter-title">第一章：旧家与断俗缘</h2>
  <div class="chapter-prose">
    <h3 class="story-sec-title">一、一纸之隔的皮影戏</h3>
    <p>暮色四合的大江上，楼船顶层的两间舱房只隔着一道直棂白纸隔扇。</p>
    <p>隔壁燃着暖黄的烛火，纸上映出一男一女两道剪影——摇着折扇的男人在案前谈笑，立在他身后的女人却骤然抬手，短剑寒芒在颈侧一闪。摇扇声戛然而止，折扇滑落，人影伏倒在案几之上。</p>
    {grid(2, [
        ("s01_v3_cropped", "S01", "木格糊纸隔扇占满视野，左扇女子拔簪欲刺，右扇文士摇扇对坐"),
        ("s01t_v3", "S01T", "镜头向右下平稳后拉，右扇死者伏案、左扇齐潇湘独立自语，右前景带出暗处季寒衣侧影")
    ])}
    <p class="quote-highlight"><em>“曾经的齐潇湘确实心地善良，柔韧坚强……”</em></p>
    <p>镜头缓缓拉远，这一侧未点灯的冷暗舱房里，季寒衣正背对隔扇独立窗前。她穿着葱白短衫与鹅黄罗裙，黑亮的长发披散在肩头，与那场刺杀仅隔一层薄纸，却连头也没有回一下。江风吹入窗棂，拂起她颊边的黑发，将光阴吹回了很久以前的一个清晨。</p>

    <h3 class="story-sec-title">二、藏进袖筒的桂花糕</h3>
    <p>金黄的榆钱随晨风飘过农家小院，大榆树下的方桌旁，一家四口正围坐着吃早饭。母亲温柔地侧过身，替年幼的她擦去嘴角的饭粒。</p>
    <p>桌沿底下，十二三岁的二哥悄悄探出手，塞给她一块桂花糕，又冲她挤挤眼，竖起食指抵在唇边比了个“嘘”。小姑娘欢喜地攥紧点心，小声叫了一句：</p>
    <p class="quote-highlight"><strong>“……二哥。”</strong></p>
    <p>她舍不得立刻吃，小心翼翼地把桂花糕缩进袖筒深处藏好。而那个隔着时空的声音，恰好在此刻轻轻落下后半句：<em>“很可怜，也很值得怜惜……”</em></p>
    {grid(1, [
        ("s02_v1", "S02", "二哥在桌下偷偷递来桂花糕，竖起食指抵唇比“嘘”")
    ])}
    {grid(2, [
        ("s02t_v1", "S02T", "大榆树下暖阳满院，一家四口围坐方桌的圆满瞬间"),
        ("s03_v2", "S03", "同一棵榆树、同一张方桌，暖金天光骤褪为死寂冷灰，长凳翻倒，空无一人")
    ])}

    <h3 class="story-sec-title">三、泥水里的红头绳</h3>
    <p>欢声笑语像被刀齐根斩断，院子里只剩下穿堂而过的凄冷风声。刚才藏进袖筒里的那块桂花糕掉在泥水里，已经被靴印碾碎了一半。</p>
    <p>孤零零跪在空院中央的女孩面前，停下了一双青衫布履。三十多岁的严长青居高临下地俯视着她，清癯儒雅的脸上竟带着长者般温和慈悲的笑意。他宽大的手缓缓落下，替女孩理了理散乱的额发，指尖顺势一勾，抽走了她发间系着的红头绳：</p>
    <p class="quote-highlight"><strong>“寒衣，既入我门下，便该断了俗缘。”</strong></p>
    <p>那根鲜红的头绳脱手坠落，啪嗒一声，掉进冰冷灰黑的泥水里。</p>
    {grid(2, [
        ("s04_v1", "S04", "冰冷泥水里被碾碎一半的桂花糕"),
        ("s04m_v1", "S04M", "严长青温和俯身，抬手抽走幼年季寒衣发间的红头绳")
    ])}
  </div>
</article>

<article class="chapter-block cold-tone" id="act-2">
  <span class="chapter-num">ACT 02 · CHAPTER TWO</span>
  <h2 class="chapter-title">第二章：歧路（阴影里的孤狼与阳光下的天骄）</h2>
  <div class="chapter-prose">
    <p class="quote-highlight"><em>“可惜，这世上的路，从来不是人人都能自己选的。”</em></p>
    <p>在绝圣道的幽暗石室里，年少的季寒衣猛然攥紧了骨节泛白的拳头。从这一刻起，两段截然不同的人生在两个世界里平行展开——她们同样年少成名，同样在十六七岁踏入宗师之境，却一个在冷雨黑石与血火算计里独行，一个在晴空花树与同门师长的护佑下长大。</p>

    <h3 class="story-sec-title">一、行 · 孤山冷雨 vs 晴空同门（大远景）</h3>
    <p>冷雨连绵的险峻黑石长阶直通魔门石阙，天地晦暗无声，只有一抹单薄的深衣身影孤身拾级而上；而在另一边的五圣宗山门大道上，漫天晴光倾洒，白衣执枪的风亦宁正与同门师兄妹并肩说笑疾行。</p>
    {grid(2, [
        ("s05_v2", "S05", "冷雨绝壁黑石长阶直通魔门石阙，季寒衣孤身踏阶而上"),
        ("s06_v1", "S06", "五圣宗晴空山门，风亦宁与同门并肩说笑同行")
    ])}

    <h3 class="story-sec-title">二、练 · 寒室独练 vs 暖院递帕（中景）</h3>
    <p>寒冬幽暗的石室四壁空寂，季寒衣独自疾速出掌收势，口鼻间呵出冷白的气雾，身后空无一人；而在春光融融的五圣宗庭院里，风亦宁一枪收势，身旁的同门早已含笑迎上，温言递来拭汗的巾帕。</p>
    {grid(2, [
        ("s07_v1", "S07", "绝圣道幽冷石室，季寒衣独自挥掌蓄势"),
        ("s08_v1", "S08", "五圣宗暖光庭院，风亦宁收枪，同门含笑递帕关怀")
    ])}

    <h3 class="story-sec-title">三、证 · 火壁影杀 vs 演武拱手（中近景）</h3>
    <p>绝圣道的试炼从无温情。地底粗糙的岩壁上火光剧烈摇曳，束着高马尾的少女黑影一刃刺穿同门胸膛，身后败者的剪影颓然倒落；而在云海金阳下的汉白玉演武台上，风亦宁与师兄切磋收招，两人坦荡含笑、抱拳拱手相贺。</p>
    {grid(2, [
        ("s09_v2", "S09", "地底火盆烈焰摇曳，岩壁上少女黑影一刃穿胸，败者黑影颓然倒下"),
        ("s10_v3", "S10", "云海金阳下的演武台，风亦宁与师兄切磋后坦荡抱拳行礼")
    ])}

    <h3 class="story-sec-title">四、师 · 垂眸奉茶 vs 按肩勉励（近景）</h3>
    <p>幽深压抑的大殿内，季寒衣跪坐于下位，双手高举过眉恭敬奉茶，深深垂下的眼帘掩住了眼底的寒霜与恨意；而在敞亮的廊庑之下，师长温厚的手掌轻轻按在风亦宁肩头，少女抬眼仰望，眉眼舒展如春风。</p>
    {grid(2, [
        ("s11_v1", "S11", "高位俯压近景，季寒衣垂眸双手过眉向严长青奉茶"),
        ("s12_v1", "S12", "敞亮廊下微仰近景，师长温和按肩勉励风亦宁")
    ])}

    <h3 class="story-sec-title">五、得 · 伤手独夺 vs 双掌受赠（大特写）</h3>
    <p>她这一生想要的东西，从来只能靠自己从血泥里去抢——沾着灰痕与血迹的右手探入寒玉盘，五指紧绷，狠狠抓起那团暗红流转的神兽血肉；而在另一处暖金光晕里，风亦宁干干净净地摊开双掌，长者双手托着一枚温润流光的凤凰卵，郑重地放进她掌心。</p>
    {grid(2, [
        ("s13_v1", "S13", "冷调俯拍，带着灰血伤痕的右手探入寒玉盘夺取赤黑神物"),
        ("s14_v1", "S14", "暖金俯拍，风亦宁摊开双掌，长者将温润流光的凤凰卵放入她掌心")
    ])}

    <h3 class="story-sec-title">六、影与光 · 困于檐影的凝望</h3>
    <p>殿门大开，白衣执枪的风亦宁在同门的目送下大步迈出门槛，背影一步步融进门外漫天灿烂的暖金云海。</p>
    <p>而当绝圣道沉重的石门推开时，季寒衣迎面走出两步，双脚却精准地停在了廊檐浓重的阴影界限之内。她没有再往前迈出那半步，只是在冷风中微仰起脸，隔着明暗交界线静静望着檐外灰冷的天色——那双清冷孤傲的眼睛深处，藏着连她自己都不肯承认的不甘，与对光的渴望。</p>
    <p class="quote-highlight"><strong>“风亦宁不行！风亦宁绝对不行！”</strong></p>
    {grid(2, [
        ("s15_v1", "S15", "大殿门敞开，风亦宁白衣执枪迈步走入漫天暖金晴光"),
        ("s16_v2", "S16", "绝圣道沉重石门内，季寒衣停在廊檐阴影分界线内不再踏出")
    ])}
    {grid(1, [
        ("s16t_v1", "S16T", "檐影下季寒衣幽冷孤傲的双眼大特写，直刺眼瞳完成向第三幕破庙的匹配转场")
    ])}
  </div>
</article>

<article class="chapter-block warm-tone" id="act-3">
  <span class="chapter-num">ACT 03 · CHAPTER THREE</span>
  <h2 class="chapter-title">第三章：城余巷的夏夜（她又做回了一次妹妹）</h2>
  <div class="chapter-prose">
    <p class="quote-highlight"><em>她本是为复仇而来，将一座小院变成棋盘。可在这场由她亲手编织的假戏里，她却替自己偷来了一段有哥哥、有家、有人哄着讲故事的夏天。</em></p>

    <h3 class="story-sec-title">一、破庙斜阳 · 重逢般的第一声“二哥”</h3>
    <p>绝圣道石殿檐下那双幽冷孤傲的眼眸，在斜阳刺入眼瞳的瞬间，化作了破庙里一双弯如月牙、盛满狡黠笑意的眼睛。</p>
    <p>刚从昏迷中醒来的书生丁松言迷茫地睁开眼，面前蹲着一个穿葱白短衫、鹅黄罗裙、梳着乖巧双螺髻的小姑娘。她歪着头笑吟吟地问他：“醒了？”见书生一脸怔忡，她眼里的灿烂笑意顺势敛成恰到好处的委屈与失落，伸手一把揪住他的袖口，熟稔地往门外温暖的夕阳里一拽：</p>
    <p class="quote-highlight"><strong>“……二哥，你不记得我了？”</strong></p>
    {grid(2, [
        ("s17_v4", "S17", "承接 S16T 石殿冷眼100%对齐眼位与发丝，破庙夕阳下眼尾微弯的温柔笑眼特写"),
        ("s17t_v1", "S17T", "破庙斜阳丁达尔光束下，丁轻烟蹲身揪住丁松言衣袖")
    ])}

    <h3 class="story-sec-title">二、灯下的家 · 飞蛾扇与理鬓温情</h3>
    <p>夕阳的金橙光晕化作城余巷小院初掌的灯火。小榆树下，憨厚的大哥丁大牛在院角劈柴，坐在门槛上的“爹爹”丁胜意悠闲地摇着折扇——扇面上清清楚楚绘着几只扑火的飞蛾，廊下的真飞蛾正绕着溢出的油灯暖光飞舞。</p>
    <p>顺着门槛暖光望进屋内，“娘亲”刘玉藻正站在丁轻烟身后，低头温柔地替她理了理鬓角碎发，用那道与开场楼船画外音一模一样的温和声线轻声叮嘱：<em>“小烟，别动。”</em>丁轻烟乖巧地闭着眼，神情安宁得仿佛这里真是她从小长大的家。</p>
    {grid(1, [
        ("s18_v1", "S18", "城余巷深焦小院，右侧大哥劈柴、门槛假爹摇飞蛾扇、内室母女梳头")
    ])}
    {grid(2, [
        ("s18m_v1", "S18M", "门槛上的“爹爹”丁胜意（邱辰）手持绘有飞蛾图案的折扇"),
        ("s18t_v1", "S18T", "“娘亲”刘玉藻站在身后，温柔替闭目乖巧的丁轻烟整理双螺髻鬓发")
    ])}

    <h3 class="story-sec-title">三、屏风后的《白蛇传》 · “每回都是最后一点”</h3>
    <p>夏夜微凉，西厢房里一豆油灯跳动着温暖的火苗。丁松言坐在书案前手持书卷，一扇素雅的屏风将房间隔开，屏风上静静映出少女侧卧在榻、盖着薄被的纤细剪影。</p>
    <p>听见二哥停了声音，屏风后的影子轻轻翻了个身，拉长了声音撒娇：</p>
    <p class="quote-highlight"><strong>“二哥，怎么不讲了？那……再讲最后一点？”<br/>“每回都是最后一点。”</strong></p>
    <p>书生失笑摇头，窗外夏虫低鸣，屏风后的绝圣道宗主在凡人笨拙却温和的讲书声里，安安静静地闭上了眼。</p>
    {grid(1, [
        ("s19_v2", "S19", "左前景油灯跳动，丁松言案前持卷，右侧屏风后映出少女侧卧听书的剪影")
    ])}

    <h3 class="story-sec-title">四、榆钱银钗与铜镜欢颜 · 不争不抢的礼物</h3>
    <p>雨后初霁，屋檐边悬着晶莹欲滴的水珠。丁松言略带别扭地从怀里摸出一支素银榆钱钗递到她面前：“给你的。”</p>
    <p>丁轻烟低头拨弄了一下那枚小巧的素银榆钱，故意促狭道：“留着以后给你媳妇吧。”可当二哥假意缩手说“要不我就送任伯家的黄狗阿花了”，她却眼疾手快地一把抢进掌心，护在胸口抄起扫帚笑骂着追打出去。</p>
    <p>那天夜里，温黄的铜镜前，那支并不名贵的素银榆钱钗已经插在了她的双螺髻间。她歪着头左右照了照，镜中的少女眉眼弯起，露出了毫无阴霾的欢喜笑意。</p>
    {grid(2, [
        ("s20_v1", "S20", "雨后廊下，丁松言摊开手掌递出素银榆钱钗，丁轻烟低头端详"),
        ("s21_v3", "S21", "夜里越肩铜镜，右髻已插上素银榆钱钗，镜中少女满眼真切欢喜")
    ])}
  </div>
</article>

<article class="chapter-block cold-tone" id="act-4">
  <span class="chapter-num">ACT 04 · CHAPTER FOUR</span>
  <h2 class="chapter-title">第四章：暗流与选择（真伤演假哭 · 悬停半寸的手）</h2>
  <div class="chapter-prose">
    <p class="quote-highlight"><em>“有时候，假的东西，倒比真的更容易让人相信。”</em></p>

    <h3 class="story-sec-title">一、织网 · 铁门入瓮与篦箱密信</h3>
    <p>铜镜里的笑意还未散尽，白昼森严的阴影已悄然合拢。丁松言怀抱一摞话本被引入高耸的甄府铁门，沉重的黑门在他身后缓缓关死。而在城余巷的灯下，替二哥安静誊抄话本的丁轻烟趁无人注意，指尖一滑，将一张折好的密信悄无声息地塞进了“娘亲”刘玉藻的篦箱暗格。扑火的飞蛾撞上灯罩，油灯“啪”地一声被吹熄。</p>
    {grid(2, [
        ("s22_v1", "S22", "高位大远景，怀抱话本的丁松言踏入甄府森严铁门"),
        ("s23_v2", "S23", "夜里书案近景，她一边誊抄话本，一边将密信悄然塞入篦箱暗格")
    ])}

    <h3 class="story-sec-title">二、噩梦与誓 · 真伤演假哭的“那我信你”</h3>
    <p>收网前夜，西厢房只剩清冷的蓝月透窗。屏风后传来小妹压抑脆弱的啜泣声，屏风上映出她抱膝蜷缩的剪影：</p>
    <p class="quote-highlight"><strong>“二哥……我做了个噩梦。我梦到，我们搬回了那个大院子……爹爹、娘亲、大哥，还有你，都不在了。只有我一个人。”<br/>“我还梦到……我一直等你来给我讲故事，一直等，一直等，你都没有来……房间好黑。”</strong></p>
    <p>榻边的丁松言温和而笃定地向她发誓：</p>
    <p class="quote-highlight"><strong>“我丁松言发誓，不会死，不会丢下小妹，去哪儿都会带着她。”<br/>“那我信你。”</strong></p>
    <p>就在尾音落下的瞬间，镜头越过屏风木框滑入内侧——清冷月光下，侧躺着的少女脸上干干净净没有半分泪痕。哭腔是她演出来的；可她静静睁着的那双黑亮眼睛里却没有半分算计得逞的冷笑，只有深不见底的安静与微怔——因为她拿来诱他发誓的噩梦，字字句句全是她自己真实的旧伤。</p>
    {grid(2, [
        ("s24_v1", "S24", "清冷蓝月下，屏风后映出抱膝蜷缩哭诉噩梦的少女剪影"),
        ("s25_v1", "S25", "左前景榻边丁松言温和立誓，右侧屏风后少女蜷缩聆听")
    ])}
    {grid(1, [
        ("s25t_v1", "S25T", "镜头横移越过屏风，月光下少女脸上无泪，唯余深不见底的安静与微怔")
    ])}

    <h3 class="story-sec-title">三、褪下“丁轻烟” · 地牢里的师徒倒转</h3>
    <p>破晓青灰的冷光里，她伸手扯下发绳，乖巧的双螺髻散落成如瀑黑发。她用一条素白丝帕在脑后松松束起长发，将那支榆钱银钗包入素帕收进袖中——“妹妹丁轻烟”就此退场，绝圣道宗主季寒衣正式归位。</p>
    <p>她提着鹅黄罗裙拾级而下，踏过幽暗潮湿的地牢石阶。沉重的铁门推开，昔日居高临下抽走她红头绳的师父严长青如今两鬓斑白、僵坐在椅中。季寒衣站在他面前居高临下地俯视着他，微微歪了歪头，眼底结着寒冰，唇角勾起一抹猫戏老鼠般的残忍戏谑：</p>
    <p class="quote-highlight"><strong>“师父，您怎么怕了？当初您断我俗缘的时候，可不是这个样子的。”</strong></p>
    {grid(2, [
        ("s26_v1", "S26", "破晓冷光，双螺髻已散，双手在脑后束起素白丝帕切回季寒衣本相"),
        ("s27_v2", "S27", "两侧虚焦铁栅掠过前景，鹅黄裙角踏过潮湿地牢石阶拾级而下")
    ])}
    {grid(1, [
        ("s28_v1", "S28", "180°权力倒转，左前景老严长青僵坐背影，季寒衣居高临下残忍戏谑俯视")
    ])}

    <h3 class="story-sec-title">四、雨屋抉择 · 两个人的不同选择</h3>
    <p>惨白的闪电劈亮甄府雨屋，地上散落着几册被雨水洇湿的话本——前来甄府说书的丁松言撞破了内室剧变。季寒衣带着魔门宗主惯性的玩味戏谑一步步逼近，将惊骇的书生逼得脊背抵死在冷墙上，右手缓缓抬起，伸向他的头顶。</p>
    <p>趁手臂扬起的瞬间，画面与开场楼船隔扇后的刺杀剪影形成惊心动魄的对照——隔扇之后，齐潇湘毫不犹豫地一击刺穿了假爹邱辰的咽喉，折扇脱手滑落；而齐潇湘冰冷的画外音也在此刻落下终段判词：</p>
    <p class="quote-highlight"><em>“……但在魔窟时，她就已经死了，如今活着的不过是一个……擅于利用他人怜悯的恶鬼。”</em></p>
    <p>同样是来自魔窟的人，同样面对这场城余巷的骗局，两个人却做出了截然不同的选择。季寒衣伸在丁松言头顶半寸处的纤白手掌骤然停在半空，指尖轻轻一蜷，主动垂手收回，两人第一次回到了水平对等的视线高度。为了掩饰那一瞬真切的心软，她微微前倾上身，唇角重又扬起三分俏皮戏谑、七分轻叹的笑意，极轻地唤出了最后一声：</p>
    <p class="quote-highlight"><strong>“……二哥。这几日我玩得很开心。”</strong></p>
    <p>她背起双手退至门边，一步迈入门外倾盆大雨，任由画框将两人隔成两界。</p>
    {grid(1, [
        ("s29_v2", "S29", "闪电余光下，前景散落雨水洇湿的话本与男靴，远处内室门边季寒衣现身")
    ])}
    {grid(2, [
        ("s29t_v1", "S29T", "雨屋墙边，季寒衣步步逼退丁松言，右手抬起伸向他头顶"),
        ("s01_strike", "S01M", "同构图平行对照：隔扇后齐潇湘决绝刺穿假爹咽喉——两个人做出了截然不同的选择")
    ])}
    {grid(2, [
        ("s30_v1", "S30", "楼船木地板上跌落展开的飞蛾折扇，揭晓开场死者正是假爹邱辰"),
        ("s31t_v2", "S31T", "主动撤手收回，恢复水平对等视线，轻声唤出最后一声“二哥”")
    ])}
  </div>
</article>

<article class="chapter-block warm-tone" id="act-5">
  <span class="chapter-num">ACT 05 · CHAPTER FIVE</span>
  <h2 class="chapter-title">第五章：楼船与银镜（幻梦的重量）</h2>
  <div class="chapter-prose">
    <h3 class="story-sec-title">一、推门认脸 · 齐潇湘与刘玉藻</h3>
    <p>瓢泼大雨声渐沉为江水拍舷声。楼船顶层那扇木格糊纸隔扇门吱呀推开，暖黄灯光下走出的女人赫然长着城余巷“娘亲”刘玉藻的那张温婉脸庞——她便是绝圣道下属齐潇湘，也是刚才在隔壁亲手杀死“假爹”邱辰的人。</p>
    <p>面对这面早已在魔窟里麻木的同类镜子，临窗而立的季寒衣连头都懒得回，只倦怠散漫地应了一句：“你们上船前我便在了。”齐潇湘恭敬地在书案上放下那把飞蛾折扇与《蛾神经》，退回隔壁合门吹熄了油灯。</p>
    {grid(2, [
        ("s32_v1", "S32", "隔扇推开一道暖光，右前景季寒衣暗影如山，齐潇湘（刘玉藻同脸）推门而入"),
        ("s32m_v1", "S32M", "微推近景拍清齐潇湘正脸，与城余巷“娘亲”刘玉藻容貌完全重合")
    ])}
    {grid(1, [
        ("s33_v1", "S33", "齐潇湘将飞蛾折扇与《蛾神经》放于书案复命")
    ])}

    <h3 class="story-sec-title">二、银镜挽发 · 唯一卸下防备的真笑</h3>
    <p>船舱彻底归于幽暗私密。书案一侧摆着透出琥珀微光的黑漆木匣（内藏她苦心谋划夺来的浑沌遗骸），另一侧放着那方素白丝帕。她伸手拨开素帕，拈起那支朴素的素银榆钱钗——钗头掠过江窗冷月，闪过一点干净的银亮微芒。</p>
    <p>她独自坐到冷蓝的玻璃银镜前，将披散的长发认认真真挽成发髻，把那支榆钱银钗稳稳插在发间。</p>
    <p>四下无人，她脸上人前所有的妖女戏谑、算计与冷傲彻底归零。她看着镜中发间的银钗，嘴角慢慢浮起一抹干干净净、毫无防备、明亮温暖的笑意——和城余巷铜镜前那个“妹妹”的一笑，一模一样。</p>
    <p class="quote-highlight"><strong>一个早已失去家的人，偏偏又做了一场有家的梦。<br/>梦醒之后，家还是没有了。但她带走了一根银钗。</strong></p>
    {grid(2, [
        ("s34_v1", "S34", "俯拍书案，左为透出琥珀光的浑沌遗骸木匣，右为素白丝帕上的榆钱银钗"),
        ("s35_v7", "S35", "与第三幕铜镜完全同机位，冷蓝银镜前挽发插钗，露出全片唯一卸下防备的干净真笑")
    ])}
  </div>
</article>
"""

story_toc_html = """
<li><a class="toc-link active" href="#act-1">一、 旧家与断俗缘</a></li>
<li><a class="toc-link" href="#act-2">二、 歧路 · 孤狼与天骄</a></li>
<li><a class="toc-link" href="#act-3">三、 城余巷的夏夜</a></li>
<li><a class="toc-link" href="#act-4">四、 暗流与选择</a></li>
<li><a class="toc-link" href="#act-5">五、 楼船与银镜</a></li>
"""

method_toc_html = """
<li><a class="toc-link active" href="#m-sec-1">一、 科班保底四大法则</a></li>
<li><a class="toc-link" href="#m-sec-2">二、 我们如何做无缝转场</a></li>
<li><a class="toc-link" href="#m-sec-3">三、 51% 情绪切点与全片矩阵</a></li>
<li><a class="toc-link" href="#m-sec-4">四、 2D 镜头调度与构图纵深</a></li>
<li><a class="toc-link" href="#m-sec-5">五、 全链路音频与声画蒙太奇</a></li>
<li><a class="toc-link" href="#m-sec-6">六、 视觉资产锚定与首帧工程</a></li>
<li><a class="toc-link" href="#m-sec-7">七、 3D 白模预演与双平台协同</a></li>
"""

transitions_data = [
    ("01 ➔ 02", "同向动势 + 冷暖反差", "江风吹拂季寒衣黑发向右飘动（冷蓝暮色）", "虚焦金黄榆钱随晨风向右掠过前景（暖金晨光）"),
    ("02 ➔ 03", "零帧差同机位蒸发 + 断音", "后拉定格在全家四口围坐早饭标准中全景（暖声满溢）", "同机位原位改图：四人瞬间蒸发、长凳翻倒、暖声刀切断绝"),
    ("03 ➔ 04", "景别骤缩 + 信物呼应", "空饭桌中全景静止（凄冷风声）", "贴地微距大特写：泥水里被碾碎的桂花糕 ➔ 上摇严长青"),
    ("04 ➔ 05", "下坠水花流体匹配", "鲜红头绳坠入黑灰泥水坑溅起泥水花", "冷雨砸落陡峭黑石山阶溅起雨水花，少女孤身独行"),
    ("05 ➔ 14", "五级漏斗同向同速接力", "季寒衣（冷黑）：远景跟拍 ➔ 中景右移 ➔ 中近景环绕 ➔ 近景俯压 ➔ 特写抓神肉", "风亦宁（暖金）：同速远景跟拍 ➔ 同速右移 ➔ 同速环绕 ➔ 近景微仰 ➔ 特写接凤卵"),
    ("15 ➔ 16", "反向情绪运镜 + 明暗对撞", "风亦宁背后前推走入漫天暖金阳光柔和过曝", "季寒衣停在深浓檐影界限内，正面缓慢后拉显出渺小孤寂"),
    ("16 ➔ 17", "眼瞳同坐标刺入匹配", "陡然反推刺入季寒衣孤冷双眼大特写（画框正中央）", "同画框正中央坐标丁轻烟弯弯月牙笑眼大特写 ➔ 流畅后拉露破庙"),
    ("17 ➔ 18", "逆光眩光漫溢 (Light Wipe)", "右手揪住衣袖往门外拽，金橙夕阳逆光眩光充满画框", "承接暖橙光晕化开，穿院推进门槛飞蛾折扇与正屋油灯"),
    ("18 ➔ 19", "油灯火苗前景掠镜接力", "正屋内向右环移，尾拍掠过桌角跳跃的暖黄油灯火苗前景", "承接向右横移，从书案前跳跃的暖黄油灯火苗前景旁滑出"),
    ("19 ➔ 20", "夜雨转晨檐水 (J-Cut)", "夜话尾拍安静气口，窗外提前响起淅沥夜雨声", "雨后初霁清晨，左上前景屋檐一滴晶莹水珠滴落"),
    ("20 ➔ 21", "动静反差 + 笑声余韵桥", "院门大景深追逃，少女把抢来的银钗护在胸口笑闹（动）", "越肩固定机位，银钗已稳插右髻，铜镜中化作无声甜笑（静）"),
    ("21 ➔ 22", "破粘连：极暖近景切极冷远景", "暖夜闺房越肩近景，铜镜甜笑（2700K 极暖极静）", "阴沉白天高机位俯拍大远景，甄府玄黑铁门关死（6500K 极冷）"),
    ("22 ➔ 23", "话本道具接力 + 旁白跨桥", "远景丁松言怀抱蓝皮话本走入铁门（旁白前半句）", "近景桌面摊开誊抄的蓝皮话本，手向右滑塞密信入篦箱（旁白后半句）"),
    ("23 ➔ 24", "吹灯入冷月 (Light-Out)", "飞蛾撞灯，昏黄油灯被一口吹熄骤陷幽蓝月色", "熄灯后清冷蓝白月夜西厢房，慢推屏风后蜷缩啜泣剪影"),
    ("24➔03➔25", "L-Cut 哭诉声桥 + 横移越屏", "哭诉噩梦中闪回 Shot 03 空饭桌（底层哭腔不断）", "左摇榻边立誓 ➔ 向右横移越过深色屏风木框遮挡，滑入内侧露无泪真容"),
    ("26 ➔ 27", "迈步裙角动作匹配", "收好银钗入袖，鹅黄罗裙转身向前迈出第一步", "低机位特写同一袭鹅黄裙角踏在潮湿地牢青石阶上溅起水花 ➔ 上摇跟拍"),
    ("27 ➔ 28", "180° 师徒越肩镜像倒转", "两侧虚焦黑色铁栅竖影划过前景，拾级而下", "铁门开，架在严长青左肩后低位微仰拍季寒衣残忍戏谑歪头（镜像 04）"),
    ("28 ➔ 29", "吹灯全黑 + 炸雷闪电切", "阴风吹灭地牢油灯陷入全黑 + 平地一声炸雷", "一道惨白闪电瞬间劈亮甄府雨屋门槛散落的湿话本 ➔ 贴肩逼退"),
    ("29➔01➔30➔31", "45°抬手几何匹配 + 停手反转", "侧逆光右手划出 45° 右上扬斜线 ➔ 硬切 01 隔扇同角度挥刺落扇", "微推地上飞蛾折扇（旁白落“恶鬼”）➔ 切回雨屋半空停手蜷指，无声推翻判词"),
    ("31 ➔ 32", "雨声化江涛 (L/J-Cut 双桥)", "迈入漫天大雨，暴雨声渐沉同频化作低沉江水拍舷声 + 齐潇湘先唤“宗主？”", "切入楼船暗主明仆深焦构图，推门暖光照亮刘玉藻正脸"),
    ("33 ➔ 34 ➔ 35", "吹灯私密 + 银芒引镜 + 抽声切黑", "齐潇湘退回隔壁合门吹熄暖灯 ➔ 俯拍拈起银钗掠过冷月闪过一点银芒", "顺抬手动势切入与 21 完全同机位的越肩银镜，真笑活态瞬间先抽空江水声再硬切纯黑"),
]

trans_rows = "".join(
    f'<tr><td class="method-code">{c}</td><td><strong>{n}</strong></td><td>{o}</td><td>{i}</td></tr>'
    for c, n, o, i in transitions_data
)

method_html = f"""
<article class="chapter-block cold-tone" id="m-sec-1">
  <span class="chapter-num">METHODOLOGY 01 · FUNDAMENTALS</span>
  <h2 class="chapter-title">一、 科班保底四大法则：如何消除镜头切换的“跳跃感”</h2>
  <div class="chapter-prose">
    <p>在经典影视剪辑理论（沃尔特·默奇《眨眼之间》、波德维尔《电影艺术》及《镜头语法》）中，镜头切换被划分为两个层级：第一层是<strong>“保底基本功”</strong>，解决画面如何衔接才自然流畅、不让观众跳戏；第二层是<strong>“高阶转场法”</strong>，解决如何跨越时空并传递戏剧张力。许多短片或 AI 视频之所以给人卡顿、眩晕的观感，往往是因为触犯了以下四条基础规则：</p>

    <div class="rule-card">
      <h4>1. 「隔级切景别」与「30° 法则」——防跳切与景别粘连</h4>
      <p><strong>核心原理：</strong>电影景别由远及近分为五档：远景（看环境）、全景（看全身）、中景（腰膝以上看肢体）、近景（胸部以上看神情）、特写（看局部细节与眼神）。相邻两个镜头切换时，机位角度变化应大于 30°，或景别至少跨越一级半（如全景直接切近景、中景直接切特写）。若相邻两镜同景别、同角度硬切，人眼会产生画面掉帧卡顿的错觉（即“跳切”或“景别粘连”）。</p>
      <p><strong>《幻梦》实战应用：</strong>这一规则唯一的例外，是刻意表现“时间瞬间坍塌、活人凭空消失”的超现实重击。在第一幕 <code>S02 ➔ S03</code> 中，前镜定格在一家四口围坐吃饭的中全景，后镜采用 0° 完全同机位、同景别的空饭桌——桌面与大榆树分毫不差，唯独四口人瞬间蒸发，利用视觉残留制造出“灭门”的失重感；紧接着 <code>S03 ➔ S04</code> 从全景空桌直接跨三级切入贴地泥水碎桂花糕大特写，严格遵循“隔级切景别”。</p>
    </div>

    <div class="rule-card">
      <h4>2. 「180° 轴线法则」——建立稳定的空间方向感</h4>
      <p><strong>核心原理：</strong>当画面中有两名角色对话或对峙时，两人视线连线构成一条无形的“轴线”。无论摄影机如何切换近景或越肩镜头，机位都必须保持在轴线的同一侧（180° 半圆内），确保一人始终在左朝右看、另一人始终在右朝左看。一旦越轴，观众对人物空间方位的认知就会瞬间错乱。</p>
      <p><strong>《幻梦》实战应用：</strong>无论是第一幕与第四幕严长青与季寒衣的越肩对峙（<code>S04M ↔ S28</code>），还是雨屋中季寒衣逼退丁松言再到平视唤出“二哥”（<code>S29T ➔ S31T</code>），机位始终锚定在同一轴线侧，让权位的倒转与视线的平权清晰可读。</p>
    </div>

    <div class="rule-card">
      <h4>3. 「动接动、静接静」——隐形剪辑的核心秘密</h4>
      <p><strong>核心原理：</strong>人眼天生会被运动中的物体吸引。当角色正在做动作或摄影机正在移动时，应在动作进行到一半、速度最快的那一帧切入下一镜头（动接动）；而当镜头推到位停稳后，则衔接固定静止的镜头（静接静）。只有当需要用突发声响或剧烈转折打破氛围时，才刻意使用“静切动”。</p>
      <p><strong>《幻梦》实战应用：</strong>在 <code>S26 ➔ S27</code> 中，季寒衣在西厢房收起银钗、鹅黄罗裙刚向前迈出第一步，画面便趁迈步动势切入地牢潮湿石阶上落下的同一袭裙角，观众的注意力完全跟随步伐流动，自然跨越了空间。而在 <code>S21 ➔ S22</code> 中，则刻意用暖夜闺房铜镜甜笑（极暖极静）一刀硬切白天高机位俯拍甄府玄黑铁门沉重关死（极冷极动），将观众从城余巷的温情美梦中骤然拉回冷酷棋局。</p>
    </div>

    <div class="rule-card">
      <h4>4. 「视觉焦点跟随（Eye-Trace）」——指哪切哪的视线引导</h4>
      <p><strong>核心原理：</strong>观众在观看前一镜头最后一秒时，视线停留在画框的哪个坐标，下一镜头第一秒的核心主体就应当出现在画框的同一坐标上，避免观众眼球在画面中费力搜寻焦点。</p>
      <p><strong>《幻梦》实战应用：</strong>第二幕结尾 <code>S16T ➔ S17</code>，镜头先推至季寒衣孤冷的双眼大特写并锁定在画框正中央；下一帧切入破庙斜阳时，丁轻烟弯弯带笑的眼睛同样精准落在画框正中央同一坐标。观众视线无需移动，便能直观感受到从“绝圣道宗主”到“邻家小妹”的无缝转换。</p>
    </div>
  </div>
</article>

<article class="chapter-block warm-tone" id="m-sec-2">
  <span class="chapter-num">METHODOLOGY 02 · OUR TRANSITION ENGINEERING</span>
  <h2 class="chapter-title">二、 我们在《幻梦》中如何实现无缝转场：从科班母法到 AI 工程落地</h2>
  <div class="chapter-prose">
    <p>在传统实拍电影中，跨时空转场依赖现场摄影机运动与后期剪辑台拼接；而在 AI 视频制片中，若直接把两段毫无关联的生成视频硬切拼在一起，极易出现“PPT 翻页感”或首尾帧强行叠化（Forced Dissolve）的伪影。为此，我们在《幻梦》中设计了一套<strong>“首帧像素级对齐 + 尾拍动势预埋 + 剪辑台黑帧/光晕桥接”</strong>的八大无缝转场工程方案：</p>

    <div class="rule-card">
      <h4>1. 同源原位改图硬切（Pixel-Locked In-Place Edit）——用于「活人蒸发」与「跨时空同镜」</h4>
      <p><strong>我们怎么做：</strong>在制作 <code>S02T（全家吃饭）➔ S03（灭门空桌）</code> 以及 <code>S16T（石殿冷眼）➔ S17（破庙笑眼）</code> 时，我们绝不分别随机生成两张图。而是先锁定前镜尾态原图，以该图作为底图进行局部重绘（In-Place Edit）：在 <code>S03</code> 中保持大榆树、屋檐、方桌、四只碗的像素坐标 100% 不变，仅擦除四个人物并抽冷色温、翻倒长凳；在 <code>S17</code> 中保持双瞳坐标与额前碎发丝毫不差，仅将冷暗眼神改绘为夕阳下弯起的月牙笑眼。两镜硬切时，背景或眼瞳零位移，视觉冲击力达到极致。</p>
    </div>

    <div class="rule-card">
      <h4>2. 遮挡横移 + 黑帧切开拼合兜底法（Obstacle Wipe + Black-Frame Splice）</h4>
      <p><strong>我们怎么做：</strong>在第四幕 <code>S25 ➔ S25T</code>（屏风外二哥立誓 ➔ 横移越过屏风揭示屏风内少女无泪真容）中，如果让 AI 一镜到底横移穿过屏风，人物极易发生面部畸变或穿模。我们的工程解法是将其拆分为两段独立镜头：前一段镜头向右横移，直至深色屏风木框完全占满画框（形成约 2～3 帧的纯暗部遮挡）；后一段镜头从深色木框遮挡处向右滑出，直接拍屏风内侧少女无泪的侧脸。后期在木框遮挡最暗的那一帧一刀切开拼合，肉眼完全看不出剪辑痕迹，却实现了 100% 稳定的一镜越屏效果。</p>
    </div>

    <div class="rule-card">
      <h4>3. 逆光眩光漫溢擦除（Light Flare Wipe）——用暖光融化时空边界</h4>
      <p><strong>我们怎么做：</strong>在第三幕开篇 <code>S17T（破庙揪袖）➔ S18（城余巷掌灯）</code> 中，我们在 <code>S17T</code> 的视频生成提示词尾拍明确写入“少女拉着衣袖拽向门外斜阳，金橙色逆光眩光瞬间漫溢占满整个画框”；而在 <code>S18</code> 起幅则从一团暖橙色的油灯光晕化开、缓缓推进小院。利用全屏暖金过曝帧作为过渡桥梁，让破庙的夕阳余晖自然流淌成城余巷的万家灯火。</p>
    </div>

    <div class="rule-card">
      <h4>4. 吹灯全黑与炸雷闪电硬切（Light-Out & Lightning Cut）</h4>
      <p><strong>我们怎么做：</strong>在 <code>S23 ➔ S24</code>（塞密信入夜）与 <code>S28 ➔ S29</code>（地牢转雨屋）中，我们主动利用“光源骤灭”制造天然切点。前镜尾拍让飞蛾撞灯或阴风吹熄油灯，画面在最后 0.3 秒自然陷入全黑；下一镜借平地炸雷与一道惨白闪电瞬间劈亮甄府雨屋地面上的湿话本，既省去了生硬的转场特效，又在视听上打出惊雷般的戏剧重音。</p>
    </div>

    <div class="rule-card">
      <h4>5. 几何线条与迈步动作匹配（Graphic & Action Match Cut）</h4>
      <p><strong>我们怎么做：</strong>在跨场景动作接力时，我们在首帧构图阶段就预先对齐几何角度。例如 <code>S29T ➔ S01 ➔ S30</code>：雨屋中季寒衣抬起右手伸向二哥头顶，手臂在画框中划出一条 45° 右上扬斜线；切点恰好落在手臂扬起一半时，直接硬切回开场隔扇后齐潇湘以完全一致的 45° 斜线挥剑刺落。同样，在 <code>S26 ➔ S27</code> 中，西厢房收钗迈出的鹅黄裙角与地牢石阶踏落的裙角在画框下半区严丝合缝相接。</p>
    </div>

    <div class="method-table-wrap">
      <table class="method-table">
        <thead>
          <tr>
            <th>六大跨时空转场母法</th>
            <th>镜头衔接核心机制</th>
            <th>《幻梦》片中实操落点</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. 动作匹配剪辑</strong><br/><span style="font-size:12px;color:var(--text-muted)">Action Match Cut</span></td>
            <td>前镜做前半程动作，后镜在另一时空接后半程动作。</td>
            <td>• <code>S26 ➔ S27</code>：西厢房收钗迈出第一步裙角 ➔ 地牢石阶同一袭裙角落地溅起水花。<br/>• <code>S04 ➔ S05</code>：红头绳落入泥坑溅起泥水花 ➔ 冷雨砸落黑石山阶溅起雨水花。</td>
          </tr>
          <tr>
            <td><strong>2. 图形与方向匹配</strong><br/><span style="font-size:12px;color:var(--text-muted)">Graphic / Directional Match</span></td>
            <td>靠不同时空里相同的几何线条角度或运动方向硬切。</td>
            <td>• <code>S29T ➔ S01</code>：雨屋季寒衣 45° 抬手斜线 ➔ 船舱隔扇齐潇湘 45° 挥剑刺落。<br/>• <code>S01T ➔ S02</code>：江风将黑发吹向右侧 ➔ 晨风将金黄榆钱吹向右侧。</td>
          </tr>
          <tr>
            <td><strong>3. 遮挡擦除转场</strong><br/><span style="font-size:12px;color:var(--text-muted)">Wipe / Obstacle Reveal</span></td>
            <td>让前景深色物体或强光横扫挡满画框，在遮挡瞬间偷换时空。</td>
            <td>• <code>S17T ➔ S18</code>：破庙揪袖夕阳金橙眩光漫溢满屏 ➔ 化开为城余巷夜间油灯。<br/>• <code>S25 ➔ S25T</code>：横移越过深色屏风木框黑帧拼合 ➔ 滑入内侧露无泪真容。</td>
          </tr>
          <tr>
            <td><strong>4. 视线与因果匹配</strong><br/><span style="font-size:12px;color:var(--text-muted)">Eyeline / Cause-Effect Cut</span></td>
            <td>前镜触发开关（吹灯、拈钗），后镜直接展示跨时空结果。</td>
            <td>• <code>S28 ➔ S29</code>：地牢阴风吹熄油灯全黑 + 炸雷 ➔ 惨白闪电劈亮雨屋湿话本。<br/>• <code>S34 ➔ S35</code>：拈起榆钱银钗掠过冷月闪过银芒 ➔ 顺势切入银镜插钗。</td>
          </tr>
          <tr>
            <td><strong>5. 声音桥接</strong><br/><span style="font-size:12px;color:var(--text-muted)">J-Cut & L-Cut</span></td>
            <td>声音与画面错开 1～2 秒切换（声先画后或声留画变）。</td>
            <td>• <code>S31T ➔ S32</code>：走入暴雨，雨声渐沉同频化作江水拍舷声 + 齐潇湘先唤“宗主？”。<br/>• <code>S19 ➔ S20</code>：屏风夜话尾拍窗外先响起夜雨声 ➔ 切次日清晨屋檐滴水。</td>
          </tr>
          <tr>
            <td><strong>6. 平行漏斗蒙太奇</strong><br/><span style="font-size:12px;color:var(--text-muted)">Parallel Funnel Montage</span></td>
            <td>双线交叉剪辑，景别由远及近逐级收紧，同速接力。</td>
            <td>• <code>S05–S14</code>：大远景跟拍 ➔ 中景右移 ➔ 中近景环绕 ➔ 近景俯仰 ➔ 手部大特写五级收紧，最后在 <code>S15–S16</code> 一朝前推追光、一朝后拉困暗豁然拉开。</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</article>

<article class="chapter-block cold-tone" id="m-sec-3">
  <span class="chapter-num">METHODOLOGY 03 · EMOTION & FULL MATRIX</span>
  <h2 class="chapter-title">三、 沃尔特·默奇「51% 情绪法则」与全片 35 镜转场总表</h2>
  <div class="chapter-prose">
    <p>在剪辑经典《眨眼之间》中，沃尔特·默奇提出了著名的权重法则：当所有剪辑规则发生冲突时，<strong>“情绪（Emotion）”独占 51% 的决定权</strong>，而视线跟随、三维空间轴线与二维画面构图加起来只占 49%。人在观看戏剧或交谈时，往往会在思绪与情绪发生转折的瞬间自然眨眼——而电影最精准的切点，正是替观众“眨眼”的那一瞬间。</p>
    <div class="rule-card">
      <h4>《幻梦》全片三大核心情绪切点</h4>
      <p><strong>1. 第一幕 S02T ➔ S03（极暖骤失的断崖切点）：</strong>当二哥桌下递糕、母亲温柔擦嘴的家庭暖意推至顶点，观众内心刚刚升起温情与安全感的那一秒——画面不作任何过渡，一刀硬切同机位死寂空桌，暖声瞬间断绝，让幸福感在最高点戛然归零。</p>
      <p><strong>2. 第四幕 S29T ➔ S31T（推翻“恶鬼”判词的平权切点）：</strong>当季寒衣在雨屋抬手伸向二哥头顶，楼船画外音念出<em>“如今活着的不过是一个擅于利用他人怜悯的恶鬼”</em>时，镜头切回她悬停半空微蜷的指尖，随即从错位压迫的越肩机位切换为水平对等的双人侧面平视，轻声唤出最后一声“……二哥”，用画面动作完成了对冷酷判词的无声反驳。</p>
      <p><strong>3. 第五幕 S35 终幕（余韵留白的活态切黑）：</strong>当季寒衣独自在冷蓝银镜前插上榆钱银钗，卸下所有妖女伪装露出全片唯一真笑、眼波最柔和的那一瞬间——不等笑容凝固，先一步抽空窗外江水声，紧接着一刀干脆硬切纯黑，将那抹温暖笑意永远定格在观众的视觉余韵里。</p>
    </div>

    <h3 class="story-sec-title">全片 35 镜转场咬合全景表</h3>
    <div class="method-table-wrap">
      <table class="method-table">
        <thead>
          <tr>
            <th>切点区间</th>
            <th>转场技法名称</th>
            <th>前镜尾拍（Out-Point）</th>
            <th>后镜起幅（In-Point）</th>
          </tr>
        </thead>
        <tbody>
          {trans_rows}
        </tbody>
      </table>
    </div>
  </div>
</article>

<article class="chapter-block warm-tone" id="m-sec-4">
  <span class="chapter-num">METHODOLOGY 04 · SHOT DESIGN & DEPTH</span>
  <h2 class="chapter-title">四、 2D 镜头调度与构图纵深体系（ai-cinematography-shot-design）</h2>
  <div class="chapter-prose">
    <p>为彻底摆脱 AI 视频常见的“人物贴在背景上站桩说话”的平庸写真感，我们将分镜摄影与构图规范沉淀为以下四项核心技法：</p>

    <div class="rule-card">
      <h4>1. 四大前景遮挡与三层画框纵深（Dirty Frame）</h4>
      <p><strong>• 记忆与抒情场（虚焦动态前景 + 跟焦推进）：</strong>如旧家清晨前景飘落虚焦金黄榆钱（<code>S02</code>）、雨后送钗前景悬挂屋檐晶莹水珠（<code>S20</code>），焦点从前景自然推至中景人物，赋予画面呼吸感与生活气。</p>
      <p><strong>• 压迫与囚禁场（前景铁栅竖影划过）：</strong>如季寒衣下地牢（<code>S27</code>），镜头两侧加入虚焦的黑色铁栅栏竖影一道道掠过画框，在移动中层层收紧囚笼压迫感。</p>
      <p><strong>• 权力与主仆场（暗主明仆斜向深焦同框）：</strong>如楼船齐潇湘推门复命（<code>S32</code>），右前景保留未点灯暗处季寒衣稳如泰山的披发肩颈黑影，左后方中远景暖光框出推门而入的齐潇湘，随后微推越过前景认脸，一眼定住上位者与下属的控制格局。</p>
      <p><strong>• 诀别与两界场（三层画框套画框 Frame-within-a-Frame）：</strong>如雨屋告别（<code>S31T</code> 尾拍），摄影机留在室内，近景是幽暗门框黑边，中景侧后方是怔立暗处的丁松言，远景门框外是漫天白雨与渐行渐远的鹅黄背影——一步迈出，从此两界。</p>
    </div>

    <div class="rule-card">
      <h4>2. 机位高度与 180° 越肩权力镜像</h4>
      <p><strong>• 师徒宿命 180° 倒转（S04M ↔ S28）：</strong>第一幕断俗缘时，机位贴在跪地幼女肩后微仰拍居高临下、面带慈悲笑意的严长青（不反打幼女正脸）；第四幕地牢清算时，机位严格 180° 对调，架在太师椅中两鬓斑白的严长青左肩后，微仰拍站立俯视、歪头残忍戏谑的成年季寒衣（同样不反打严长青正脸），无需多言即完成权位反转。</p>
      <p><strong>• 越肩逼退压迫 ➔ 水平侧面平权（S29T ➔ S31T）：</strong>季寒衣初现本相逼退二哥时，采用错位越肩压迫机位；当她主动停手收回、决定放过二哥时，机位第一次切换为水平高度完全对等的双人正侧面平视（Profile Two-Shot），用机位高度的平权外化她内心那一瞬的柔软。</p>
    </div>

    <div class="rule-card">
      <h4>3. 动静相生：流动推拉与全片仅留的三处“绝对静止锚点”</h4>
      <p>全片对手戏广泛采用推拉摇移与双人同框拉扯（如送钗一场戏采用“假缩手与真抢钗”同框互动接院门大景深追逃），唯独在全片最扎心的三个节点<strong>彻底锁死固定机位</strong>：① <code>S03</code> 灭门后的死寂空饭桌；② <code>S21</code> 城余巷夜里铜镜前插钗甜笑；③ <code>S35</code> 楼船冷蓝银镜前插钗真笑。周围镜头越流动，这三处绝对静止的凝视就越发触动人心。</p>
    </div>

    <div class="rule-card">
      <h4>4. 去脸谱化表演：「妖女戏谑」的四阶温度拆解直至归零</h4>
      <p>拒绝“反派奸笑 / 好人痛哭”的脸谱化指令。自第四幕季寒衣解开双螺髻、束起白丝帕切回本相起，我们将她的“妖女戏谑感”精准拆解为四层不同温度：① 对严长青是<strong>眼底结冰的残忍猫鼠戏谑</strong>；② 逼退二哥抬手时是<strong>上位者审视凡人的惯性玩味戏谑</strong>；③ 停手唤出“二哥”并背手入雨时，是<strong>拿俏皮戏谑当遮羞布、悄悄藏起心软的温柔</strong>；④ 楼船对齐潇湘是<strong>面对麻木同类的倦怠疏离戏谑</strong>；直至 ⑤ 独自面对银镜挽发插钗时，<strong>一切戏谑伪装彻底归零</strong>，露出全片唯一毫无防备的干净真笑。</p>
    </div>
  </div>
</article>

<article class="chapter-block cold-tone" id="m-sec-5">
  <span class="chapter-num">METHODOLOGY 05 · AUDIO & SOUND MONTAGE</span>
  <h2 class="chapter-title">五、 全链路音频工程与声画蒙太奇（ai-video-audio-montage）</h2>
  <div class="chapter-prose">
    <p>声音不仅是画面的伴奏，更是跨越时空与构建戏剧反差的第一驱动力。我们的音频工程包含以下核心准则：</p>

    <div class="rule-card">
      <h4>1. 音色锚定与「单角色多状态声线矩阵」</h4>
      <p><strong>• 纯净干声基准（@VOICE）：</strong>所有核心角色均前置提取 3～5 秒无混响、无配乐的 24-bit WAV 纯净干声作为参考锚点。</p>
      <p><strong>• 同一声底的阶段微调：</strong>季寒衣在第三幕伪装“小妹丁轻烟”时，声线在原声底上偏高半度，清脆明快、尾音微拖带撒娇气音；第四幕切回“宗主本相”后，声线微沉半度，语速放缓，透出漫不经心的柔媚寒意。</p>
      <p><strong>• 听觉伏笔（同声锚点）：</strong>开场楼船隔扇后的冷漠画外音（齐潇湘）与第三幕城余巷温柔替小烟理鬓的“娘亲刘玉藻”严格绑定同一成熟女声锚点，在第五幕推门认脸前便为观众埋下听觉线索。</p>
    </div>

    <div class="rule-card">
      <h4>2. 原生音画一体直出五大工程铁律</h4>
      <p><strong>① 强制锁死无背景音乐（No BGM）：</strong>每条视频生成提示词末尾均强制声明“无背景音乐，仅生成纯净环境音、动作音效与人物对白”，防止多镜头拼接时 AI 随机生成的配乐互相打架。</p>
      <p><strong>② 秒级时间戳卡点：</strong>对 6 秒以上长镜头按秒级区间精确绑定动作与台词起止点。</p>
      <p><strong>③ 闭嘴镜头显式防幻觉：</strong>凡是仅有画外音而画面内角色不说话的镜头，提示词必须写明“人物紧闭双唇不说话”，杜绝 AI 让画面人物跟着旁白乱动嘴唇。</p>
      <p><strong>④ 句尾呼吸气口预留：</strong>台词结束后强制预留 0.5～1.5 秒纯环境音（夜雨声、灯花跳动声、江水拍舷声），赋予文戏真实呼吸感。</p>
      <p><strong>⑤ 场内直出与跨切点干声分流：</strong>单镜场内对白随视频原生直出；跨越多个快切镜头的长旁白则单独生成完整连续干声通铺在剪辑音轨上，严防画面切换截断字音。</p>
    </div>

    <div class="rule-card">
      <h4>3. 判词三段拆分与声画反差双关</h4>
      <p>我们将原著中齐潇湘评价自己的那句长判词拆分为三段，分别贴在全片的三个关键节点上形成强烈的声画互文：</p>
      <p>• <strong>前段</strong>（<em>“曾经的齐潇湘确实心地善良，柔韧坚强……”</em>）贴在开场楼船刺杀后，顺向建立悬念；</p>
      <p>• <strong>中段</strong>（<em>“很可怜，也很值得怜惜……”</em>）贴在童年二哥偷偷递桂花糕的极暖画面上，冰冷判词与孩童温情形成第一次残酷双关；</p>
      <p>• <strong>末段</strong>（<em>“……但在魔窟时，她就已经死了，如今活着的不过是一个擅于利用他人怜悯的恶鬼。”</em>）精准落在第四幕雨屋季寒衣抬手欲杀二哥的瞬间；然而下一秒，画面中的季寒衣却在半空停手蜷指、轻声唤出“二哥”放他离去——<strong>前两段画面都在印证这句判词，唯独最后一段，季寒衣用自己的选择无声推翻了它。</strong></p>
    </div>
  </div>
</article>

<article class="chapter-block warm-tone" id="m-sec-6">
  <span class="chapter-num">METHODOLOGY 06 · VISUAL ASSETS & FIRST-FRAME RULES</span>
  <h2 class="chapter-title">六、 视觉资产锚定与首帧生成铁律（seedance-video-director）</h2>
  <div class="chapter-prose">
    <div class="rule-card">
      <h4>1. 母脸锁死、原位衍生与「拆单图喂入」原则</h4>
      <p>全片首先锁定唯一一张高分辨率正面/半侧母脸定妆照，随后通过原位改图（In-Place Edit）衍生出不同时期（童年、绝圣道黑衣、城余巷鹅黄双螺髻、地牢散发白丝帕）的服装与神态基准卡。在向视频模型喂入参考图时，<strong>严禁直接喂入多宫格拼图或三视图</strong>（会导致单张人脸可用像素被压缩至几十分之一而引发变脸），必须拆分为独立高清单图配合独立道具卡（<code>@PROP</code> 如素银榆钱钗、飞蛾折扇、浑沌遗骸木匣）精准注入。</p>
    </div>

    <div class="rule-card">
      <h4>2. 首帧动作「前置临界态」生图铁律</h4>
      <p>AI 视频生成最容易崩坏的环节是“手部凭空掏出细小物品”或“远距离伸手精准触碰”。因此，我们在制作全部 35 张首帧时严格执行<strong>前置临界态原则</strong>：凡涉及抽红绳（<code>S04M</code>）、桌下递糕（<code>S02</code>）、廊下递钗（<code>S20</code>）、篦箱塞信（<code>S23</code>）、探盘抓神物（<code>S13</code>），首帧静态图直接将手部绘制在<strong>“指尖已触及或刚捏住目标物边缘”的起动临界瞬间</strong>，视频模型只需驱动顺势抽走、递出或滑入的后半程动作，从根源上杜绝手部变形与道具幻觉。</p>
    </div>

    <div class="rule-card">
      <h4>3. 单首帧直出优先与「85% 相似度防叠化」铁律</h4>
      <p>90% 以上的镜头均采用<strong>单首帧 + 精准运动提示词直出</strong>，让物理光影与衣袂动态自然流淌。仅当确需锁定落幅构图时才使用首尾帧模式，且首帧与尾帧的场景透视与主体结构相似度必须高于 85%，严禁将两个机位角度差异巨大的画面强塞进同一条首尾帧生成（否则必触发模型在中间强行交叉叠化）。</p>
    </div>

    <div class="rule-card">
      <h4>4. 提示词语法：「名词给先验、动词链给结果、左右按画框写」</h4>
      <p>提示词摒弃抽象形容词堆砌，采用<strong>“物理材质名词提供视觉先验 + 连续受力动词链描述运动结果”</strong>；所有空间方位描述（左、右、前、后）一律以<strong>当前摄影机画框的屏幕左右（Screen Left / Screen Right）</strong>为准，绝不混用角色自身左右，确保运镜与走位指哪打哪。</p>
    </div>
  </div>
</article>

<article class="chapter-block cold-tone" id="m-sec-7">
  <span class="chapter-num">METHODOLOGY 07 · 3D CLAY PREVIS & HYBRID PIPELINE</span>
  <h2 class="chapter-title">七、 3D 白模空间控制与跨平台协同制片</h2>
  <div class="chapter-prose">
    <p>针对纯 2D 图生视频难以搞定的复杂空间调度与极致光学物理镜头，我们挂载了两个进阶工程模块：</p>

    <div class="rule-card">
      <h4>1. Blender 3D 白模预演控制（blender-white-model-controller）</h4>
      <p><strong>• 介入边界：</strong>日常中近景文戏与平行镜头坚持纯 2D 首帧直出以保住最鲜活的眼神灵气；仅当遇到大角度三维环绕、一镜到底多空间穿行、严苛前景遮挡或复杂多人走位时，才介入 Blender 白模控制。</p>
      <p><strong>• 防“木头人”三档精细度法则：</strong>白模绝非越精细越好（过细的僵硬骨骼动画反而会让 AI 渲染出恐怖谷木偶感）。我们按镜头需求分为三档：70% 走位运镜镜仅用<strong>极简胶囊/圆柱体</strong>交代空间位移与遮挡；20% 静态构图镜用<strong>四肢定姿白模</strong>；仅 10% 复杂交互镜使用骨骼动画并配合“去木偶化自然物理惯性”提示词。</p>
    </div>

    <div class="rule-card">
      <h4>2. 即梦 Seedance + Google Flow (Veo 3.1) 双平台协同分流（google-flow-veo-director）</h4>
      <p>充分发挥不同底座模型的长板进行混合制片：凡涉及<strong>多模态多图锁脸、原生中文对白口型同步、长镜头复杂叙事交互</strong>的镜头，交由即梦（Seedance 2.0 / 2.5）主力完成；凡涉及<strong>极致浅景深光学虚化、流体雨滴飞溅、火光烟雾物理质感及无台词纯情绪空镜/特写</strong>的镜头，分流至 Google Flow（Veo 3.1 Quality），采用“前 15 词运镜权重前置”的五段式英文提示词与外源首帧锚定法，实现人物一致性与好莱坞光学质感的双赢。</p>
    </div>
  </div>
</article>
"""

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>幻梦 · 丁轻烟 / 季寒衣</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div id="progress-bar"></div>

  <header class="top-nav">
    <div class="brand">
      <span class="brand-seal">幻梦</span>
      <span>丁轻烟 · 季寒衣</span>
    </div>
    <div class="view-tabs">
      <button class="tab-btn active" data-view-target="view-novel">二创人物志</button>
      <button class="tab-btn" data-view-target="view-story">图文剧情</button>
      <button class="tab-btn" data-view-target="view-method">方法论 · 转场</button>
    </div>
    <div class="controls">
      <button class="ctrl-btn" data-size="16px">小</button>
      <button class="ctrl-btn active" data-size="18px">标准</button>
      <button class="ctrl-btn" data-size="21px">大</button>
    </div>
  </header>

  <section class="hero">
    <div class="hero-tag">《剑烛大荒》第一卷 · 当时年少春衫薄</div>
    <h1 class="hero-title">幻 梦</h1>
    <p class="hero-subtitle">丁轻烟 · 季寒衣</p>
    <div class="hero-epigraph">
      一个早已失去家的人，偏偏又做了一场有家的梦。
    </div>
    <div class="view-tabs" style="margin-top: 36px;">
      <button class="tab-btn active" data-view-target="view-novel">阅读 · 二创人物志</button>
      <button class="tab-btn" data-view-target="view-story">赏析 · 图文分镜剧情</button>
      <button class="tab-btn" data-view-target="view-method">精研 · 影视转场方法论</button>
    </div>
  </section>

  <!-- 视图一：二创人物志（纯文字长卷） -->
  <div id="view-novel" class="view-section active">
    <main class="layout">
      <aside class="toc-sidebar">
        <div class="toc-header">人物志目录 · MONOGRAPH</div>
        <ul class="toc-list">
          {toc_html}
        </ul>
      </aside>
      <section class="manuscript">
        {"".join(chapters_html)}
      </section>
    </main>
  </div>

  <!-- 视图二：图文剧情（五幕故事 + 44张高清剧照全平铺） -->
  <div id="view-story" class="view-section">
    <main class="layout story-layout">
      <aside class="toc-sidebar">
        <div class="toc-header">五幕剧情 · STORYBOARD</div>
        <ul class="toc-list">
          {story_toc_html}
        </ul>
      </aside>
      <section class="manuscript">
        {story_html}
      </section>
    </main>
  </div>

  <!-- 视图三：方法论 · 镜头转场与剪辑语法 -->
  <div id="view-method" class="view-section">
    <main class="layout story-layout">
      <aside class="toc-sidebar">
        <div class="toc-header">转场方法论 · METHODOLOGY</div>
        <ul class="toc-list">
          {method_toc_html}
        </ul>
      </aside>
      <section class="manuscript">
        {method_html}
      </section>
    </main>
  </div>

  <footer class="site-footer">
    <p>《剑烛大荒》第一卷《当时年少春衫薄》 · 丁轻烟 / 季寒衣《幻梦》专题站</p>
  </footer>

  <script src="app.js"></script>
</body>
</html>
"""

out_path.write_text(html, encoding="utf-8")
print(f"Generated {out_path} ({len(html)} bytes).")
