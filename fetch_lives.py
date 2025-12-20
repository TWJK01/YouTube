import yt_dlp

# 頻道清單
CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
    "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams"
}

def get_live_info():
    # 這裡的設定是為了應對 YouTube 在海外 IP 上的限制
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-10',  # 檢查最新的 10 個影片
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
                # 提取資訊
                info = ydl.extract_info(url, download=False)
                
                if info and 'entries' in info:
                    for entry in info['entries']:
                        if not entry: continue
                        
                        # 同時檢查 live_status 與影片標題
                        # 木棉花的直播常被標註為 is_upcoming 或 was_live，但標題會寫「直播中」
                        status = entry.get('live_status')
                        title = entry.get('title', '')
                        
                        if status == 'is_live' or (status == 'is_upcoming' and '直播中' in title) or (status == 'is_upcoming' and '馬拉松' in title):
                            video_id = entry.get('id')
                            video_url = f"https://www.youtube.com/watch?v={video_id}"
                            
                            # 格式：網頁標題,網址
                            results.append(f"{title},{video_url}")
                            print(f"  [找到] {title}")
                            
            except Exception as e:
                print(f"  [跳過] {name} 檢查失敗")
                
    return results

def main():
    live_list = get_live_info()
    
    # 去除重複項並保持順序
    seen = set()
    final_list = []
    for item in live_list:
        if item not in seen:
            final_list.append(item)
            seen.add(item)

    # 寫入檔案
    with open("live_list.txt", "w", encoding="utf-8") as f:
        if final_list:
            f.write("\n".join(final_list) + "\n")
        else:
            f.write("") # 清空檔案
            
    print(f"\n掃描結束。共找到 {len(final_list)} 個直播網址。")

if __name__ == "__main__":
    main()
