# -*- coding: utf-8 -*-

import sys
import csv
import json


def get_selection(pref_code):
    QUIZ_SELECTION = {
        "01": ["北海道", "新潟県", "青森県", "秋田県"],
        "02": ["青森県", "岩手県", "秋田県", "山形県"],
        "03": ["岩手県", "山形県", "秋田県", "宮城県"],
        "04": ["宮城県", "岩手県", "福島県", "山形県"],
        "05": ["秋田県", "青森県", "山形県", "岩手県"],
        "06": ["山形県", "秋田県", "宮城県", "岩手県"],
        "07": ["福島県", "新潟県", "宮城県", "栃木県"],
        "08": ["茨城県", "栃木県", "群馬県", "福島県"],
        "09": ["栃木県", "茨城県", "群馬県", "福島県"],
        "10": ["群馬県", "栃木県", "福島県", "新潟県"],
        "11": ["埼玉県", "茨城県", "栃木県", "群馬県"],
        "12": ["千葉県", "東京都", "埼玉県", "茨城県"],
        "13": ["東京都", "千葉県", "埼玉県", "神奈川県"],
        "14": ["神奈川県", "兵庫県", "東京都", "千葉県"],
        "15": ["新潟県", "山形県", "富山県", "鳥取県"],
        "16": ["富山県", "石川県", "新潟県", "長野県"],
        "17": ["石川県", "新潟県", "富山県", "福井県"],
        "18": ["福井県", "石川県", "富山県", "京都府"],
        "19": ["山梨県", "長野県", "岐阜県", "群馬県"],
        "20": ["長野県", "山梨県", "岐阜県", "群馬県"],
        "21": ["岐阜県", "長野県", "滋賀県", "秋田県"],
        "22": ["静岡県", "神奈川県", "愛知県", "山梨県"],
        "23": ["愛知県", "静岡県", "三重県", "神奈川県"],
        "24": ["三重県", "愛知県", "和歌山県", "滋賀県"],
        "25": ["滋賀県", "愛知県", "福井県", "京都府"],
        "26": ["京都府", "奈良県", "和歌山県", "滋賀県"],
        "27": ["大阪府", "兵庫県", "東京都", "愛知県"],
        "28": ["兵庫県", "大阪府", "広島県", "岡山県"],
        "29": ["奈良県", "京都府", "和歌山県", "滋賀県"],
        "30": ["和歌山県", "奈良県", "京都府", "三重県"],
        "31": ["鳥取県", "島根県", "山口県", "兵庫県"],
        "32": ["島根県", "鳥取県", "山口県", "広島県"],
        "33": ["岡山県", "香川県", "兵庫県", "広島県"],
        "34": ["広島県", "山口県", "岡山県", "福岡県"],
        "35": ["山口県", "岡山県", "広島県", "福岡県"],
        "36": ["徳島県", "高知県", "香川県", "愛媛県"],
        "37": ["香川県", "徳島県", "愛媛県", "高知県"],
        "38": ["愛媛県", "高知県", "徳島県", "香川県"],
        "39": ["高知県", "和歌山県", "徳島県", "愛媛県"],
        "40": ["福岡県", "山口県", "熊本県", "佐賀県"],
        "41": ["佐賀県", "福岡県", "熊本県", "長崎県"],
        "42": ["長崎県", "佐賀県", "熊本県", "大分県"],
        "43": ["熊本県", "大分県", "宮崎県", "鹿児島県"],
        "44": ["大分県", "鹿児島県", "宮崎県", "熊本県"],
        "45": ["宮崎県", "鹿児島県", "大分県", "熊本県"],
        "46": ["鹿児島県", "宮崎県", "沖縄県", "長崎県"],
        "47": ["沖縄県", "東京都", "鹿児島県", "長崎県"],
    }
    selections = []
    pref_code_ = ("00" + pref_code)[-2:]
    it = iter(QUIZ_SELECTION[pref_code_])
    selections.append({"text": next(it), "correct": True})
    for i in it:
        selections.append({"text": i, "correct": False})
    return selections


def convert_json():
    inputf = sys.stdin
    outputf = sys.stdout
    reader = csv.DictReader(inputf, delimiter="\t")
    quizzes = []

    for row in reader:
        if row['spottitle'] == '':
            continue
        quizzes.append({
            "url": row["url"],
            "thumburl": row["thumb_url"],
            "photo-title": row["title"],
            "title": row["spottitle"],
            "subtitle": row["subtitle"],
            "lat": float(row["lat"]),
            "lon": float(row["lon"]),
            "selections": get_selection(row["prefecture_code"]),
            "description": row["description"],
        })
    json.dump({"quizzes": quizzes}, outputf, ensure_ascii=False)


if __name__ == "__main__":
    convert_json()
