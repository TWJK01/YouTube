import requests
import re

CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
    "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams"
}

def get_live_urls(name, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    found_urls = []
    try:
        response = requests.get(url, headers=headers, timeout=20)
        html = response.text

        # 核心邏輯：尋找所有包含影片資訊的 JSON 片段
        # 我們尋找包含 "style":"LIVE" 的影片渲染器區塊
        video_segments = re.findall(r'(\{"videoRenderer":\{"videoId":"[^"]+".*?"style":"LIVE"\}\})', html)
        
        for segment in video_segments:
            video_id_match = re.search(r'"videoId":"([^"]+)"', segment)
            if video_id_match:
                video_id = video_id_match.group(1)
                full_url = f"https://www.youtube.com/watch?v={video_id}"
                # 避免重複抓取同一個 ID
                entry = f"{name},{full_url}"
                if entry not in found_urls:
                    found_urls.append(entry)
                    
        return found_urls
    except Exception as e:
        print(f"查詢 {name} 時發生錯誤: {e}")
    return []

def main():
    final_list = []
    for name, url in CHANNELS.items():
        print(f"正在檢查: {name}...")
        lives = get_live_urls(name, url)
        if lives:
            final_list.extend(lives)
            print(f"找到直播: {lives}")
        else:
            print(f"{name} 目前沒有直播")

    # 寫入檔案
    with open("live_list.txt", "w", encoding="utf-8") as f:
        if final_list:
            f.write("\n".join(final_list) + "\n")
        else:
            f.write("") 

if __name__ == "__main__":
    main()
