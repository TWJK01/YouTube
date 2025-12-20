import yt_dlp

# 請在此處放入您所有的頻道清單
CATEGORIES = {
    "台灣,#genre#": {
        "台灣地震監視": "https://www.youtube.com/@台灣地震監視/streams",
        "華視新聞": "https://www.youtube.com/@CtsTw/streams",
        "東森新聞": "https://www.youtube.com/@newsebc/streams",
        # ... 貼上其餘台灣分類頻道
    },
    "綜藝,#genre#": {
        "MIT台灣誌": "https://www.youtube.com/@ctvmit/streams",
        "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams",
        # ... 貼上其餘綜藝分類頻道
    },
    "少兒,#genre#": {
        "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
        "Ani-One中文官方動畫頻道": "https://www.youtube.com/@AniOneAnime/streams",
        # ... 貼上其餘少兒分類頻道
    },
    "體育,#genre#": {
        "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
        # ... 貼上其餘體育分類頻道
    },
    "風景,#genre#": {
        "台北觀光即時影像": "https://www.youtube.com/@taipeitravelofficial/streams",
        "陽明山國家公園": "https://www.youtube.com/@ymsnpinfo/streams",
        # ... 貼上其餘風景分類頻道
    }
}

def get_live_info():
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-5',
        'ignoreerrors': True,
        'no_warnings': True,
        'extra_headers': {
            'Accept-Language': 'zh-TW',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    }
    
    final_output = []
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for genre, channels in CATEGORIES.items():
            genre_results = []
            print(f"正在檢查分類: {genre}")
            
            for display_name, url in channels.items():
                try:
                    # 木棉花地區限制補救
                    target_url = url
                    if "Muse_Family" in url:
                        target_url = "https://www.youtube.com/@Muse_Family/live"
                    
                    info = ydl.extract_info(target_url, download=False)
                    if not info: continue
                    
                    entries = info.get('entries', [info])
                    for entry in entries:
                        if not entry: continue
                        if entry.get('live_status') == 'is_live' or entry.get('is_live') is True:
                            title = entry.get('title', display_name)
                            v_id = entry.get('id')
                            if v_id:
                                v_url = f"https://www.youtube.com/watch?v={v_id}"
                                genre_results.append(f"{title},{v_url}")
                                print(f"  [FOUND] {display_name}")
                except:
                    continue
            
            # 如果該分類下有找到直播，則加入清單並在末尾加一個空行
            if genre_results:
                final_output.append(genre)
                final_output.extend(genre_results)
                final_output.append("") # 增加間隔空行
                
    return final_output

def main():
    results = get_live_info()
    with open("live_list.txt", "w", encoding="utf-8") as f:
        # 使用 join 並過濾掉最後一個多餘的空行
        f.write("\n".join(results).strip() + "\n")
    print("\n任務結束，live_list.txt 已更新
