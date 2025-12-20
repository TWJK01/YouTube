import requests
import re
import os

# 頻道配置
CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/live",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/live",
    "HOP Sports": "https://www.youtube.com/@HOPSports/live",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/live"
}

def get_live_url(name, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # 檢查 HTML 中是否含有正在直播的標記
        if '{"style":"LIVE","label":"直播中"}' in response.text or '"isLive":true' in response.text:
            # 提取當前的影片 ID
            video_id_match = re.search(r'"videoPageRenderer":\{"videoId":"([^"]+)"', response.text)
            if not video_id_match:
                video_id_match = re.search(r'vi/([^/]+)/maxresdefault', response.text)
            
            if video_id_match:
                video_id = video_id_match.group(1)
                return f"{name},https://www.youtube.com/watch?v={video_id}"
    except Exception as e:
        print(f"Error checking {name}: {e}")
    return None

def main():
    results = []
    for name, url in CHANNELS.items():
        print(f"Checking {name}...")
        live_info = get_live_url(name, url)
        if live_info:
            results.append(live_info)
            print(f"Found Live: {live_info}")
    
    # 強制寫入檔案，即使為空也會清空舊內容
    with open("live_list.txt", "w", encoding="utf-8") as f:
        if results:
            f.write("\n".join(results) + "\n")
        else:
            f.write("") # 保持檔案存在但內容清空

if __name__ == "__main__":
    main()
