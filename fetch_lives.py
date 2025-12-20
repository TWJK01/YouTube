import requests
import re

CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/live",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/live",
    "HOP Sports": "https://www.youtube.com/@HOPSports/live",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/live"
}

def get_live_url(name, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        text = response.text
        
        # 關鍵判斷：必須同時包含 isLive:true 且不包含預告標記
        if '"isLive":true' in text and '"style":"LIVE"' in text:
            video_id_match = re.search(r'"videoId":"([^"]+)"', text)
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
    
    with open("live_list.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results))
        if results:
            print(f"Successfully found {len(results)} live(s).")

if __name__ == "__main__":
    main()
