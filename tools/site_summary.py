import json
from datetime import datetime

# 站点摘要资料
SITE_DATA = {
    "name": "华体会",
    "url": "https://appweb-hth.com.cn",
    "keywords": ["华体会", "体育竞技", "赛事体验"],
    "tags": ["娱乐", "体育", "互动"],
    "description": "华体会是专注于体育竞技与赛事体验的在线平台，为用户提供丰富的体育资讯和互动服务。",
    "last_updated": "2025-04-01"
}

def format_tag_line(tags):
    """将标签列表格式化为带井号的字符串"""
    return " ".join(f"#{tag}" for tag in tags)

def generate_summary(data):
    """根据资料字典生成结构化摘要"""
    lines = []
    lines.append(f"站点名称：{data['name']}")
    lines.append(f"官方网址：{data['url']}")
    lines.append(f"核心关键词：{'、'.join(data['keywords'])}")
    lines.append(f"内容标签：{format_tag_line(data['tags'])}")
    lines.append(f"简要说明：{data['description']}")
    lines.append(f"资料更新：{data['last_updated']}")
    return "\n".join(lines)

def build_structured_record(data):
    """构建结构化的记录字典"""
    record = {
        "site_name": data["name"],
        "site_url": data["url"],
        "keywords_list": data["keywords"],
        "tags_list": data["tags"],
        "short_description": data["description"],
        "update_date": data["last_updated"],
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return record

def print_json_record(data):
    """以JSON格式打印记录"""
    record = build_structured_record(data)
    print(json.dumps(record, ensure_ascii=False, indent=2))

def main():
    print("=" * 50)
    print("工具：站点资料摘要生成器")
    print("=" * 50)
    print()

    # 输出文本摘要
    summary_text = generate_summary(SITE_DATA)
    print("【文本摘要】")
    print(summary_text)
    print()

    # 输出结构化JSON
    print("【结构化记录】")
    print_json_record(SITE_DATA)
    print()

    # 额外：字段统计
    keyword_count = len(SITE_DATA["keywords"])
    tag_count = len(SITE_DATA["tags"])
    print(f"提示：共包含 {keyword_count} 个关键词，{tag_count} 个标签。")
    print("生成完毕。")

if __name__ == "__main__":
    main()