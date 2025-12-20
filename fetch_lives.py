import yt_dlp

CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
    "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams"
}

def get_live_urls_ytdlp(name, url):
    # yt-dlp 配置：只抓取標題和 ID，不下載，過濾直播
    ydl_opts = {
        'quiet': True,
        'extract_flat': 'in_playlist',  # 快速提取列表資訊
        'skip_download': True,
        'playlist_items': '1-5',        # 只檢查前 5 個影片，節省時間
    }
    
    found_urls = []
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 獲取頻道 streams 頁面的影片列表
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:
                for entry in info['entries']:
                    # 關鍵：yt-dlp 會標記影片狀態
                    # live_status 可能為 'is_live', 'is_upcoming', 'was_live'
                    if entry.get('live_status') == 'is_live':
                        video_id = entry.get('id')
                        found_urls.append(f"{name},https://www.youtube.com/watch?v={video_id}")
    except Exception as e:
        print(f"檢查 {name} 時出錯: {e}")
    
    return found_urls

def main():
    final_results = []
    for name, url in CHANNELS.items():
        print(f"正在檢查: {name}...")
        lives = get_live_urls_ytdlp(name, url)
        if lives:
            print(f"  [!] 找到直播：{lives}")
            final_results.extend(lives)
        else:
            print(f"  [x] 目前無直播")

    # 寫入檔案
    with open("live_list.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(final_results))
        if final_results:
            f.write("\n")
            
    print(f"\n任務完成，共找到 {len(final_results)} 個直播。")

if __name__ == "__main__":
    main()
