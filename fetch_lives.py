import yt_dlp

CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/live", # 改用 /live 強制導向
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
                # extract_info 會處理 /live 的自動跳轉
                info = ydl.extract_info(url, download=False)
                
                if not info:
                    continue
                
                # 處理 entries (列表) 或 直接是個影片資訊 (單一直播)
                entries = info.get('entries', [info])
                
                for entry in entries:
                    if not entry: continue
                    
                    # 狀態判斷：正在直播 或 標題包含直播
                    status = entry.get('live_status')
                    title = entry.get('title', 'Unknown Title')
                    
                    # 如果是正在直播 (is_live) 或 列表中的直播項目
                    if status == 'is_live' or entry.get('is_live') is True:
                        video_id = entry.get('id')
                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                        results.append(f"{title},{video_url}")
                        print(f"  [成功] {title}")
                        
            except Exception as e:
                print(f"  [跳過] {name} 檢查失敗: {e}")
                
    return results

def main():
    live_list = get_live_info()
    
    # 移除重複項目
    final_list = list(dict.fromkeys(live_list))

    with open("live_list.txt", "w", encoding="utf-8") as f:
        if final_list:
            f.write("\n".join(final_list) + "\n")
        else:
            f.write("") # 保持空檔
            
    print(f"\n任務結束。共找到 {len(final_list)} 個直播。")

if __name__ == "__main__":
    main()
