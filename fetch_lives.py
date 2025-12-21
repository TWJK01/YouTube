import yt_dlp
import re

# 1. 完整頻道分類與來源定義
CATEGORIES = {
    "國會,#genre#": {
        "國會頻道": "https://www.youtube.com/@parliamentarytv/streams"
    },
    "風景,#genre#": {
        "台北觀光即時影像": "https://www.youtube.com/@taipeitravelofficial/streams",
        "遊桃園 Taoyuan Travel": "https://www.youtube.com/@TaoyuanTravel/streams",
        "新北旅客 New Taipei Tour": "https://www.youtube.com/@ntctour/streams",
        "高雄旅遊網": "https://www.youtube.com/@travelkhh/streams",
        "阿里山國家風景區": "https://www.youtube.com/@Alishannsa/streams",
        "東部海岸國家風景區": "https://www.youtube.com/@eastcoastnsa0501/streams"
    }
}

# 2. 地標翻譯對照表 (針對純英文或辨識困難標題的保底機制)
LANDMARK_MAP = {
    # 高雄系列
    "Shoushan Lovers": "壽山情人觀景台", "Lianchihtan": "蓮池潭", "Lotus Pond": "蓮池潭",
    "Cijin": "旗津", "Love River": "愛河", "Sizihwan": "西子灣",
    # 桃園系列
    "Baling": "巴陵大橋", "Amuping": "阿姆坪", "Ginger Island": "薑絲島", "Cihu": "慈湖",
    "Shihmen Reservoir": "石門水庫", "Daxi Old Street": "大溪老街", "Jiaobanshan": "角板山",
    "Lala Mountain": "拉拉山", "Xuchuogang": "許厝港濕地", "Xiao Wulai": "小烏來",
    # 阿里山系列
    "Fenqihu": "奮起湖", "Eryanping": "二延平", "Taiping Suspension Bridge": "太平雲梯",
    "Lijia": "里佳資訊站", "Sheng-Li Farm": "生力農場", "Niupuzai": "牛埔仔大草原",
    # 東部海岸系列
    "Chaikou": "綠島柴口", "Fanchuanbi": "帆船鼻", "Shitiping": "石梯坪", "Changhong Bridge": "長虹橋",
    "Dashshibi": "大石鼻山", "Jialulan": "加路蘭", "Torik": "都歷", "Sanxiantai": "三仙台"
}

def extract_best_title(v_title, nickname):
    """
    智慧標題優化：自動處理國會會議區分與風景地標提取。
    """
    # A. 國會頻道：提取具體會議名稱 (例如：司法及法制委員會)
    if "國會頻道" in nickname:
        segments = re.split(r'[\|\-\—\–]', v_title)
        if len(segments) > 1:
            return f"【國會頻道】{segments[0].strip()}"
        return f"【國會頻道】{v_title.replace('立法院議事轉播', '').strip()}"

    # B. 風景頻道品牌標準化
    if "高雄" in nickname or "Kaohsiung" in v_title: brand = "高雄旅遊網"
    elif "Taipei" in nickname or "台北" in v_title: brand = "Taipei Live Cam"
    elif "桃園" in nickname or "Taoyuan" in v_title: brand = "遊桃園"
    elif "新北" in nickname or "New Taipei" in v_title: brand = "新北旅客"
    elif "阿里山" in nickname or "Alishan" in v_title: brand = "阿里山"
    elif "東部海岸" in nickname or "East Coast" in v_title: brand = "東部海岸"
    else: brand = nickname

    # C. 風景地標提取 (移除括號並反向搜尋核心中文)
    clean_title = re.sub(r'[【\[\(].*?[】\]\)]', '', v_title).strip()
    segments = re.split(r'[\|\-\—\–]', clean_title)
    
    landmark = ""
    for seg in reversed(segments):
        chinese_found = "".join(re.findall(r'[\u4e00-\u9fa5]+', seg))
        # 移除重複的城市名與常見噪音字
        noises = ["即時影像", "直播", "頻道", "官方", "高雄", "桃園", "台北", "新北", "觀光", "風景區", "管理處"]
        for n in noises:
            chinese_found = chinese_found.replace(n, "")
        if len(chinese_found) >= 2:
            landmark = chinese_found
            break

    # D. 英文翻譯救援機制
    if len(landmark) < 2:
        for eng, chi in LANDMARK_MAP.items():
            if eng.lower() in v_title.lower():
                landmark = chi
                break

    # E. 最終保底清理
    if not landmark:
        landmark = re.sub(r'(?i)Live Cam|4K|Stream|即時影像|Taiwan', '', clean_title).strip()
        landmark = landmark.split('|')[0].strip() if landmark else "即時影像"

    return f"【{brand}】{landmark}"

def get_live_info():
    """
    抓取 YouTube 直播資訊並進行優化處理。
    """
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-15',
        'ignoreerrors': True,
        'no_warnings': True,
        'extra_headers': {
            'Accept-Language': 'zh-TW,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    }
    
    final_output = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for genre, channels in CATEGORIES.items():
            genre_list = []
            seen_urls = set()
            print(f">>> 正在掃描並優化: {genre}")
            
            for nickname, url in channels.items():
                try:
                    info = ydl.extract_info(url, download=False)
                    if not info: continue
                    
                    entries = info.get('entries', []) or ([info] if info.get('live_status') == 'is_live' else [])

                    for entry in entries:
                        if not entry or not (entry.get('live_status') == 'is_live' or entry.get('is_live')):
                            continue
                            
                        v_url = f"https://www.youtube.com/watch?v={entry.get('id')}"
                        if v_url not in seen_urls:
                            # 套用整合優化方案
                            final_title = extract_best_title(entry.get('title', ''), nickname)
                            genre_list.append(f"{final_title},{v_url}")
                            seen_urls.add(v_url)
                except Exception:
                    continue
            
            if genre_list:
                final_output.append(genre)
                final_output.extend(genre_list)
                final_output.append("") 
                
    return final_output

if __name__ == "__main__":
    results = get_live_info()
    with open("live_list.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results).strip() + "\n")
    print("\n✅ 國會、高雄與全台風景優化整合完成！請檢查 live_list.txt")
