import os
import json

# GitHubパス情報（あなたのプロジェクトに合わせてね！）
github_user = "Official-MzCG"
repo_name = "barossa-data"
branch_name = "main"
character_name = "Varrosa"

# フォルダ構成前提: ./emotion/感情/表情/*.png
base_dir = "emotion"
output_file = "emotion_data.json"

json_data = []

for root, _, files in os.walk(base_dir):
    parts = root.split(os.sep)
    if len(parts) >= 3:
        emotion = parts[1]
        expression = parts[2]
        for file in files:
            if file.lower().endswith(".png"):
                url = f"https://raw.githubusercontent.com/{github_user}/{repo_name}/{branch_name}/{base_dir}/{emotion}/{expression}/{file}"
                json_data.append({
                    "url": url,
                    "emotion": [emotion],
                    "expression": expression,
                    "character": character_name
                })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print(f"✅ JSON出力完了！ → {output_file}")
