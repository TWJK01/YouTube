import yt_dlp

# 定義頻道與已知直播 ID (木棉花常駐直播)
CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
    "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams"
}

# 木棉花常駐直播 ID 清單，用於繞過海外 IP 找不到分頁的問題
MUSE_STREAMS = [
    "https://www.youtube.com/watch?v=S-tS_e9Wl3E", # 蠟筆小新
    "https://www.youtube.com/watch?v=2m687TIn_04", # 我們這一家
    "https://www.youtube.com/watch?v=S37f_9mO9uY", # 中華一番
    "https://www.youtube.com/watch?v=G6X8UAnV_O8"  # 哆啦A夢
]

def get_live_info():
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-10',
        'ignoreerrors': True,
        'no_warnings': True,
        'extra_headers': {'Accept-Language': 'zh-TW'}
    }
    
    results = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 第一部分：動態掃描頻道
        for name, url in CHANNELS.items():
            print(f"正在檢查頻道: {name}...")
            try:
                info = ydl.extract_info(url, download=False)
                if info and 'entries' in info:
                    for entry in info['entries']:
                        if entry.get('live_status') == 'is_live':
                            results.append(f"{entry.get('title')},https://www.youtube.com/watch?v={entry.get('id')}")
                            print(f"  [成功] 找到直播: {entry.get('title')}")
            except:
                continue

        # 第二部分：針對木棉花進行強制偵測 (處理地區封鎖)
        print("正在執行木棉花專項偵測...")
        for url in MUSE_STREAMS:
            try:
                info = ydl.extract_info(url, download=False)
                if info and info.get('is_live'):
                    results.append(f"{info.get('title')},{url}")
                    print(f"  [成功] 強制偵測找到: {info.get('title')}")
            except:
                continue
                
    return list(dict.fromkeys(results)) # 去除重複

def main():
    live_list = get_live_info()
    with open("live_list.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(live_list) + ("\n" if live_list else ""))
    print(f"\n任務完成。共偵測到 {len(live_list)} 個直播。")

if __name__ == "__main__":
    main()
