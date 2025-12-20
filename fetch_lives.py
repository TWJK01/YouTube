import yt_dlp

# 頻道清單
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
        "中天亞洲台": "https://www.youtube.com/@中天亞洲台CtiAsia/streams",
        "CTI+ | 中天2台": "https://www.youtube.com/@中天2台ctiplusnews/streams",	
        "TVBS NEWS": "https://www.youtube.com/@TVBSNEWS01/streams",
        "Focus全球新聞": "https://www.youtube.com/@tvbsfocus/streams",	
        "寰宇新聞": "https://www.youtube.com/@globalnewstw/streams",
        "udn video": "https://www.youtube.com/@udn-video/streams",
        "CNEWS匯流新聞網": "https://www.youtube.com/@CNEWS/streams",	
        "新唐人亞太電視台": "https://www.youtube.com/@NTDAPTV/streams",
        "八大民生新聞": "https://www.youtube.com/@gtvnews27/streams",		
        "原視新聞網 TITV News": "https://www.youtube.com/@TITVNews16/streams",
        "飛碟聯播網": "https://www.youtube.com/@921ufonetwork/streams",		
        "三大一台": "https://www.youtube.com/@SDTV55ch/streams",	
        "中天財經頻道": "https://www.youtube.com/@中天財經頻道CtiFinance/streams",	
        "東森財經股市": "https://www.youtube.com/@57ETFN/streams",	
        "寰宇財經新聞": "https://www.youtube.com/@globalmoneytv/streams",
        "非凡電視": "https://www.youtube.com/@ustv/streams",
        "非凡商業台": "https://www.youtube.com/@ustvbiz/streams",	
        "運通財經台": "https://www.youtube.com/@EFTV01/streams",
        "全球財經台2": "https://www.youtube.com/@全球財經台2/streams",	
        "AI主播倪珍Nikki 播新聞": "https://www.youtube.com/@NOWnews-sp2di/streams",
        "BNE TV - 新西兰中文国际频道": "https://www.youtube.com/@BNETVNZ/streams",	
        "POP Radio聯播網": "https://www.youtube.com/@917POPRadio/streams",
        "Eight FM": "https://www.youtube.com/@eight-audio/streams",	
        "鳳凰衛視PhoenixTV": "https://www.youtube.com/@phoenixtvhk/streams",
        "鳳凰資訊 PhoenixTVNews": "https://www.youtube.com/@phoenixtvnews7060/streams",
        "HOY 資訊台 × 有線新聞": "https://www.youtube.com/@HOYTVHK/streams",		
        "CCTV中文": "https://www.youtube.com/@LiveNow24H/streams",
        "8world": "https://www.youtube.com/@8worldSG/streams"
    },
    "綜藝,#genre#": {
        "MIT台灣誌": "https://www.youtube.com/@ctvmit/streams",
        "大陸尋奇": "https://www.youtube.com/@ctvchinatv/streams",	
        "八大電視娛樂百分百": "https://www.youtube.com/@GTV100ENTERTAINMENT/streams",
        "三立娛樂星聞": "https://www.youtube.com/@star_setn/streams",	
        "中視經典綜藝": "https://www.youtube.com/@ctvent_classic/streams",
        "綜藝一級棒": "https://www.youtube.com/@NO1TVSHOW/streams",
        "小姐不熙娣": "https://www.youtube.com/@deegirlstalk/streams",
        "民視 超級冰冰Show": "https://www.youtube.com/@superbingbingshow/streams",
        "民視綜藝娛樂": "https://www.youtube.com/@FTV_Show/streams",			
        "木曜4超玩": "https://www.youtube.com/@Muyao4/streams",	
        "華視綜藝頻道": "https://www.youtube.com/@CTSSHOW/streams",
        "綜藝大熱門": "https://www.youtube.com/@HotDoorNight/streams",
        "綜藝玩很大": "https://www.youtube.com/@Mr.Player/streams",	
        "11點熱吵店": "https://www.youtube.com/@chopchopshow/streams",
        "飢餓遊戲": "https://www.youtube.com/@HungerGames123/streams",	
        "豬哥會社": "https://www.youtube.com/@FTV_ZhuGeClub/streams",
        "百變智多星": "https://www.youtube.com/@百變智多星/streams",	
        "東森綜合台": "https://www.youtube.com/@ettv32/streams",
        "中天娛樂頻道": "https://www.youtube.com/@ctitalkshow/streams",		
        "57怪奇物語": "https://www.youtube.com/@57StrangerThings/streams",
        "命運好好玩": "https://www.youtube.com/@eravideo004/streams",	
        "TVBS娛樂頭條": "https://www.youtube.com/@tvbsenews/streams",	
        "台灣啟示錄": "https://www.youtube.com/@ebcapocalypse/streams",
        "緯來日本台": "https://www.youtube.com/@VideolandJapan/streams",
        "我愛小明星大跟班": "https://www.youtube.com/@我愛小明星大跟班/streams",
        "明星下班路": "https://www.youtube.com/@gtvstaroad/streams",		
        "204檔案": "https://www.youtube.com/@204/streams",
        "WTO姐妹會": "https://www.youtube.com/@WTOSS/streams",	
        "好看娛樂": "https://www.youtube.com/@好看娛樂/streams",
        "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/streams",	
        "TVBS女人我最大": "https://www.youtube.com/@tvbsqueen/streams",
        "型男大主廚": "https://www.youtube.com/@twcookingshow/streams",	
        "非凡大探索": "https://www.youtube.com/@ustvfoody/streams",
        "你好星期六": "https://www.youtube.com/@HelloSaturdayOfficial/streams",	
        "BIF相信未來": "https://www.youtube.com/@BelieveinfutureTV/streams",
        "GTV 自由的旅行者": "https://www.youtube.com/@gtvfreedomtravelers/streams",
        "原視 TITV+": "https://www.youtube.com/@titv8932/streams",
        "寶島神很大": "https://www.youtube.com/@godBlessBaodao/streams",
        "Taste The World": "https://www.youtube.com/@TasteTheWorld66/streams",
        "現在宅知道": "https://www.youtube.com/@cbotaku/streams",
        "娱综星天地": "https://www.youtube.com/@娱综星天地/streams",
        "靖天電視台": "https://www.youtube.com/@goldentvdrama/streams",
        "靈異錯別字": "https://www.youtube.com/@靈異錯別字ctiwugei/streams",
        "下面一位": "https://www.youtube.com/@ytnextone_1/streams",		
        "公共電視-我們的島": "https://www.youtube.com/@ourislandTAIWAN/streams",
        "WeTV 綜藝經典": "https://www.youtube.com/@WeTV-ClassicVariety/streams",
        "爆梗TV": "https://www.youtube.com/@爆梗PunchlineTV/streams",
        "灿星官方频道": "https://www.youtube.com/@CanxingMediaOfficialChannel/streams",
        "陕西廣播電視台": "https://www.youtube.com/@chinashaanxitvofficialchan2836/streams",		
        "北京廣播電視台": "https://www.youtube.com/@btvfinance/streams"		
    },
    "影劇,#genre#": {	
        "戲說台灣": "https://www.youtube.com/@TWStoryTV/streams",	
        "CCTV纪录": "https://www.youtube.com/@CCTVDocumentary/streams",
        "大愛劇場": "https://www.youtube.com/@DaAiDrama/streams",	
        "台視時光機": "https://www.youtube.com/@TTVClassic/streams",
        "中視經典戲劇": "https://www.youtube.com/@ctvdrama_classic/streams",
        "華視戲劇頻道": "https://www.youtube.com/@cts_drama/streams",
        "民視戲劇館": "https://www.youtube.com/@FTVDRAMA/streams",
        "四季線上4gTV": "https://www.youtube.com/@4gTV_online/streams",	
        "三立電視 SET TV": "https://www.youtube.com/@SETTV/streams",
        "三立華劇": "https://www.youtube.com/@SETdrama/streams",
        "三立台劇": "https://www.youtube.com/@setdramatw/streams",	
        "終極系列": "https://www.youtube.com/@KOONERETURN/streams",
        "TVBS劇在一起": "https://www.youtube.com/@tvbsdrama/streams",
        "TVBS戲劇-女兵日記": "https://www.youtube.com/@tvbs-1587/streams",	
        "八大劇樂部": "https://www.youtube.com/@gtv-drama/streams",
        "GTV DRAMA": "https://www.youtube.com/@gtvdramaenglish/streams",
        "萌萌愛追劇": "https://www.youtube.com/@mengmengaizhuijuminidrama/streams",	
        "龍華電視": "https://www.youtube.com/@ltv_tw/streams",
        "Vidol TV": "https://www.youtube.com/@vidoltv/streams",		
        "緯來戲劇台": "https://www.youtube.com/@Vldrama43/streams",
        "緯來育樂台": "https://www.youtube.com/@maxtv71/streams",		
        "愛爾達綜合台": "https://www.youtube.com/@ELTAWORLD/streams",
        "愛爾達影劇台": "https://www.youtube.com/@eltadrama/streams",
        "VBL Series": "https://www.youtube.com/@variety_between_love/streams",
        "甄嬛传全集": "https://www.youtube.com/@LegendofConcubineZhenHuan/streams",		
        "精选大剧": "https://www.youtube.com/@精选大剧/streams",		
        "百纳經典劇": "https://www.youtube.com/@BainationTVSeriesOfficial/streams",
        "华录百納熱播劇場": "https://www.youtube.com/@Baination/streams",	
        "iQIYI 愛奇藝": "https://www.youtube.com/@iQIYIofficial/streams",
        "爱奇艺大电影": "https://www.youtube.com/@iQIYIMOVIETHEATER/streams",
        "芒果TV青春剧场": "https://www.youtube.com/@MangoTVDramaOfficial/streams",	
        "CCTV电视剧": "https://www.youtube.com/@CCTVDrama/streams",	
        "SMG上海電視台": "https://www.youtube.com/@SMG-Official/streams",
        "SMG電視劇": "https://www.youtube.com/@SMGDrama/streams",
        "正午陽光": "https://www.youtube.com/@DaylightEntertainmentDrama/streams",		
        "超級影迷電影": "https://www.youtube.com/@MegaFilmLovers/streams",
        "MadHouse 免費電影": "https://www.youtube.com/@MadHouseFreeMovie/streams"
    },
    "少兒,#genre#": {
        "YOYOTV": "https://www.youtube.com/@yoyotvebc/streams",
        "momokids親子台": "https://www.youtube.com/@momokidsYT/streams",
        "Bebefinn 兒歌": "https://www.youtube.com/@Bebefinn繁體中文/streams",
        "寶貝多米": "https://www.youtube.com/@Domikids_CN/streams",
        "瑪莎與熊": "https://www.youtube.com/@MashaBearTAIWAN/streams",	
        "碰碰狐 鯊魚寶寶": "https://www.youtube.com/@Pinkfong繁體中文/streams",
        "寶寶巴士": "https://www.youtube.com/@BabyBusTC/streams",
        "小猪佩奇": "https://www.youtube.com/@PeppaPigChineseOfficial/streams",
        "Muse木棉花-TW": "https://www.youtube.com/@MuseTW/streams",	
        "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
        "Ani-One中文動畫": "https://www.youtube.com/@AniOneAnime/streams",
        "嗶哩嗶哩動畫": "https://www.youtube.com/@MadeByBilibili/streams"
    },
    "體育,#genre#": {
        "愛爾達體育家族": "https://www.youtube.com/@ELTASPORTSHD/streams",
        "緯來體育台": "https://www.youtube.com/@vlsports/streams",
        "公視體育": "https://www.youtube.com/@pts_sports/streams",
        "智林體育台": "https://www.youtube.com/@oursport_tv1/streams",
        "博斯體育台": "https://www.youtube.com/@Sportcasttw/streams",	
        "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
        "DAZN 台灣": "https://www.youtube.com/@DAZNTaiwan/streams",	
        "P.LEAGUE+": "https://www.youtube.com/@PLEAGUEofficial/streams",
        "TPBL": "https://www.youtube.com/@TPBL.Basketball/streams",		
        "CPBL 中華職棒": "https://www.youtube.com/@CPBL/streams",
        "WWE": "https://www.youtube.com/@WWE/streams"
    },
    "音樂,#genre#": {
        "Eight FM": "https://www.youtube.com/@eight-audio/streams",
        "Sony Music HK": "https://www.youtube.com/@sonymusichk/streams",		
        "Douyin Chill": "https://www.youtube.com/@DouyinChill-xr2yk/streams",
        "抖音音樂台": "https://www.youtube.com/@douyinyinyuetai/streams",
        "Radio Hits Music": "https://www.youtube.com/@LiveMusicRadio/streams"		
    },
    "政論,#genre#": {
        "壹電視NEXT TV": "https://www.youtube.com/@壹電視NEXTTV/streams",
        "庶民大頭家": "https://www.youtube.com/@庶民大頭家/streams",
        "TVBS 優選頻道": "https://www.youtube.com/@tvbschannel/streams",
        "全球大視野": "https://www.youtube.com/@全球大視野Global_Vision/streams",
        "民視讚夯": "https://www.youtube.com/@FTV_Forum/streams",
        "新聞大白話": "https://www.youtube.com/@tvbstalk/streams",
        "關鍵時刻": "https://www.youtube.com/@ebcCTime/streams",
        "少康戰情室": "https://www.youtube.com/@tvbssituationroom/streams",
        "萬事通事務所": "https://www.youtube.com/@sciencewillwin/streams"
    },
    "購物,#genre#": {
        "momo購物一台": "https://www.youtube.com/@momoch4812/streams",
        "momo購物二台": "https://www.youtube.com/@momoch3571/streams",
        "ViVa TV美好家庭購物": "https://www.youtube.com/@ViVaTVtw/streams",
        "Live東森購物台": "https://www.youtube.com/@HotsaleTV/streams"		
    },
    "國會,#genre#": {
        "國會頻道": "https://www.youtube.com/@parliamentarytv/streams"
    },	
    "風景,#genre#": {
        "台北觀光即時影像": "https://www.youtube.com/@taipeitravelofficial/streams",
        "陽明山國家公園": "https://www.youtube.com/@ymsnpinfo/streams",
        "新北旅客": "https://www.youtube.com/@ntctour/streams",
        "遊桃園 Taoyuan Travel": "https://www.youtube.com/@TaoyuanTravel/streams",
        "阿里山國家風景區": "https://www.youtube.com/@Alishannsa/streams",
        "高雄旅遊網": "https://www.youtube.com/@travelkhh/streams",
        "樂遊金門": "https://www.youtube.com/@kinmentravel/streams"
    }
}

def get_live_info():
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-3',
        'ignoreerrors': True,
        'no_warnings': True,
        'extra_headers': {'Accept-Language': 'zh-TW'}
    }
    
    final_lines = []
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for genre_title, channels in CATEGORIES.items():
            genre_buffer = []
            print(f">>> 掃描分類: {genre_title}")
            
            for display_name, url in channels.items():
                try:
                    # 強制處理特殊頻道或一般頻道
                    target_url = url
                    if "Muse_Family" in url:
                        target_url = "https://www.youtube.com/@Muse_Family/live"
                    
                    info = ydl.extract_info(target_url, download=False)
                    if not info: continue
                    
                    entries = info.get('entries', [info])
                    for entry in entries:
                        if not entry: continue
                        if entry.get('live_status') == 'is_live' or entry.get('is_live') is True:
                            # 關鍵修正：標題取我們定義的中文名稱，並移除名稱中的逗號
                            safe_name = display_name.replace(",", " ")
                            video_id = entry.get('id')
                            if video_id:
                                video_url = f"https://www.youtube.com/watch?v={video_id}"
                                genre_buffer.append(f"{safe_name},{video_url}")
                                print(f"  [找到] {safe_name}")
                                break # 每個頻道通常只取一個直播，避免重複
                except:
                    continue
            
            if genre_buffer:
                final_lines.append(genre_title)
                final_lines.extend(genre_buffer)
                final_lines.append("") # 分類結束後插入一個空行
                
    return final_lines

def main():
    output_data = get_live_info()
    with open("live_list.txt", "w", encoding="utf-8") as f:
        # 去掉最後一個多餘的空行並寫入
        f.write("\n".join(output_data).strip() + "\n")
    print(f"\n[完成] 檔案 live_list.txt 已產生。")

if __name__ == "__main__":
    main()
