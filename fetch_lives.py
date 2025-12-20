import yt_dlp

CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
    "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams"
}

def get_live_urls_ytdlp():
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-10',  # 增加檢查數量以確保抓到多個直播
        'ignoreerrors': True,
        'no_warnings': True,
    }
    
    found_urls = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for name, url in CHANNELS.items():
            print(f"正在檢查: {name}...")
            try:
                info = ydl.extract_info(url, download=False)
                if info and 'entries' in info:
                    for entry in info['entries']:
                        # 改良判斷邏輯：檢查 live_status 或 標題關鍵字
                        title = entry.get('title', '')
                        is_live_status = entry.get('live_status') == 'is_live'
                        
                        if is_live_status or "直播" in title:
                            video_id = entry.get('id')
                            if video_id:
                                full_url = f"https://www.youtube.com/watch?v={video_id}"
                                found_urls.append(f"{name},{full_url}")
                                print(f"  [!] 找到直播：{name} - {title}")
            except Exception as e:
                print(f"  [x] 檢查 {name} 時出錯: {e}")
    
    return found_urls

def main():
    final_results = get_live_urls_ytdlp()
    # 去除重複項
    final_results = list(dict.fromkeys(final_results))

    with open("live_list.txt", "w", encoding="utf-8") as f:
        if final_results:
            f.write("\n".join(final_results) + "\n")
        else:
            f.write("")
            
    print(f"\n任務完成，共找到 {len(final_results)} 個直播。")

if __name__ == "__main__":
    main()
