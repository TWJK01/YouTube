import yt_dlp

CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
    "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams"
}

def get_live_info():
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-15', # 檢查更多項目以確保抓到多個直播
        'ignoreerrors': True,
        'no_warnings': True,
        'extra_headers': {
            'Accept-Language': 'zh-TW'
        }
    }
    
    results = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for name, url in CHANNELS.items():
            print(f"正在檢查: {name}...")
            try:
                info = ydl.extract_info(url, download=False)
                if info and 'entries' in info:
                    for entry in info['entries']:
                        # 關鍵判斷：除了 is_live，木棉花這類馬拉松有時在 Metadata 標註為 was_live 但實際正在播
                        # 所以我們檢查 live_status 是否包含 live 且標題不含「預告」
                        status = entry.get('live_status', '')
                        title = entry.get('title', '')
                        
                        if status == 'is_live' or (status == 'is_upcoming' and '馬拉松' in title):
                            video_id = entry.get('id')
                            if video_id:
                                video_url = f"https://www.youtube.com/watch?v={video_id}"
                                # 嚴格輸出格式：網頁標題,網址
                                results.append(f"{title},{video_url}")
                                print(f"  [成功] {title}")
            except Exception as e:
                print(f"  [錯誤] {name} 檢查失敗: {e}")
                
    return results

def main():
    live_list = get_live_info()
    # 去除重複
    live_list = list(dict.fromkeys(live_list))

    with open("live_list.txt", "w", encoding="utf-8") as f:
        if live_list:
            f.write("\n".join(live_list) + "\n")
        else:
            f.write("")
            
    print(f"\n掃描結束。共找到 {len(live_list)} 個直播。")

if __name__ == "__main__":
    main()
