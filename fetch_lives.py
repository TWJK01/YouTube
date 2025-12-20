import yt_dlp

# 使用最直接的網址
CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/live", # 強制存取直播路徑
    "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams"
}

def get_live_info():
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-10',
        'ignoreerrors': True,
        'no_warnings': True,
        'extra_headers': {
            'Accept-Language': 'zh-TW',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    }
    
    results = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for name, url in CHANNELS.items():
            print(f"正在檢查: {name}...")
            try:
                # 關鍵：使用 process=False 配合特定路徑
                info = ydl.extract_info(url, download=False)
                if not info:
                    continue
                
                # 處理 entries (列表) 或直接是影片 (單路徑)
                entries = info.get('entries', [info])
                
                for entry in entries:
                    if not entry: continue
                    
                    # 狀態判定：只要 metadata 顯示是直播或正在播放
                    is_live = entry.get('live_status') == 'is_live' or entry.get('is_live') is True
                    
                    if is_live:
                        title = entry.get('title', '直播中')
                        video_id = entry.get('id')
                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                        
                        line = f"{title},{video_url}"
                        results.append(line)
                        print(f"  [成功找到] {title}")
            except Exception:
                print(f"  [跳過] {name} 無法存取")
                
    return results

def main():
    live_list = get_live_info()
    # 去除重複
    final_list = list(dict.fromkeys(live_list))

    with open("live_list.txt", "w", encoding="utf-8") as f:
        if final_list:
            f.write("\n".join(final_list) + "\n")
        else:
            f.write("")
            
    print(f"\n掃描結束。共偵測到 {len(final_list)} 個直播網址。")

if __name__ == "__main__":
    main()
