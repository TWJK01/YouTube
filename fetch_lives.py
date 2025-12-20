import requests
import re
import json

CHANNELS = {
    "華視新聞": "https://www.youtube.com/@CtsTw/streams",
    "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
    "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
    "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams"
}

def get_live_from_streams(name, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # 提取 YouTube 頁面的初始資料 JSON
        data_text = re.search(r'var ytInitialData = (\{.*?\});', response.text).group(1)
        data = json.loads(data_text)
        
        # 進入 JSON 結構尋找影片列表
        # 結構路徑通常為: contents -> twoColumnBrowseResultsRenderer -> tabs -> [1] (Streams) -> content -> richGridRenderer -> contents
        tabs = data['contents']['twoColumnBrowseResultsRenderer']['tabs']
        
        # 找到「直播」分頁 (通常是索引值 1 或 2，這裡用名稱過濾較保險)
        streams_tab = next(tab for tab in tabs if 'richGridRenderer' in tab.get('tabRenderer', {}).get('content', {}))
        contents = streams_tab['tabRenderer']['content']['richGridRenderer']['contents']
        
        found_links = []
        for item in contents:
            if 'richItemRenderer' not in item: continue
            video_data = item['richItemRenderer']['content'].get('videoRenderer', {})
            
            # 判斷是否帶有 "LIVE" 或 "直播中" 標籤
            is_live = False
            badges = video_data.get('badges', [])
            for badge in badges:
                label = badge.get('metadataBadgeRenderer', {}).get('label', '')
                if label in ["LIVE", "直播中"]:
                    is_live = True
                    break
            
            if is_live:
                video_id = video_data.get('videoId')
                found_links.append(f"{name},https://www.youtube.com/watch?v={video_id}")
        
        return found_links
    except Exception as e:
        print(f"Error scraping {name}: {e}")
    return []

def main():
    all_results = []
    for name, url in CHANNELS.items():
        print(f"Checking {name} streams...")
        lives = get_live_from_streams(name, url)
        if lives:
            all_results.extend(lives)
            print(f"Found {len(lives)} live(s) for {name}")

    with open("live_list.txt", "w", encoding="utf-8") as f:
        if all_results:
            f.write("\n".join(all_results) + "\n")
        else:
            f.write("") # 清空檔案代表目前無直播

if __name__ == "__main__":
    main()
