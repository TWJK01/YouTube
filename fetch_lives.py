import yt_dlp
import re

# 頻道分類清單 (已根據您提供的完整資料整合)
CATEGORIES = {
    "台灣,#genre#": {
        "台灣地震監視": "https://www.youtube.com/@台灣地震監視/streams",
        "台灣颱風論壇": "https://www.youtube.com/@twtybbs2009/streams",		
        "台視新聞": "https://www.youtube.com/@TTV_NEWS/streams",
        "中視新聞": "https://www.youtube.com/@chinatvnews/streams",
        "中視新聞 HD": "https://www.youtube.com/@twctvnews/streams",
        "華視新聞": "https://www.youtube.com/@CtsTw/streams",
        "民視新聞網": "https://www.youtube.com/@FTV_News/streams",
        "公視": "https://www.youtube.com/@ptslivestream/streams",
        "公視新聞網": "https://www.youtube.com/@PNNPTS/streams",
        "公視台語台": "https://www.youtube.com/@ptstaigitai/streams",
        "TaiwanPlus": "https://www.youtube.com/@TaiwanPlusLive/streams",		
        "大愛電視": "https://www.youtube.com/@DaAiVideo/streams",
        "鏡新聞": "https://www.youtube.com/@mnews-tw/streams",
        "東森新聞": "https://www.youtube.com/@newsebc/streams",	
        "三立iNEWS": "https://www.youtube.com/@setinews/streams",
        "三立LIVE新聞": "https://www.youtube.com/@setnews/streams",
        "中天新聞CtiNews": "https://www.youtube.com/@中天新聞CtiNews/streams",
        "中天電視CtiTv": "https://www.youtube.com/@中天電視CtiTv/streams",
        "TVBS NEWS": "https://www.youtube.com/@TVBSNEWS01/streams",
        "寰宇新聞": "https://www.youtube.com/@globalnewstw/streams",
        "新唐人亞太電視台": "https://www.youtube.com/@NTDAPTV/streams",
        "非凡電視": "https://www.youtube.com/@ustv/streams",
        "鳳凰衛視PhoenixTV": "https://www.youtube.com/@phoenixtvhk/streams",
        "CCTV中文": "https://www.youtube.com/@LiveNow24H/streams"
    },
    "綜藝,#genre#": {
        "MIT台灣誌": "https://www.youtube.com/@ctvmit/streams",
        "八大娛樂百分百": "https://www.youtube.com/@GTV100ENTERTAINMENT/streams",
        "中視經典綜藝": "https://www.youtube.com/@ctvent_classic/streams",
        "木曜4超玩": "https://www.youtube.com/@Muyao4/streams",	
        "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams",
        "現在宅知道": "https://www.youtube.com/@cbotaku/streams"
    },
    "影劇,#genre#": {	
        "戲說台灣": "https://www.youtube.com/@TWStoryTV/streams",	
        "大愛劇場": "https://www.youtube.com/@DaAiDrama/streams",	
        "中視經典戲劇": "https://www.youtube.com/@ctvdrama_classic/streams",
        "甄嬛傳全集": "https://www.youtube.com/@LegendofConcubineZhenHuan/streams"
    },
    "少兒,#genre#": {
        "YOYOTV": "https://www.youtube.com/@yoyotvebc/streams",
        "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
        "Ani-One中文官方動畫頻道": "https://www.youtube.com/@AniOneAnime/streams"
    },
    "體育,#genre#": {
        "愛爾達體育家族": "https://www.youtube.com/@ELTASPORTSHD/streams",
        "緯來體育台": "https://www.youtube.com/@vlsports/streams",
        "WWE": "https://www.youtube.com/@WWE/streams"
    },
    "風景,#genre#": {
        "台北觀光即時影像": "https://www.youtube.com/@taipeitravelofficial/streams",
        "陽明山國家公園": "https://www.youtube.com/@ymsnpinfo/streams",
        "阿里山國家風景區": "https://www.youtube.com/@Alishannsa/streams"
    }
}

def clean_title(text, nickname, max_length=40):
    """標題處理邏輯"""
    # 移除逗號避免格式錯誤
    text = text.replace(',', ' ').strip()
    
    # 判斷是否包含英文（拉丁字母）
    has_eng = bool(re.search(r'[a-zA-Z]{3,}', text))
    
    # 如果沒英文，優先使用我們定義的中文暱稱
    if not has_eng:
        display_title = nickname
    else:
        display_title = text

    # 長度截斷處理
    if len(display_title) > max_length:
        return display_title[:max_length] + "..."
    return display_title

def get_live_info():
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-10', # 搜尋範圍擴大，確保抓到所有直播
        'ignoreerrors': True,
        'no_warnings': True,
    }
    
    final_output = []
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for genre, channels in CATEGORIES.items():
            genre_buffer = []
            processed_urls = set() # 防止同頻道重複抓取相同網址
            print(f"正在檢查分類: {genre}")
            
            for nickname, url in channels.items():
                try:
                    info = ydl.extract_info(url, download=False)
                    if not info: continue
                    
                    entries = info.get('entries', [])
                    # 若直接給直播網址而非頻道網址，處理單一 entry
                    if not entries and info.get('live_status') == 'is_live':
                        entries = [info]

                    for entry in entries:
                        if not entry: continue
                        # 判定是否為直播
                        if entry.get('live_status') == 'is_live' or entry.get('is_live') is True:
                            v_id = entry.get('id')
                            v_url = f"https://www.youtube.com/watch?v={v_id}"
                            
                            if v_id and v_url not in processed_urls:
                                v_raw_title = entry.get('title', '')
                                # 呼叫清理標題函式
                                final_title = clean_title(v_raw_title, nickname)
                                
                                genre_buffer.append(f"{final_title},{v_url}")
                                processed_urls.add(v_url)
                                print(f"  [OK] 找到: {final_title}")
                except Exception as e:
                    continue
            
            # 分類區塊寫入
            if genre_buffer:
                final_output.append(genre)
                final_output.extend(genre_buffer)
                final_output.append("") # 類別結束後的空行
                
    return final_output

def main():
    results = get_live_info()
    with open("live_list.txt", "w", encoding="utf-8") as f:
        # 清除結尾多餘空白並寫入檔案
        content = "\n".join(results).strip()
        f.write(content + "\n")
    print(f"\n任務結束！已產出完整直播清單至 live_list.txt")

if __name__ == "__main__":
    main()
