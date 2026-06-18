#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从导出的英文静态 HTML 中提取干净文案，输出为 Markdown，方便录入 WordPress。"""
import os, re
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "英文文案")

# 要提取的核心页面：(源文件, 栏目, 友好名)
PAGES = [
    ("index.html",                 "01-主要页面", "首页 Home"),
    ("products.html",              "01-主要页面", "产品总览 Products"),
    ("design.html",                "01-主要页面", "设计方案 Design Solutions"),
    ("news.html",                  "01-主要页面", "新闻 News"),
    ("servicesupport.html",        "01-主要页面", "服务支持 Support"),
    ("about-gemmanew.html",        "01-主要页面", "关于 About"),

    ("about-gemmanew/about.html",   "02-关于", "公司介绍 About"),
    ("about-gemmanew/career.html",  "02-关于", "招贤纳士 Career"),
    ("about-gemmanew/contact.html", "02-关于", "联系我们 Contact"),

    ("design/hospital.html",  "03-设计方案", "医疗 Healthcare"),
    ("design/business.html",  "03-设计方案", "工业/商业 Industrial-Business"),
    ("design/hotel.html",     "03-设计方案", "酒店办公 Hospitality & Office"),
    ("design/education.html", "03-设计方案", "教育运动 Education & Sports"),
    ("design/transport.html", "03-设计方案", "交通 Transportation"),
    ("design/cleaness.html",  "03-设计方案", "洁净/住宅商业 Residential & Commercial"),

    ("products/pvchomogeneousflooring-elektra.html",      "04-产品大类", "PVC 同质透心 Elektra"),
    ("products/pvchomogeneouscoiledflooring-centra.html", "04-产品大类", "PVC 同质卷材 Centra"),
    ("products/pvcmultilayercompositeflooring-health.html","04-产品大类", "PVC 多层复合 Health"),
    ("products/pvcmultilayercompositeflooring-wego.html", "04-产品大类", "PVC 多层复合 Wego"),
    ("products/pvcresistantquartzsandflooring-onestep.html","04-产品大类","PVC 石英砂耐磨 Onestep"),
    ("products/quartzflooring-yinger.html",               "04-产品大类", "石英地板 Yinger"),
    ("products/rubberflooring-elephant.html",             "04-产品大类", "橡胶地板 Elephant"),
    ("products/scaldresistantwaterproofflooring-pinger.html","04-产品大类","防烫防水 Pinger"),
    ("products/spcflooring-senger.html",                  "04-产品大类", "SPC 石塑 Senger"),
    ("products/lvtstoneplasticflooring-linger.html",      "04-产品大类", "LVT 石塑 Linger"),
    ("products/wall.html",                                "04-产品大类", "墙面材料 Wall Materials"),
    ("products/securitydoors.html",                       "04-产品大类", "金属门 Metal Doors"),

    ("news/gemmanewhosipitalnews.html",          "05-新闻", "医院新闻 Hospital"),
    ("news/gemmanewoestepnews.html",             "05-新闻", "Onestep 新闻"),
    ("news/gemmanewpvcelectrcityconductor.html", "05-新闻", "导电地板 Conductive"),
    ("news/gemmanewpvcproductdisplay.html",      "05-新闻", "产品展示 Display"),
    ("news/gemmanewspcnews.html",                "05-新闻", "SPC 新闻"),
    ("news/newproduct-yinger.html",              "05-新闻", "新品 Yinger"),

    ("servicesupport/faq.html",          "06-服务支持", "常见问题 FAQ"),
    ("servicesupport/filedownload.html", "06-服务支持", "资料下载 Downloads"),
]

# 这些是导航/页脚/按钮里反复出现的词，正文里如果整段就是它们则跳过
NAV_NOISE = {
    "home","products","design solutions","support","news","about gemmanew",
    "ch/en","downloads","faq","menu","search","close","skip to content",
    "view more","view details","view detail","view","read more","learn more",
    "more","details","detail","+","→","all colours","all colors",
}
# 已被这些块级文字标签捕获时，其中的链接不再单独抓（避免重复）
TEXT_ANCESTORS = {"p","h1","h2","h3","h4","li","td","th","blockquote","figcaption"}

def clean(text):
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract(path):
    html = open(path, encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    title = clean(soup.title.get_text()) if soup.title else os.path.basename(path)

    # 优先正文区域
    node = soup.select_one(".entry-content") or soup.select_one("main#main") \
           or soup.select_one("article") or soup.body
    if node is None:
        return title, []

    # 去掉脚本/样式/导航/页脚
    for bad in node.select("script,style,noscript,nav,header,footer,form"):
        bad.decompose()

    lines, seen = [], set()
    for el in node.find_all(["h1","h2","h3","h4","p","li","blockquote","figcaption","td","th","a"]):
        # 链接：只抓"独立卡片"型链接（祖先不是段落/标题/列表项），否则会和正文重复
        if el.name == "a":
            if any(a.name in TEXT_ANCESTORS for a in el.parents):
                continue
        txt = clean(el.get_text(" "))
        if not txt or len(txt) < 2:
            continue
        if txt.lower() in NAV_NOISE:
            continue
        key = txt.lower()
        if key in seen:        # 去重复（菜单常重复）
            continue
        seen.add(key)
        tag = el.name
        if tag == "h1":   lines.append(("# ", txt))
        elif tag == "h2": lines.append(("## ", txt))
        elif tag in ("h3","h4"): lines.append(("### ", txt))
        elif tag in ("li","a"):  lines.append(("- ", txt))
        else:                    lines.append(("", txt))
    return title, lines

def main():
    os.makedirs(OUT, exist_ok=True)
    index_lines = ["# 英文文案汇总（待录入 WordPress）\n",
                   "> 每个页面一个文件，按栏目分文件夹。复制对应内容，粘到 WordPress 里复制出来的中文页副本中即可。\n"]
    count = 0
    for src, section, name in PAGES:
        p = os.path.join(ROOT, src)
        if not os.path.exists(p):
            print("跳过(找不到):", src); continue
        title, lines = extract(p)
        sec_dir = os.path.join(OUT, section)
        os.makedirs(sec_dir, exist_ok=True)
        safe = name.replace("/", "-")
        md_path = os.path.join(sec_dir, safe + ".md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"<!-- 源文件: {src} -->\n")
            f.write(f"<!-- 网页 <title>: {title} -->\n\n")
            for prefix, txt in lines:
                f.write(f"{prefix}{txt}\n\n")
        index_lines.append(f"- [{section}] {name}  →  `英文文案/{section}/{safe}.md`")
        count += 1
        print(f"OK  {src}  ({len(lines)} 段)")
    with open(os.path.join(OUT, "00-目录索引.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines) + "\n")
    print(f"\n完成：共 {count} 个页面，输出在 英文文案/")

if __name__ == "__main__":
    main()
