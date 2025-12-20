import yt_dlp

# 定義頻道與搜尋路徑
# 針對木棉花，我們改用搜尋模式來嘗試繞過分頁的地區過濾
CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/search?query=直播",
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
                info = ydl.extract_info(url, download=False)
                if not info:
                    continue
                
                entries = info.get('entries', [])
                for entry in entries:
                    if not entry: continue
                    
                    # 寬鬆判定條件：
                    # 1. 官方標記為 is_live
                    # 2. 標題含有「直播」字眼且狀態不為已結束
                    status = entry.get('live_status')
                    title = entry.get('title', '')
                    
                    if status == 'is_live' or (status == 'is_upcoming' and '直播' in title) or ('直播中' in title):
                        video_id = entry.get('id')
                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                        
                        # 格式：網頁標題,網址
                        results.append(f"{title},{video_url}")
                        print(f"  [成功找到] {title}")
            except Exception as e:
                print(f"  [錯誤] {name} 檢查失敗: {e}")
                
    return results

def main():
    live_list = get_live_info()
    
    # 移除重複項目並保持順序
    seen = set()
    final_list = []
    for item in live_list:
        if item not in seen:
            final_list.append(item)
            seen.add(item)

    # 寫入文字檔 (UTF-8)
    with open("live_list.txt", "w", encoding="utf-8") as f:
        if final_list:
            f.write("\n".join(final_list) + "\n")
        else:
            f.write("") # 清空檔案
            
    print(f"\n任務結束。共偵測到 {len(final_list)} 個正在直播。")

if __name__ == "__main__":
    main()
