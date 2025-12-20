import yt_dlp
import os

# 頻道清單
CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
    "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams"
}

def get_live_info():
    # 配置 yt-dlp
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-10', # 檢查前 10 支影片
        'ignoreerrors': True,
        'no_warnings': True,
        'extra_headers': {
            'Accept-Language': 'zh-TW' # 確保抓到中文標題
        }
    }
    
    results = []
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for name, url in CHANNELS.items():
            print(f"正在檢查: {name}...")
            try:
                # 提取頻道 Streams 頁面資訊
                info = ydl.extract_info(url, download=False)
                
                if info and 'entries' in info:
                    for entry in info['entries']:
                        # 嚴格篩選：只抓取「正在直播」的影片
                        if entry.get('live_status') == 'is_live':
                            video_title = entry.get('title')
                            video_id = entry.get('id')
                            video_url = f"https://www.youtube.com/watch?v={video_id}"
                            
                            # 格式：網頁標題,網址
                            results.append(f"{video_title},{video_url}")
                            print(f"  [LIVE] 找到：{video_title}")
            except Exception as e:
                print(f"  [ERROR] {name} 檢查出錯: {e}")
                
    return results

def main():
    live_list = get_live_info()
    
    # 寫入文字檔 (UTF-8)
    with open("live_list.txt", "w", encoding="utf-8") as f:
        if live_list:
            f.write("\n".join(live_list) + "\n")
        else:
            f.write("") # 沒直播時保持空檔
            
    print(f"\n任務完成。共偵測到 {len(live_list)} 個正在直播的網址。")

if __name__ == "__main__":
    main()
