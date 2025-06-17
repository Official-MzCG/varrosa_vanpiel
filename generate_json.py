import os
import json

# GitHub パス情報（あなたのリポジトリに合わせて修正済！）
github_user = "Official-MzCG"
repo_name = "varrosa_vanpiel"
branch_name = "main"
character_name = "Varrosa"

# ローカルフォルダ構成: ./emotion/感情/表情/*.png
base_dir = "emotion"
output_file = "emotion_grouped.json"

# GitHubの raw URL ベース（↑これが超重要！）
base_url = f"https://raw.githubusercontent.com/{github_user}/{repo_name}/{branch_name}"

# 最終出力するデータ構造
output = {
    "character": character_name,
    "data": []
}

# 内部的に emotion + expression ごとにURLをまとめる
structure = {}

# フォルダ内走査
for root, _, files in os.walk(base_dir):
    parts = root.split(os.sep)
    if len(parts) >= 3:
        emotion = parts[1]
        expression = parts[2]
        key = (emotion, expression)
        if key not in structure:
            structure[key] = []
        for file in files:
            if file.lower().endswith(".png"):
                url = f"{base_url}/{base_dir}/{emotion}/{expression}/{file}"
                structure[key].append(url)

# データ整形して出力に追加
for (emotion, expression), urls in structure.items():
    output["data"].append({
        "emotion": emotion,
        "expression": expression,
        "images": urls
    })

# JSONファイルとして保存
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"✅ JSON出力完了！ → {output_file}")
