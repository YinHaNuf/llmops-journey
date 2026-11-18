# 第1章结课项目：学习记录器
import json
from datetime import datetime

FILE = "study_log.json"

class StudyLogger:
    def __init__(self):
        self.records = self._load()

    def _load(self):
        """从文件读回已有记录"""
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save(self):
        """把记录写入文件"""
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=2)

    def add(self):
        subject = input("学科：")
        hours = float(input("小时数："))
        note = input("备注（可跳过）：")
        self.records.append({
            "date": datetime.now().strftime("%m-%d %H:%M"),
            "subject": subject,
            "hours": hours,
            "note": note,
        })
        self._save()
        print("已记录 ✓")

    def stats(self):
        if not self.records:
            print("还没有记录。")
            return
        total = sum(r["hours"] for r in self.records)
        print(f"共 {len(self.records)} 条，累计 {total:.1f} 小时")

    def run(self):
        print(f"已加载 {len(self.records)} 条记录")
        while True:
            c = input("\n1.记录  2.统计  3.退出\n选：")
            if c == "1":
                self.add()
            elif c == "2":
                self.stats()
            elif c == "3":
                break

if __name__ == "__main__":
    StudyLogger().run()