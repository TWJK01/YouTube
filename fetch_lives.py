import yt_dlp
import re

# 頻道分類清單
CATEGORIES = {
    "風景,#genre#": {
        "台北觀光即時影像": "https://www.youtube.com/@taipeitravelofficial/streams",
        "新北旅客": "https://www.youtube.com/@ntctour/streams",
        "基隆旅遊": "https://www.youtube.com/@klcg_travel/streams",
        "阿里山國家風景區": "https://www.youtube.com/@Alishannsa/streams",
        "東部海岸風景區": "https://www.youtube.com/@eastcoastnsa0501/streams",
        "高雄旅遊網": "https://www.youtube.com/@travelkhh/streams"
    },
    "台灣,#genre#": {
        "台視新聞": "https://www.youtube.com/@TTV_NEWS/streams",
        "中視新聞": "https://www.youtube.com/@chinatvnews/streams",
        "華視新聞": "https://www.youtube.com/@CtsTw/streams",
        "民視新聞網": "https://www.youtube.com/@FTV_News/streams",
        "公視新聞網": "https://www.youtube.com/@PNNPTS/streams",
        "東森新聞": "https://www.youtube.com/@newsebc/streams",
        "三立LIVE新聞": "https://www.youtube.com/@setnews/streams",
        "TVBS NEWS": "https://www.youtube.com/@TVBSNEWS01/streams",
        "中天新聞": "https://www.youtube.com/@中天新聞CtiNews/streams"
    },
    "少兒,#genre#": {
        "YOYOTV": "https://www.youtube.com/@yoyotvebc/streams",
        "momokids親子台": "https://www.youtube.com/@momokidsYT/streams",
        "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
        "Ani-One中文官方動畫頻道": "https://www.youtube.com/@AniOneAnime/streams"
    }
}

def get_full_display_title(v_title, nickname):
    """
    提取標題中完整的中文部分，確保風景類地標清晰可見。
    """
    # 1. 處理品牌前綴 (e.g., 【Taipei Live Cam】)
    if "台北" in nickname or "Taipei" in v_title:
        brand = "Taipei Live Cam"
    elif "新北" in nickname:
        brand = "新北旅客"
    else:
        # 從標題括號提取或使用自定義暱稱
        bracket_match = re.search(r'[【\[](.*?)[】\]]', v_title)
        brand = bracket_match.group(1) if bracket_match else nickname
        # 移除前綴中多餘的英文噪音
        brand = re.sub(r'(?i)4K|Live|Cam|Stream', '', brand).strip()

    # 2. 提取完整的中文描述 (跳過英文地點名，直取中文地標)
    # 移除括號內容
    main_text = re.sub(r'[【\[].*?[】\]]', '', v_title).strip()
    
    # 匹配中文字符串 (包含中文標點)
    chinese_pattern = r'[\u4e00-\u9fa5\uff01-\uff5e\u3000-\u303f0-9]+'
    chinese_matches = re.findall(chinese_pattern, main_text)
    
    # 將找到的中文地標組合
    full_chinese = " ".join(chinese_matches)

    # 3. 組合最終標題
    if full_chinese:
        # 移除重複的頻道名，保留純地標內容
        clean_desc = full_chinese.replace(nickname, "").replace("即時影像", "").strip()
        if not clean_desc: clean_desc = full_chinese
        return f"【{brand}】{clean_desc}"
    
    # 若完全無中文，回傳原始標題前段
    return f"【{brand}】{main_text[:25]}"

def get_live_info():
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
            print(f">>> 正在掃描分類: {genre}")
            
            for nickname, url in channels.items():
                try:
                    info = ydl.extract_info(url, download=False)
                    if not info: continue
                    
                    entries = info.get('entries', [])
                    if not entries and info.get('live_status') == 'is_live':
                        entries = [info]

                    for entry in entries:
                        if not entry: continue
                        if entry.get('live_status') == 'is_live' or entry.get('is_live'):
                            v_id = entry.get('id')
                            v_url = f"https://www.youtube.com/watch?v={v_id}"
                            
                            if v_id and v_url not in seen_urls:
                                v_raw_title = entry.get('title', '')
                                # 執行標題優化
                                final_title = get_full_display_title(v_raw_title, nickname)
                                
                                genre_list.append(f"{final_title},{v_url}")
                                seen_urls.add(v_url)
                                print(f"  [OK] {final_title}")
                except Exception:
                    continue
            
            if genre_list:
                final_output.append(genre)
                final_output.extend(genre_list)
                final_output.append("") # 分類間隔空行
                
    return final_output

if __name__ == "__main__":
    results = get_live_info()
    with open("live_list.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results).strip() + "\n")
    print("\n✅ 完整標題直播清單已產出！")
