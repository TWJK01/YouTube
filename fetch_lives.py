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
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'PREF=hl=zh-TW' # 強制 YouTube 回傳中文界面，方便判斷
    }
    found_urls = []
    try:
        response = requests.get(url, headers=headers, timeout=20)
        html = response.text

        # 1. 先抓出所有影片區塊 (videoRenderer)
        # 2. 在區塊中尋找是否有 "正在觀看" 或 "LIVE"
        items = re.findall(r'\{"videoRenderer":\{"videoId":"[^"]+".*?\}\}', html)
        
        for item in items:
            # 排除已結束的直播（已結束的會顯示 "觀看次數"，正在直播的會顯示 "人在觀看" 或 "LIVE"）
            if '"style":"LIVE"' in item or '人在觀看' in item or 'watching' in item:
                video_id_match = re.search(r'"videoId":"([^"]+)"', item)
                if video_id_match:
                    video_id = video_id_match.group(1)
                    full_url = f"https://www.youtube.com/watch?v={video_id}"
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
            # 去重處理
            for l in lives:
                if l not in final_list:
                    final_list.append(l)
            print(f">>> 成功找到 {name} 的直播網址！")
        else:
            print(f"--- {name} 目前真的沒有直播")

    with open("live_list.txt", "w", encoding="utf-8") as f:
        if final_list:
            f.write("\n".join(final_list) + "\n")
        else:
            f.write("") 
    print(f"\n任務結束，共抓取到 {len(final_list)} 個直播。")

if __name__ == "__main__":
    main()
