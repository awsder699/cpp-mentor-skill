#!/usr/bin/env python3
"""校验并打包 cpp-mentor Skill。

用法:
    python scripts/package_skill.py <skill-dir> [output-dir]

示例:
    python scripts/package_skill.py cpp-mentor/ dist/

校验项: SKILL.md 存在、YAML frontmatter 格式、name 命名规范、
        name 与目录名一致、description 完整性、references 文件可读。
校验通过后在 output-dir 生成 <skill-name>.zip（zip 内保持
<skill-name>/ 目录结构，解压即可安装）。
"""

import re
import sys
import zipfile
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text):
    """提取 YAML frontmatter 的顶层键值（仅支持单行 key: value）。"""
    m = FM_RE.match(text)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def validate(skill_dir):
    """返回错误列表，空列表表示通过。"""
    errors = []

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return ["缺少 SKILL.md"]

    fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if fm is None:
        errors.append("SKILL.md 缺少 YAML frontmatter（--- 包裹的 name/description）")
        return errors

    name = fm.get("name", "")
    if not NAME_RE.match(name):
        errors.append(
            f"name 不合规: {name!r}（须为小写字母/数字，以连字符分隔，如 cpp-mentor）"
        )
    if name and name != skill_dir.name:
        errors.append(f"name({name!r}) 与目录名({skill_dir.name!r}) 不一致")

    desc = fm.get("description", "")
    if len(desc) < 20:
        errors.append("description 过短：须说明 Skill 做什么、何时触发（建议 50 字以上）")
    if not any(
        kw in desc.lower()
        for kw in ("cpp", "c++", "教学", "teach", "mentor", "讲解", "调试", "debug")
    ):
        errors.append("description 未体现 C++ 教学主题，触发匹配可能不准确")

    refs = skill_dir / "references"
    if refs.is_dir():
        for f in sorted(refs.glob("*.md")):
            if not f.read_text(encoding="utf-8").strip():
                errors.append(f"references/{f.name} 内容为空")
    else:
        errors.append("缺少 references/ 目录（教学资料应放在 references 中按需加载）")

    return errors


def package(skill_dir, out_dir):
    errors = validate(skill_dir)
    if errors:
        print("❌ 校验失败：")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"{skill_dir.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                zf.write(f, f.relative_to(skill_dir.parent))

    print(f"✅ 校验通过，已打包: {zip_path}")
    print("   zip 内结构（解压后可直接安装）:")
    with zipfile.ZipFile(zip_path) as zf:
        for n in zf.namelist():
            print(f"     {n}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    skill = Path(sys.argv[1]).resolve()
    if not skill.is_dir():
        print(f"❌ 目录不存在: {skill}")
        sys.exit(1)
    out = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else skill.parent / "dist"
    package(skill, out)
