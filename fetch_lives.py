import yt_dlp
import re

# 1. 自動抓取的頻道清單
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
        "民視綜藝娛樂 Formosa TV Entertainments": "https://www.youtube.com/@FTV_Show/streams",			
        "木曜4超玩": "https://www.youtube.com/@Muyao4/streams",	
        "華視綜藝頻道": "https://www.youtube.com/@CTSSHOW/streams",
        "綜藝大熱門": "https://www.youtube.com/@HotDoorNight/streams",
        "綜藝玩很大": "https://www.youtube.com/@Mr.Player/streams",	
        "11點熱吵店": "https://www.youtube.com/@chopchopshow/streams",
        "飢餓遊戲": "https://www.youtube.com/@HungerGames123/streams",	
        "豬哥會社": "https://www.youtube.com/@FTV_ZhuGeClub/streams",
        "百變智多星": "https://www.youtube.com/@百變智多星/streams",	
        "東森綜合台": "https://www.youtube.com/@中天娛樂CtiEntertainment/streams",
        "中天娛樂頻道": "https://www.youtube.com/@ettv32/streams",		
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
        "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/videos",	
        "TVBS女人我最大": "https://www.youtube.com/@tvbsqueen/streams",
        "型男大主廚": "https://www.youtube.com/@twcookingshow/streams",	
        "非凡大探索": "https://www.youtube.com/@ustvfoody/streams",
        "你好, 星期六 Hello Saturday Official": "https://www.youtube.com/@HelloSaturdayOfficial/streams",	
        "BIF相信未來 官方頻道": "https://www.youtube.com/@BelieveinfutureTV/streams",
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
        "陕西广播电视台官方频道": "https://www.youtube.com/@chinashaanxitvofficialchan2836/streams",		
        "北京廣播電視台生活頻道": "https://www.youtube.com/@btvfinance/streams"		
        
    },
    "影劇,#genre#": {	
        "戲說台灣": "https://www.youtube.com/@TWStoryTV/streams",	
	    "CCTV纪录": "https://www.youtube.com/@CCTVDocumentary/streams",
	    "大愛劇場 DaAiDrama": "https://www.youtube.com/@DaAiDrama/streams",	
        "台視時光機": "https://www.youtube.com/@TTVClassic/streams",
        "中視經典戲劇": "https://www.youtube.com/@ctvdrama_classic/streams",
        "華視戲劇頻道": "https://www.youtube.com/@cts_drama/streams",
        "民視戲劇館": "https://www.youtube.com/@FTVDRAMA/streams",
        "四季線上4gTV": "https://www.youtube.com/@4gTV_online/streams",	
        "三立電視 SET TV": "https://www.youtube.com/@SETTV/streams",
        "三立華劇 SET Drama": "https://www.youtube.com/@SETdrama/streams",
        "三立台劇 SET Drama": "https://www.youtube.com/@setdramatw/streams",	
        "終極系列": "https://www.youtube.com/@KOONERETURN/streams",
        "TVBS劇在一起": "https://www.youtube.com/@tvbsdrama/streams",
        "TVBS戲劇-女兵日記 女力報到": "https://www.youtube.com/@tvbs-1587/streams",	
        "八大劇樂部": "https://www.youtube.com/@gtv-drama/streams",
        "GTV DRAMA English": "https://www.youtube.com/@gtvdramaenglish/streams",
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
        "百纳经典独播剧场": "https://www.youtube.com/@BainationTVSeriesOfficial/streams",
        "华录百納熱播劇場": "https://www.youtube.com/@Baination/streams",	
        "iQIYI 爱奇艺": "https://www.youtube.com/@iQIYIofficial/streams",
        "iQIYI Show Giải Trí Vietnam": "https://www.youtube.com/@iQIYI_ShowGiảiTríVietnam/streams",		
        "iQIYI Indonesia": "https://www.youtube.com/@iQIYIIndonesia/streams",
        "爱奇艺大电影": "https://www.youtube.com/@iQIYIMOVIETHEATER/streams",
        "iQIYI 慢綜藝": "https://www.youtube.com/@iQIYILifeShow/streams",		
        "iQIYI 潮綜藝": "https://www.youtube.com/@iQIYISuperShow/streams",
        "iQIYI 爆笑宇宙": "https://www.youtube.com/@iQIYIHappyWorld/streams",		
        "MangoTV Shorts": "https://www.youtube.com/@MangoTVShorts/streams",
        "MangoTV English": "https://www.youtube.com/@MangoTVEnglishOfficial/streams",
        "MangoTV Malaysia": "https://www.youtube.com/@MangoTVMalaysia/streams",		
        "芒果TV古裝劇場": "https://www.youtube.com/@TVMangoTVCostume-yw1hj/streams",	
        "芒果TV青春剧场": "https://www.youtube.com/@MangoTVDramaOfficial/streams",	
        "芒果TV季风频道": "https://www.youtube.com/@MangoMonsoon/streams",	
        "芒果TV推理宇宙": "https://www.youtube.com/@MangoTV-Mystery/streams",
        "芒果TV大電影劇場": "https://www.youtube.com/@MangoC-TheatreChannel/streams",
        "芒果TV心动": "https://www.youtube.com/@MangoTVSparkle/streams",	
        "CCTV电视剧": "https://www.youtube.com/@CCTVDrama/streams",	
        "SMG上海电视台官方频道": "https://www.youtube.com/@SMG-Official/streams",
        "SMG上海东方卫视欢乐频道": "https://www.youtube.com/@SMG-Comedy/streams",
        "SMG电视剧": "https://www.youtube.com/@SMGDrama/streams",
        "老广一起睇": "https://www.youtube.com/@老广一起睇/streams",		
        "安徽衛視官方頻道": "https://www.youtube.com/@chinaanhuitvofficialchanne8354/streams",	
        "中国东方卫视官方频道": "https://www.youtube.com/@SMGDragonTV/streams",
        "北京广播电视台官方频道": "https://www.youtube.com/@Brtvofficialchannel/streams",
        "陕西广播电视台官方频道": "https://www.youtube.com/@chinashaanxitvofficialchan2836/streams",
        "贵州卫视官方频道": "https://www.youtube.com/@gztvofficial/streams",
        "喜剧大联盟": "https://www.youtube.com/@SuperComedyLeague/streams",
        "China Zone 古裝劇場": "https://www.youtube.com/@ChinaZoneCostume/streams",
        "China Zone 剧乐部": "https://www.youtube.com/@ChinaZoneDrama/streams",
        "China Zone 流金岁月": "https://www.youtube.com/@ChinaZone-ClassicDrama/streams",
        "China Zone梦想剧场": "https://www.youtube.com/@ChinaZone-DreamDrama/streams",		
        "欢娱影视官方频道": "https://www.youtube.com/@chinahuanyuent.officialchannel/streams",		
        "正午阳光官方频道": "https://www.youtube.com/@DaylightEntertainmentDrama/streams",		
        "超級影迷 正版電影免費看": "https://www.youtube.com/@MegaFilmLovers/streams",
        "電影想飛 正版電影免費看": "https://www.youtube.com/@moviesintheair/streams",
        "MadHouse 免費電影": "https://www.youtube.com/@MadHouseFreeMovie/streams",
        "FAST 免費電影": "https://www.youtube.com/@FASTMOVIE168/streams",		
        "SMG音乐频道": "https://www.youtube.com/@SMGMusic/streams"				
    },
    "少兒,#genre#": {
        "YOYOTV": "https://www.youtube.com/@yoyotvebc/streams",
        "momokids親子台": "https://www.youtube.com/@momokidsYT/streams",
        "Bebefinn 繁體中文 - 兒歌": "https://www.youtube.com/@Bebefinn繁體中文/streams",
        "寶貝多米-兒歌童謠-卡通動畫-經典故事": "https://www.youtube.com/@Domikids_CN/streams",
        "會說話的湯姆貓家族": "https://www.youtube.com/@TalkingFriendsCN/streams",
        "瑪莎與熊": "https://www.youtube.com/@MashaBearTAIWAN/streams",	
        "碰碰狐 鯊魚寶寶": "https://www.youtube.com/@Pinkfong繁體中文/streams",
        "碰碰狐 Pinkfong Baby Shark 儿歌·故事": "https://www.youtube.com/@Pinkfong简体中文/streams",	
        "寶寶巴士": "https://www.youtube.com/@BabyBusTC/streams",
        "Miliki Family - 繁體中文 - 兒歌": "https://www.youtube.com/@MilikiFamily_Chinese/streams",	
        "貝樂虎-幼兒動畫-早教启蒙": "https://www.youtube.com/@BarryTiger_Education_CN/streams",	
        "貝樂虎兒歌-童謠歌曲": "https://www.youtube.com/@barrytiger_kidssongs/streams",
        "貝樂虎-兒歌童謠-卡通動畫-經典故事": "https://www.youtube.com/@barrytiger_zh/streams",
        "小猪佩奇": "https://www.youtube.com/@PeppaPigChineseOfficial/streams",
        "Kids Songs - Giligilis": "https://www.youtube.com/@KidsSongs6868/streams",
        "超級汽車-卡通動畫": "https://www.youtube.com/@Supercar_Cartoon/streams",	
        "神奇鸡仔": "https://www.youtube.com/@como_cn/streams",
        "朱妮托尼 - 动画儿歌": "https://www.youtube.com/@JunyTonyCN/streams",	
        "會說話的湯姆貓家族": "https://www.youtube.com/@TalkingFriendsCN/streams",
        "Muse木棉花-TW": "https://www.youtube.com/@MuseTW/streams",	
        "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
        "Ani-One中文官方動畫頻道": "https://www.youtube.com/@AniOneAnime/streams",
        "Lv.99 Animation Club": "https://www.youtube.com/@Lv.99AnimationClub/streams",
        "嘀嘀漫畫站": "https://www.youtube.com/@嘀嘀漫畫站DidiComic/streams",			
        "嗶哩嗶哩動畫Anime Made By Bilibili": "https://www.youtube.com/@MadeByBilibili/streams",	
        "回歸線娛樂": "https://www.youtube.com/@tropicsanime/streams",
        "愛奇藝國漫": "https://www.youtube.com/@iQIYIAnimation/streams",	
        "超人官方 YouTube 粵語頻道": "https://www.youtube.com/@ultraman_cantonese_official/streams"				
    },
    "體育,#genre#": {
        "愛爾達體育家族": "https://www.youtube.com/@ELTASPORTSHD/streams",
        "緯來體育台": "https://www.youtube.com/@vlsports/streams",
	    "公視體育": "https://www.youtube.com/@pts_sports/streams",
	    "getwin_sport": "https://www.youtube.com/@GetWinSport/streams",		
        "庫泊運動賽事": "https://www.youtube.com/@coopersport-live/streams",	
        "智林體育台": "https://www.youtube.com/@oursport_tv1/streams",
        "博斯體育台": "https://www.youtube.com/@Sportcasttw/streams",	
        "HOP Sports": "https://www.youtube.com/@HOPSports/streams",
        "DAZN 台灣": "https://www.youtube.com/@DAZNTaiwan/streams",	
        "動滋Sports": "https://www.youtube.com/@Sport_sa_taiwan/streams",
        "GoHoops": "https://www.youtube.com/@GoHoops/streams",
        "P.LEAGUE+": "https://www.youtube.com/@PLEAGUEofficial/streams",
        "TPBL": "https://www.youtube.com/@TPBL.Basketball/streams",		
        "CPBL 中華職棒": "https://www.youtube.com/@CPBL/streams",
        "Body Sports  名衍行銷運動頻道": "https://www.youtube.com/@bodysports9644/streams",		
        "日本B聯盟": "https://www.youtube.com/@b.leagueinternational/streams",
        "MotoGP": "https://www.youtube.com/@motogp/streams",
        "The Savannah Bananas": "https://www.youtube.com/@TheSavannahBananas/streams",
        "WCW": "https://www.youtube.com/@WCW/streams",		
        "BattleBots": "https://www.youtube.com/@BattleBots/streams",
        "WWE": "https://www.youtube.com/@WWE/streams",
	    "WWE Vault": "https://www.youtube.com/@WWEVault/streams"   
    },
	"音樂,#genre#": {
	    "Eight FM 线上收听！": "https://www.youtube.com/@eight-audio/streams",
	    "Sony Music Entertainment Hong Kong": "https://www.youtube.com/@sonymusichk/streams",		
	    "Hot TV": "https://www.youtube.com/@hotfm976/streams",		
	    "KKBOX 华语新歌周榜": "https://www.youtube.com/@KKBOX-baidu6868/streams",
	    "Douyin Chill": "https://www.youtube.com/@DouyinChill-xr2yk/streams",
	    "生活乐章": "https://www.youtube.com/@生活乐章/streams",	    
	    "抖音音樂台": "https://www.youtube.com/@douyinyinyuetai/streams",
	    "青春音乐铺": "https://www.youtube.com/@青春音乐铺/streams",
	    "水月琴音": "https://www.youtube.com/@Shuiyueqinyin/streams",	    
	    "Cherry 葵": "https://www.youtube.com/@Cherriexin/streams",
	    "CMIX - Chill Mix": "https://www.youtube.com/@ChillMix-CMIX/streams",		
	    "「KING AMUSEMENT CREATIVE」公式チャンネル": "https://www.youtube.com/@KAC_official/streams",
	    "FOR FUN RADIO TIME Music channel": "https://www.youtube.com/@FORFUNRADIOTIME-Relax/streams",		
	    "Mellowbeat Seeker": "https://www.youtube.com/@mellowbeatseeker/streams",
	    "The Good Life Radio x Sensual Musique": "https://www.youtube.com/@TheGoodLiferadio/streams",	
        "Best of Mix": "https://www.youtube.com/@bestofmixlive/streams",
        "Rock FM": "https://www.youtube.com/@rockfm1/streams",
        "Radio Mix": "https://www.youtube.com/@liveradiomix/streams",		
	    "Radio Hits Music": "https://www.youtube.com/@LiveMusicRadio/streams"		
    },	
    "政論,#genre#": {
        "壹電視NEXT TV": "https://www.youtube.com/@壹電視NEXTTV/streams",
        "庶民大頭家": "https://www.youtube.com/@庶民大頭家/streams",
        "TVBS 優選頻道": "https://www.youtube.com/@tvbschannel/streams",
        "街頭麥克風": "https://www.youtube.com/@street-mic/streams",
        "全球大視野": "https://www.youtube.com/@全球大視野Global_Vision/streams",
        "鄉民監察院": "https://www.youtube.com/@FTControlYuan/streams",		
        "民視讚夯": "https://www.youtube.com/@FTV_Forum/streams",
        "新台派上線": "https://www.youtube.com/@NewTaiwanonline/streams",	
        "94要客訴": "https://www.youtube.com/@94politics/streams",	
        "大新聞大爆卦": "https://www.youtube.com/@大新聞大爆卦HotNewsTalk/streams",	
        "新聞大白話": "https://www.youtube.com/@tvbstalk/streams",
        "國民大會": "https://www.youtube.com/@tvbscitizenclub/streams",	
        "中時新聞網": "https://www.youtube.com/@ChinaTimes/streams",
        "中天深喉嚨": "https://www.youtube.com/@ctitalkshow/streams",		
        "新聞挖挖哇！": "https://www.youtube.com/@newswawawa/streams",	
        "前進新台灣": "https://www.youtube.com/@SETTaiwanGo/streams",
        "哏傳媒": "https://www.youtube.com/@funseeTW/streams",	
        "57爆新聞": "https://www.youtube.com/@57BreakingNews/streams",
        "關鍵時刻": "https://www.youtube.com/@ebcCTime/streams",
        "新聞龍捲風": "https://www.youtube.com/@新聞龍捲風NewsTornado/streams",		
        "頭條開講": "https://www.youtube.com/@頭條開講HeadlinesTalk/streams",		
	    "少康戰情室": "https://www.youtube.com/@tvbssituationroom/streams",
        "文茜的世界周報": "https://www.youtube.com/@tvbssisysworldnews/streams",
        "萬事通事務所": "https://www.youtube.com/@sciencewillwin/streams",		
        "中天深喉嚨": "https://www.youtube.com/@ctitalkshow/streams",
        "品觀點": "https://www.youtube.com/@pinviewmedia/streams",
        "52新聞聚樂部 ": "https://www.youtube.com/@52newsclub/streams",		
        "觀點": "https://www.youtube.com/@%E8%A7%80%E9%BB%9E/streams",		
        "金臨天下": "https://www.youtube.com/@tvbsmoney/streams"		
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
        "和平島公園即時影像": "https://www.youtube.com/@和平島公園即時影像/streams",
		"台北觀光即時影像": "https://www.youtube.com/@taipeitravelofficial/streams",
		"陽明山國家公園": "https://www.youtube.com/@ymsnpinfo/streams",
		"大新店有線電視": "https://www.youtube.com/@CGNEWS8888/streams",
		"新北旅客 New Taipei Tour": "https://www.youtube.com/@ntctour/streams",
		"紅樹林有線電視": "https://www.youtube.com/@紅樹林有線電視-h7k/streams",
		"necoast nsa": "https://www.youtube.com/@necoastnsa2903/streams",
		"野柳即時影像": "https://www.youtube.com/@野柳即時影像/streams",
		"遊桃園 Taoyuan Travel": "https://www.youtube.com/@TaoyuanTravel/streams",
		"雪霸國家公園 Shei-Pa National Park": "https://www.youtube.com/@spnp852/streams",
		"交通部觀光署-參山風管處": "https://www.youtube.com/@trimtnsa/streams",
		"大玩台中-臺中觀光旅遊局": "https://www.youtube.com/@大玩台中-臺中觀光旅/streams",
		"台灣即時影像監視器": "https://www.youtube.com/@twipcam/streams",
		"Amos YANG": "https://www.youtube.com/@feng52/streams",
		"國家森林遊樂區即時影像": "https://www.youtube.com/@fancarecreation/streams",
		"阿里山國家風景區管理處": "https://www.youtube.com/@Alishannsa/streams",
		"大台南新聞": "https://www.youtube.com/@大台南新聞南天地方新/streams",
		"內政部國家公園署台江國家公園管理處": "https://www.youtube.com/@taijiangnationalpark/streams",
		"高雄旅遊網": "https://www.youtube.com/@travelkhh/streams",
		"茂林國家風景區": "https://www.youtube.com/@茂林國家風景區/streams",
		"南喃夕語": "https://www.youtube.com/@thesouth.2022/streams",
		"ktnpworld": "https://www.youtube.com/@ktnpworld/streams",
		"斯爾本科技有限公司": "https://www.youtube.com/@Suburban-Security/streams",
		"花蓮縣政府觀光處七星潭風景區": "https://www.youtube.com/@花蓮縣政府觀光處七星/streams",
		"東部海岸國家風景管理處": "https://www.youtube.com/@eastcoastnsa0501/streams",
		"Amazing Taitung 台東就醬玩": "https://www.youtube.com/@taitungamazing7249/streams",
		"ervnsa": "https://www.youtube.com/@ervnsa/streams",
		"交通部觀光署澎湖國家風景區管理處": "https://www.youtube.com/@交通部觀光署澎湖國家/streams",		
		"樂遊金門": "https://www.youtube.com/@kinmentravel/streams",
		"馬祖國家風景區": "https://www.youtube.com/@matsunationalscenicarea9539/streams"		
    }
}

# 2. 手動新增連結 (您可以在此直接放入網址)
# 格式為: "分類名稱": ["標題,網址", "標題,網址"]
MANUAL_LINKS = {
    "少兒,#genre#": [
        "【Muse木棉花】魔都精兵的奴隸,https://www.youtube.com/live/qXD7NKZlLPA?si=zyVpCoX7dpqsJNWn",
        "【Muse木棉花】間諜家家酒,https://www.youtube.com/watch?v=dI2negE-v4c",
        "【Muse木棉花】進擊的巨人,https://www.youtube.com/watch?v=GlVvyu7jehk",
        "【Muse木棉花】關於我轉生變成史萊姆這檔事,https://www.youtube.com/watch?v=ATsYVyh_Nwk",		
        "【Muse木棉花】葬送的芙莉蓮,https://www.youtube.com/live/DAVfn4Sp8xw?si=ZEWt4HIP6KBuhaYr",
        "【Muse木棉花】蠟筆小新TV版,https://www.youtube.com/watch?v=ENnjj7jQ23g",
        "【Muse木棉花】新哆啦A夢,https://www.youtube.com/watch?v=jbZCyIhL4WQ",
        "【Muse木棉花】中華一番,https://www.youtube.com/watch?v=mRCXonM5ru8",
        "【Muse木棉花】我們這一家,https://www.youtube.com/watch?v=e1gbvCkwxFE"		

		
    ]
}

# 3. 地標翻譯對照表 (救援標題)
LANDMARK_MAP = {
    "Shoushan Lovers": "壽山情人觀景台", "Lianchihtan": "蓮池潭", "Lotus Pond": "蓮池潭",
    "Cijin": "旗津", "Baling": "巴陵大橋", "Shihmen Reservoir": "石門水庫",
    "Fenqihu": "奮起湖", "Eryanping": "二延平", "Taiping Suspension Bridge": "太平雲梯",
    "Sanxiantai": "三仙台", "Chaikou": "綠島柴口", "Shitiping": "石梯坪", "Jialulan": "加路蘭"
}

def extract_best_title(v_title, nickname):
    """
    智慧優化標題：處理國會名稱與風景地標。
    """
    # 國會處理
    if "國會頻道" in nickname:
        segments = re.split(r'[\|\-\—\–]', v_title)
        if len(segments) > 1:
            return f"【國會頻道】{segments[0].strip()}"
        return f"【國會頻道】{v_title.replace('立法院議事轉播', '').strip()}"

    # 風景品牌標準化
    if "高雄" in nickname or "Kaohsiung" in v_title: brand = "高雄旅遊網"
    elif "Taipei" in nickname or "台北" in v_title: brand = "Taipei Live Cam"
    elif "桃園" in nickname or "Taoyuan" in v_title: brand = "遊桃園"
    elif "新北" in nickname or "New Taipei" in v_title: brand = "新北旅客"
    elif "阿里山" in nickname or "Alishan" in v_title: brand = "阿里山"
    elif "東部海岸" in nickname or "East Coast" in v_title: brand = "東部海岸"
    else: brand = nickname

    # 地標提取
    clean_title = re.sub(r'[【\[\(].*?[】\]\)]', '', v_title).strip()
    segments = re.split(r'[\|\-\—\–]', clean_title)
    landmark = ""
    for seg in reversed(segments):
        chinese_found = "".join(re.findall(r'[\u4e00-\u9fa5]+', seg))
        noises = ["即時影像", "直播", "頻道", "官方", "高雄", "桃園", "台北", "新北", "觀光", "風景區", "管理處"]
        for n in noises:
            chinese_found = chinese_found.replace(n, "")
        if len(chinese_found) >= 2:
            landmark = chinese_found; break

    if len(landmark) < 2:
        for eng, chi in LANDMARK_MAP.items():
            if eng.lower() in v_title.lower():
                landmark = chi; break

    if not landmark:
        landmark = re.sub(r'(?i)Live Cam|4K|Stream|即時影像|Taiwan', '', clean_title).strip()
        landmark = landmark.split('|')[0].strip() if landmark else "即時影像"

    return f"【{brand}】{landmark}"

def get_live_info():
    """
    獲取 YouTube 資訊，合併手動連結與自動抓取結果。
    """
    ydl_opts = {
        'quiet': True, 'extract_flat': True, 'skip_download': True,
        'playlist_items': '1-20', 'ignoreerrors': True, 'no_warnings': True,
        'extra_headers': {
            'Accept-Language': 'zh-TW,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    }
    
    final_output = []
    
    # 建立一個集合來排除重複網址
    all_seen_urls = set()

    for genre, channels in CATEGORIES.items():
        genre_list = []
        
        # A. 先加入手動連結
        if genre in MANUAL_LINKS:
            for item in MANUAL_LINKS[genre]:
                url = item.split(',')[-1]
                genre_list.append(item)
                all_seen_urls.add(url)

        # B. 抓取 YouTube 直播
        print(f">>> 正在同步: {genre}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for nickname, url in channels.items():
                try:
                    info = ydl.extract_info(url, download=False)
                    if not info: continue
                    entries = info.get('entries', []) or ([info] if info.get('live_status') == 'is_live' else [])

                    for entry in entries:
                        is_live = entry.get('live_status') == 'is_live' or entry.get('is_live')
                        if not is_live: continue
                        
                        v_url = f"https://www.youtube.com/watch?v={entry.get('id')}"
                        if v_url not in all_seen_urls:
                            final_title = extract_best_title(entry.get('title', ''), nickname)
                            genre_list.append(f"{final_title},{v_url}")
                            all_seen_urls.add(v_url)
                except: continue
        
        if genre_list:
            final_output.append(genre)
            final_output.extend(genre_list)
            final_output.append("") 
                
    return final_output

if __name__ == "__main__":
    results = get_live_info()
    with open("live_list.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results).strip() + "\n")
    print("\n✅ 清單已更新 (含手動新增連結)！")
