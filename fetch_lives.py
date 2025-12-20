import yt_dlp
import os

# 頻道清單：名稱與網址
channels = {
    "華視新聞": "https://www.youtube.com/@CtsTw/live",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/live",
    "HOP Sports": "https://www.youtube.com/@HOPSports/live",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/live"
}

def check_live(name, url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # 判斷是否為正在進行的直播
            if info.get('is_live') or info.get('live_status') == 'is_live':
                return f"{name},{info['webpage_url']}"
    except Exception:
        return None
    return None

def main():
    live_results = []
    for name, url in channels.items():
        result = check_live(name, url)
        if result:
            live_results.append(result)
    
    # 寫入檔案 (若無直播則清空或保持空白)
    with open("live_list.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(live_results))

if __name__ == "__main__":
    main()
