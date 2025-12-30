import yt_dlp
import re

# ==========================================
# 1. 頻道與手動連結配置區
# ==========================================
CATEGORIES = {
    "跨年,#genre#": {
        "小寬日常": "https://www.youtube.com/@%E5%B0%8F%E5%AF%AC%E6%97%A5%E5%B8%B8/streams",
        "Suwah Music 瑞华唱片": "https://www.youtube.com/@SuwahMusic/streams"		
    },
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
        "三立iNEWS": "https://www.youtube.com/channel/UCoNYj9OFHZn3ACmmeRCPwbA",		
        "三立LIVE新聞": "https://www.youtube.com/@setnews/streams",
        "中天新聞CtiNews": "https://www.youtube.com/@中天新聞CtiNews/streams",
        "中天電視CtiTv": "https://www.youtube.com/@中天電視CtiTv/streams",
        "中天亞洲台": "https://www.youtube.com/@中天亞洲台CtiAsia/streams",	
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
        "AI主播倪珍Nikki 播新聞": "https://www.youtube.com/@NOWNEWS-AI-Anchor-Niki/streams",
        "BNE TV - 新西兰中文国际频道": "https://www.youtube.com/@BNETVNZ/streams",	
        "POP Radio聯播網": "https://www.youtube.com/@917POPRadio/streams",
        "LIVE NOW": "https://www.youtube.com/@LiveNow24H/streams",	
        "鳳凰衛視PhoenixTV": "https://www.youtube.com/@phoenixtvglobal/streams",
        "HOY 資訊台 × 有線新聞": "https://www.youtube.com/@HOYTVHK/streams",		
        "CCTV中文": "https://www.youtube.com/@CCTVCH/featured",
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
        "東森綜合台": "https://www.youtube.com/@ettv32/streams",
        "中天娛樂頻道": "https://www.youtube.com/user/ctimulti",		
        "57怪奇物語": "https://www.youtube.com/@57StrangerThings/streams",
        "命運好好玩": "https://www.youtube.com/@eravideo004/streams",	
        "TVBS娛樂頭條": "https://www.youtube.com/@tvbsenews/streams",	
        "台灣啟示錄": "https://www.youtube.com/@ebcapocalypse/streams",
        "緯來日本台": "https://www.youtube.com/@VideolandJapan/streams",
        "我愛小明星大跟班": "https://www.youtube.com/@我愛小明星大跟班/streams",
        "明星下班路": "https://www.youtube.com/@gtvstaroad/videos",		
        "204檔案": "https://www.youtube.com/@204/streams",
        "WTO姐妹會": "https://www.youtube.com/@WTOSS/streams",	
        "好看娛樂": "https://www.youtube.com/@好看娛樂/streams",
        "超級夜總會": "https://www.youtube.com/@SuperNightClubCH29/videos",	
        "TVBS女人我最大": "https://www.youtube.com/@tvbsqueen/streams",
        "型男大主廚": "https://www.youtube.com/@twcookingshow/videos",
        "娛樂星動線": "https://www.youtube.com/@chinatimesent/streams",		
        "非凡大探索": "https://www.youtube.com/@ustvfoody/streams",
        "你好, 星期六 Hello Saturday Official": "https://youtube.com/@hellosaturdayofficial?si=--6KGPLtLMpXRMN5",	
        "BIF相信未來 官方頻道": "https://www.youtube.com/@BelieveinfutureTV/streams",
        "GTV 自由的旅行者": "https://www.youtube.com/@gtvfreedomtravelers/streams",
        "原視 TITV+": "https://www.youtube.com/@titv8932/videos",
		"寶島神很大": "https://www.youtube.com/@godBlessBaodao/streams",
        "Taste The World": "https://www.youtube.com/@TasteTheWorld66/videos",
        "現在宅知道": "https://www.youtube.com/@cbotaku/streams",
		"娱综星天地": "https://www.youtube.com/@娱综星天地/streams",
        "靖天電視台": "https://www.youtube.com/@goldentvdrama/streams",
        "靈異錯別字": "https://www.youtube.com/@靈異錯別字ctiwugei/streams",
        "綜藝一級棒": "https://www.youtube.com/@NO1TVSHOW/streams",		
        "下面一位": "https://www.youtube.com/@ytnextone_1/streams",		
        "公共電視-我們的島": "https://www.youtube.com/@ourislandTAIWAN/streams",
        "WeTV 綜藝經典": "https://www.youtube.com/@WeTV-ClassicVariety/videos",
        "爆梗TV": "https://www.youtube.com/@爆梗PunchlineTV/streams",
		"緯來新聞網": "https://www.youtube.com/@videolandnews/streams",
        "灿星官方频道": "https://www.youtube.com/@CanxingMediaOfficialChannel/streams",
        "陕西广播电视台官方频道": "https://www.youtube.com/@chinashaanxitvofficialchan2836/videos",		
        "北京廣播電視台生活頻道": "https://www.youtube.com/@Brtvofficialchannel/streams"		
        
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
        "Vidol TV": "https://youtube.com/@vidoltv?si=wc0vxpCHtEVhigyf",		
        "緯來戲劇台": "https://www.youtube.com/@Vldrama43/streams",
        "緯來育樂台": "https://www.youtube.com/@maxtv71/videos",		
        "愛爾達綜合台": "https://www.youtube.com/@ELTAWORLD/streams",
        "愛爾達影劇台": "https://www.youtube.com/@eltadrama/streams",
        "VBL Series": "https://www.youtube.com/@variety_between_love/streams",
        "甄嬛传全集": "https://www.youtube.com/@LegendofConcubineZhenHuan/videos",		
        "精选大剧": "https://www.youtube.com/@精选大剧/videos",		
        "百纳经典独播剧场": "https://www.youtube.com/@BainationTVSeriesOfficial/streams",
        "华录百納熱播劇場": "https://www.youtube.com/@Baination/streams",	
        "iQIYI 爱奇艺": "https://www.youtube.com/@iQIYIofficial/streams",
        "iQIYI Show Giải Trí Vietnam": "https://www.youtube.com/@iQIYI_ShowGi%E1%BA%A3iTr%C3%ADVietnam/videos",		
        "iQIYI Indonesia": "https://www.youtube.com/@iQIYIIndonesia/streams",
        "爱奇艺大电影": "https://www.youtube.com/@iQIYIMOVIETHEATER/streams",
        "iQIYI 慢綜藝": "https://www.youtube.com/@iQIYILifeShow/streams",		
        "iQIYI 潮綜藝": "https://www.youtube.com/@iQIYISuperShow/streams",
        "iQIYI 爆笑宇宙": "https://www.youtube.com/@iQIYIHappyWorld/streams",		
        "MangoTV Shorts": "https://www.youtube.com/@MangoTVShorts/videos",
        "MangoTV English": "https://www.youtube.com/@MangoTVEnglishOfficial/videos",
        "MangoTV Malaysia": "https://www.youtube.com/@MangoTVMalaysia/streams",		
        "芒果TV古裝劇場": "https://www.youtube.com/@TVMangoTVCostume-yw1hj/videos",	
        "芒果TV青春剧场": "https://www.youtube.com/@MangoTVDramaOfficial/streams",	
        "芒果TV季风频道": "https://www.youtube.com/@MangoMonsoon/streams",	
        "芒果TV推理宇宙": "https://youtube.com/@mangotv-mystery?si=CRrdrZLRFBy4GXtQ",
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
        "贵州卫视官方频道": "https://www.youtube.com/@gztvofficial/streams",
        "喜剧大联盟": "https://www.youtube.com/@SuperComedyLeague/streams",
        "China Zone 古裝劇場": "https://www.youtube.com/@ChinaZoneCostume/streams",
        "China Zone 剧乐部": "https://www.youtube.com/@ChinaZoneDrama/streams",
        "China Zone 流金岁月": "https://www.youtube.com/@ChinaZone-ClassicDrama/streams",
        "China Zone梦想剧场": "https://www.youtube.com/@ChinaZone-DreamDrama/streams",		
        "欢娱影视官方频道": "https://www.youtube.com/@chinahuanyuent.officialchannel/streams",
        "乐视视频官方频道": "https://www.youtube.com/@letvdramas/streams",		
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
        "Muse木棉花-TW": "https://www.youtube.com/@MuseTW/streams",	
        "Muse木棉花-闔家歡": "https://www.youtube.com/@Muse_Family/streams",
        "Ani-One中文官方動畫頻道": "https://www.youtube.com/@AniOneAnime/streams",
        "Lv.99 Animation Club": "https://www.youtube.com/@Lv.99AnimationClub/streams",
        "嘀嘀漫畫站": "https://www.youtube.com/@嘀嘀漫畫站DidiComic/streams",			
        "嗶哩嗶哩動畫Anime Made By Bilibili": "https://www.youtube.com/@MadeByBilibili/streams",	
        "回歸線娛樂": "https://www.youtube.com/@tropicsanime/streams",
        "愛奇藝國漫": "https://www.youtube.com/@iQIYIAnimation/streams",
        "艾瑪愛學習": "https://www.youtube.com/@EmmaLearning/streams",		
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
        "CBC籃球聯盟": "https://www.youtube.com/@cbc726/streams",
        "MAX籃球聯盟": "https://www.youtube.com/@MAX-mv8mr/streams",		
        "TPVL 台灣職業排球聯盟": "https://www.youtube.com/@tpvl.official/streams",
        "籃海運動": "https://www.youtube.com/@pbe1772/streams",		
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
	    "4kTQ-music": "https://www.youtube.com/@4kTQ-music/streams",	
	    "Eight无限": "https://www.youtube.com/@eight-audio/streams",
	    "相信音樂BinMusic": "https://www.youtube.com/@binmusictaipei/streams",
	    "周杰倫 Jay Chou": "https://www.youtube.com/@jaychou/streams",		
	    "Sony Music Entertainment Hong Kong": "https://www.youtube.com/@sonymusichk/streams",		
	    "Hot TV": "https://www.youtube.com/@hotfm976/streams",
	    "时间节拍 Melody": "https://www.youtube.com/@%E6%97%B6%E9%97%B4%E8%8A%82%E6%8B%8DMelody/streams",
	    "孤心旋律": "https://www.youtube.com/@GuXinXuanlu68/streams",		
	    "KKBOX 华语新歌周榜": "https://www.youtube.com/@KKBOX-baidu6868/streams",
	    "Douyin Chill": "https://www.youtube.com/@DouyinChill-xr2yk/streams",
	    "生活乐章": "https://www.youtube.com/@生活乐章/streams",	    
	    "抖音音樂台": "https://www.youtube.com/@douyinyinyuetai/streams",
	    "青春音乐铺": "https://www.youtube.com/@青春音乐铺/streams",
	    "水月琴音": "https://www.youtube.com/@Shuiyueqinyin/streams",	    
	    "Cherry 葵": "https://www.youtube.com/@Cherriexin/streams",
	    "Kanata Ch. 天音かなた": "https://www.youtube.com/@AmaneKanata/streams",		
	    "CMIX - Chill Mix": "https://www.youtube.com/@ChillMix-CMIX/streams",		
	    "「KING AMUSEMENT CREATIVE」公式チャンネル": "https://www.youtube.com/@KAC_official/streams",
	    "FOR FUN RADIO TIME Music channel": "https://www.youtube.com/@FORFUNRADIOTIME-Relax/streams",		
	    "Mellowbeat Seeker": "https://www.youtube.com/@mellowbeatseeker/streams",
	    "The Good Life Radio x Sensual Musique": "https://www.youtube.com/@TheGoodLiferadio/streams",	
        "Best of Mix": "https://www.youtube.com/@bestofmixlive/streams",
        "Rock FM": "https://www.youtube.com/@rockfm1/streams",
        "Radio Mix": "https://www.youtube.com/@liveradiomix/streams",
        "Too Music": "https://www.youtube.com/@toomusicc/streams",		
	    "Radio Hits Music": "https://www.youtube.com/@LiveMusicRadio/streams",
	    "Dark City Sounds": "https://www.youtube.com/@darkcitysounds/streams",
	    "Pop Japan Music": "https://www.youtube.com/@PopJapanMusic-du6su/streams",
	    "Tokyo Sound Rank": "https://www.youtube.com/@TokyoSoundRank98/streams",
	    "MEET48 Global": "https://www.youtube.com/@MEET48Global/streams",		
	    "KING AMUSEMENT CREATIVE": "https://www.youtube.com/@KAC_official/streams"		
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
        "董事長開講": "https://www.youtube.com/@dongsshow/streams",
        "政經關不了": "https://www.youtube.com/@truevoiceoftaiwan/streams",			
        "57爆新聞": "https://www.youtube.com/@57BreakingNews/streams",
        "關鍵時刻": "https://www.youtube.com/@ebcCTime/streams",
		"郭正亮頻道": "https://www.youtube.com/@Guovision-TV/streams",
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
        "海豚多媒體": "https://www.youtube.com/@24811001/streams",
        "玉麟網路電視台": "https://www.youtube.com/@YuLinNetworkTelevision/streams",		
        "寶島文化台": "https://www.youtube.com/@bdtvbest/streams",
        "三聖電視台": "https://www.youtube.com/@tsimtv-01/streams",		
        "桐瑛台中電視臺": "https://www.youtube.com/@%E6%A1%90%E7%91%9B%E5%8F%B0%E4%B8%AD%E9%9B%BB%E8%A6%96%E8%87%BA/streams",
        "桐瑛虎尾電視臺": "https://www.youtube.com/@%E6%A1%90%E7%91%9B%E8%99%8E%E5%B0%BE%E9%9B%BB%E8%A6%96%E8%87%BA/streams",
        "桐瑛台南電視臺": "https://www.youtube.com/@%E6%A1%90%E7%91%9B%E5%8F%B0%E5%8D%97%E9%9B%BB%E8%A6%96%E8%87%BA/streams",		
        "momo購物一台": "https://www.youtube.com/@momoch4812/streams",
	    "momo購物二台": "https://www.youtube.com/@momoch3571/streams",
	    "ViVa TV美好家庭購物": "https://www.youtube.com/@ViVaTVtw/streams",
	    "Live東森購物台": "https://www.youtube.com/@HotsaleTV/streams"		
    },
    "國會,#genre#": {
        "國會頻道": "https://www.youtube.com/@parliamentarytv/streams"
    },
    "宗教,#genre#": {
        "淨土宗": "https://www.youtube.com/@plbtp/streams",
        "中華傳統文化教育中心": "https://www.youtube.com/@520wtv/streams",
        "修心時刻": "https://www.youtube.com/@Practicetime7/streams",
        "華藏衛視直播2台": "https://www.youtube.com/@hztv2212/streams",		
        "佛光山梵唄讚頌團": "https://www.youtube.com/@VG_MUSICAL/streams",
        "生命電視台": "https://www.youtube.com/@LIFETV_HaiTao/streams",		
        "遠東良友": "https://www.youtube.com/@febc/streams"		
    },
    "教育,#genre#": {	
        "龍騰高中聲": "https://www.youtube.com/@LTeduForStudent/streams",
        "Oziter茅": "https://www.youtube.com/@oziter/streams",		
        "ABC Learning English": "https://www.youtube.com/@ABCLearningEnglish/streams",		
        "學習粵語": "https://www.youtube.com/@CantoneseClass101/streams",
        "南非荷蘭語": "https://www.youtube.com/@AfrikaansPod101/streams",
        "學習印地語": "https://www.youtube.com/@hindipod101/streams",
        "學習菲律賓語": "https://www.youtube.com/@FilipinoPod101/streams",
        "學習烏爾都語": "https://www.youtube.com/@UrduPod101/streams",
        "學習德語": "https://www.youtube.com/@Germanpod101/streams",
        "學習土耳其語": "https://www.youtube.com/@TurkishClass101/streams",
        "學習阿拉伯語": "https://www.youtube.com/@ArabicPod101/streams",
        "學習瑞典語": "https://www.youtube.com/@SwedishPod101/streams",
        "學習挪威語": "https://www.youtube.com/@NorwegianClass101/streams",
        "學習希伯來語": "https://www.youtube.com/@HebrewPod101/streams",
        "學習希臘語": "https://www.youtube.com/@GreekPod101/streams",
        "學習波蘭語": "https://www.youtube.com/@PolishPod101/streams",
        "學習日文": "https://www.youtube.com/@JapanesePod101/streams",
        "學習中文": "https://www.youtube.com/@ChineseClass101/streams",
        "學習匈牙利語": "https://www.youtube.com/@HungarianPod101/streams",
        "學習芬蘭語": "https://www.youtube.com/@FinnishPod101/streams",
        "學習荷蘭語": "https://www.youtube.com/@DutchPod101/streams",
        "學習韓語": "https://www.youtube.com/@KoreanClass101/streams",
        "學習法語": "https://www.youtube.com/@frenchpod101/streams",		
        "學習波斯語": "https://www.youtube.com/@PersianPod101/streams"		
    },		
    "風景,#genre#": {
        "TW Live Cam": "https://www.youtube.com/@DanjiangBridge/streams",	
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

# 若某些頻道在美國伺服器 100% 報 404，請在此手動填入連結保底
MANUAL_LINKS = {
    "跨年,#genre#": [
        "【臺北市政府】【1900】臺北最High新年城,https://www.youtube.com/watch?v=6Ekqt2eQWaM",
        "【壹電視】【1900】「2026雄嗨趴」高雄跨年晚會 ,https://www.youtube.com/watch?v=6nV37uSsx1o",
        "【嘉義+1 We Chiayi】【1730】「2026雄嗨趴」高雄跨年晚會 ,https://www.youtube.com/watch?v=_ePcCXyHDAk",		
        "【TVBS】【2400】2026新年快樂! 101、劍湖山、義大煙火秀,https://www.youtube.com/watch?v=ecZwForwUZw",
        "【TVBS】【2100】澳洲跨年煙火,https://www.youtube.com/watch?v=DGl5KwpeCF0",
        "【TVBS】【2026】新北淡水跨河煙火秀,https://www.youtube.com/watch?v=nKGzbBDRGDU",
        "【TVBS】【2000】新全台跨年晚會精彩不錯過,https://www.youtube.com/watch?v=X2ghfCFsb0Y",
        "【東森新聞】【2355】SPARK 101🎆6分鐘絢爛迎接2026,https://www.youtube.com/watch?v=jaycBr8YWT4",
        "【東森新聞】【1800】大新竹跨年晚會,https://www.youtube.com/watch?v=fO69UoXVgUU",
        "【東森新聞】【1700】新北淡水漁人碼頭,https://www.youtube.com/watch?v=pTWzBlJMDh4",
        "【台視新聞】【2350】劍湖山史上最High「1公里環繞式」摩天輪跨年煙火秀,https://www.youtube.com/watch?v=fVdO_J2WSpQ",
        "【台視新聞】【2350】高雄義大煙火秀,https://www.youtube.com/watch?v=ETykNhwk8xs",
        "【台視新聞】【2350】台北101低煙煙火+光雕秀致敬,https://www.youtube.com/watch?v=5siQQu4YLYg",
        "【台視新聞】【2100】2026雪梨煙火秀,https://www.youtube.com/watch?v=yg3DWq9LMrg"
        "【台視新聞】【2026】閃耀新北「淡江大橋」13分14秒 跨河煙火迎2026,https://www.youtube.com/watch?v=CVI2QpMRY7A",
        "【台視新聞】【1900】紐西蘭奧克蘭,https://www.youtube.com/watch?v=apIF_-2liiM",
        "【中視新聞】【1900】臺北最High新年城-2026跨年晚會,https://www.youtube.com/watch?v=1jnde6OlFwk",
        "【民視新聞網】【0800】2026英國倫敦跨年煙火盛典,https://www.youtube.com/watch?v=auDc55UKXio",
        "【民視新聞網】【0530】2026阿里山日出印象音樂會,https://www.youtube.com/watch?v=m3EL4m2RjHo",
        "【民視新聞網】【2100】2026澳洲雪梨獨特的跨年,https://www.youtube.com/watch?v=ThMmrKvO4JU",
        "【民視新聞網】【1940】2025東港跨年聯歡晚會,https://www.youtube.com/watch?v=ThMmrKvO4JU",
        "【民視新聞網】【1940】2026紐西蘭跨年煙火秀,https://www.youtube.com/watch?v=8eFrTsKsZjY",
        "【非凡電視】【2350】劍湖山史上最High「1公里環繞式」摩天輪跨年煙火秀,https://www.youtube.com/watch?v=exM3jdA42eg",
        "【非凡電視】【2350】台北101低煙煙火+光雕秀致敬,https://www.youtube.com/watch?v=YNyQp_v2nmY",
        "【非凡電視】【2350】高雄義大全台首創「藍色流星雨」 999秒跨年煙火秀迎新年,https://www.youtube.com/watch?v=0Q3kgnrplRo",
        "【非凡電視】【2100】全球跨年 2026雪梨煙火秀,https://www.youtube.com/watch?v=BD2vmXPX-uc",
        "【非凡電視】【2026】閃耀新北「淡江大橋」,https://www.youtube.com/watch?v=uk3JixPp3Lc",
        "【非凡電視】【1900】紐西蘭奧克蘭 迎接2026,https://www.youtube.com/watch?v=FtdlBFqAFk8",
        "【三立新聞】【1600】拉斯維加斯封街迎2026,https://www.youtube.com/watch?v=GLkmiJxpEOA",
        "【三立新聞】【2300】迎接2026！日本寺院撞鐘108次拋開煩惱,https://www.youtube.com/watch?v=gFbioBs5Ryg",
        "【三立新聞】【1200】「大蘋果」震撼降臨！紐約迎2026,https://www.youtube.com/watch?v=hG1jiJol8WQ",
        "【三立新聞】【0800】「迎2026！英國大笨鐘報時鐘聲,https://www.youtube.com/watch?v=xi0zWBcjVuc",
        "【三立新聞】【2400】義大跨年焰火登場,https://www.youtube.com/watch?v=uF1ebVWRqjY",
        "【三立新聞】【2400】摩天輪跨年煙火秀 劍湖山世界高空煙火彈遍布全樂園夜空,https://www.youtube.com/watch?v=WFLVt0lUJWA",
        "【三立新聞】【2300】全球最神祕國家也跨年！北韓煙火歌舞秀迎2026,https://www.youtube.com/watch?v=E_tRqvrN6fk",
        "【三立新聞】【2100】迎接2026！澳洲雪梨璀璨煙火秀傳達和平與多元,https://www.youtube.com/watch?v=FnaU9MwznaE",
        "【三立新聞】【2010】閃耀新北1314跨河煙火迎接2026,https://www.youtube.com/watch?v=nzwtqgOXpfA",	
        "【三立新聞】【1900】全球最早跨年煙火來了！紐西蘭率先迎接2026,https://www.youtube.com/watch?v=juhB825g-ww",
        "【三立新聞】【1800】迎接2026！澳洲雪梨先行煙火秀拉開序幕,https://www.youtube.com/watch?v=uZISEayt3o8",
        "【中天新聞】【0600】迎接2026第一道曙光 本島平地最早日在台東三仙台,https://www.youtube.com/watch?v=wBeUBZZCeLk",
        "【中天新聞】【0500】迎接2026 全球各地接力煙火綻放瘋跨年,https://www.youtube.com/watch?v=iPiFSlfuIcQ",
        "【中天新聞】【2350】全台瘋跨年 煙火接力直播攏底家,https://www.youtube.com/watch?v=ruM0jITtHIg",
        "【中天新聞】【2300】日本東京嗨跨年 108聲鐘響祈福喜迎,https://www.youtube.com/watch?v=wJW6KmpFNVQ",
        "【中天新聞】【2100】澳洲雪梨歌劇院上空 綻放跨年煙火,https://www.youtube.com/watch?v=ojrE1wcStK0",
        "【中天新聞】【1900】紐西蘭全球第一個跨年 奧克蘭煙火,https://www.youtube.com/watch?v=caacdc1NRng",
        "【中天新聞】【1900】2026彰化田中跨年晚會,https://www.youtube.com/watch?v=Fua-K7Yjydw",
        "【中天新聞】【1600】送別2025最後一抺夕陽 ,https://www.youtube.com/watch?v=eCoW37hPuts",
        "【中天新聞】【1600】全台跨年晚會嗨翻天! ,https://www.youtube.com/watch?v=HFbh3DmwsV8"		
    ],
    "台灣,#genre#": [
        "【TTV LIVE 台視直播】台視,https://www.youtube.com/watch?v=uDqQo8a7Xmk&rco=1&ab_channel=TTVLIVE%E5%8F%B0%E8%A6%96%E7%9B%B4%E6%92%AD"
    ],
	"音樂,#genre#": [
        "【周杰倫】音樂時光機,https://www.youtube.com/watch?v=q8hw5oKCDp4",
		"【五月天】不間斷霸佔你耳朵,https://www.youtube.com/live/R62E7cFWX6o"
    ],
    "少兒,#genre#": [
        "【Muse木棉花】魔都精兵的奴隸,https://www.youtube.com/live/qXD7NKZlLPA?si=zyVpCoX7dpqsJNWn",
        "【Muse木棉花】間諜家家酒,https://www.youtube.com/watch?v=dI2negE-v4c",
        "【Muse木棉花】進擊的巨人,https://www.youtube.com/watch?v=GlVvyu7jehk",
        "【Muse木棉花】關於我轉生變成史萊姆這檔事,https://www.youtube.com/watch?v=ATsYVyh_Nwk",		
        "【Muse木棉花】葬送的芙莉蓮,https://www.youtube.com/live/DAVfn4Sp8xw?si=ZEWt4HIP6KBuhaYr",
        "【Muse木棉花】蠟筆小新TV版,https://www.youtube.com/watch?v=ENnjj7jQ23g",
        "【Muse木棉花】新哆啦A夢,https://www.youtube.com/watch?v=jbZCyIhL4WQ",
        "【Muse木棉花】中華一番,https://www.youtube.com/watch?v=mRCXonM5ru8",
        "【Muse木棉花】我們這一家,https://www.youtube.com/watch?v=e1gbvCkwxFE",		
		"【Ani-One】白色相簿2,https://www.youtube.com/watch?v=inuV4C7UCxo",
        "【Ani-One】佐賀偶像是傳奇,https://www.youtube.com/watch?v=SNG8wNLU-_s",
        "【Ani-One】遊戲王－怪獸之決鬥,https://www.youtube.com/watch?v=nGDX7qUl6mw",
		"【回歸線娛樂】真珠美人魚,https://www.youtube.com/watch?v=BLag8MOBUg8",
        "【回歸線娛樂】夢幻遊戲,https://www.youtube.com/watch?v=7j8chjyp7tw"
    ]
}

# ==========================================
# 2. 地標優化與翻譯邏輯
# ==========================================
LANDMARK_MAP = {
    "Shoushan Lovers": "壽山情人觀景台", "Lianchihtan": "蓮池潭", "Lotus Pond": "蓮池潭",
    "Cijin": "旗津", "Baling": "巴陵大橋", "Shihmen Reservoir": "石門水庫",
    "Fenqihu": "奮起湖", "Eryanping": "二延平", "Sanxiantai": "三仙台", "Chaikou": "綠島柴口"
}

def extract_best_title(v_title, nickname):
    # 國會特殊處理
    if "國會頻道" in nickname:
        segments = re.split(r'[\|\-\—\–]', v_title)
        return f"【國會頻道】{segments[0].strip()}" if len(segments) > 1 else f"【國會頻道】{v_title}"

    # 風景品牌標準化
    brand = nickname
    for b in ["高雄", "台北", "桃園", "新北", "阿里山", "東部海岸", "MangoTV"]:
        if b in nickname: brand = b; break

    # 清理地標名稱
    clean_title = re.sub(r'[【\[\(].*?[】\]\)]', '', v_title).strip()
    
    # 嘗試從標題提取中文核心
    chinese_parts = "".join(re.findall(r'[\u4e00-\u9fa5]+', clean_title))
    for n in ["即時影像", "直播", "官方", "桃園", "台北", "高雄", "新北", brand]:
        chinese_parts = chinese_parts.replace(n, "")
        
    landmark = chinese_parts if len(chinese_parts) >= 2 else ""
    
    # 英文翻譯救援
    if not landmark:
        for eng, chi in LANDMARK_MAP.items():
            if eng.lower() in v_title.lower(): landmark = chi; break
            
    return f"【{brand}】{landmark if landmark else clean_title[:15]}"

# ==========================================
# 3. 核心抓取邏輯 (多路徑重試機制)
# ==========================================
def get_live_info():
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'playlist_items': '1-10',
        'ignoreerrors': True,  # 報錯不中斷
        'no_warnings': True,
        'extra_headers': {
            'Accept-Language': 'zh-TW,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    }
    
    final_output = []
    all_seen_urls = set()

    for genre, channels in CATEGORIES.items():
        genre_list = []
        
        # A. 加入手動保底連結
        if genre in MANUAL_LINKS:
            for item in MANUAL_LINKS[genre]:
                url = item.split(',')[-1].strip()
                genre_list.append(item)
                all_seen_urls.add(url)

        # B. 自動抓取 YouTube 直播
        print(f">>> 正在掃描分類: {genre}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for nickname, base_url in channels.items():
                # 採用多路徑嘗試：1. Streams 分頁 2. 首頁 3. Embed API
                search_paths = [f"{base_url}/streams", base_url] if "@" in base_url else [base_url]
                
                success = False
                for path in search_paths:
                    try:
                        info = ydl.extract_info(path, download=False)
                        if not info: continue
                        
                        entries = info.get('entries', []) or ([info] if info.get('live_status') == 'is_live' else [])
                        
                        for entry in entries:
                            if entry and (entry.get('live_status') == 'is_live' or entry.get('is_live')):
                                v_id = entry.get('id')
                                v_url = f"https://www.youtube.com/watch?v={v_id}"
                                if v_url not in all_seen_urls:
                                    final_title = extract_best_title(entry.get('title', ''), nickname)
                                    genre_list.append(f"{final_title},{v_url}")
                                    all_seen_urls.add(v_url)
                                    success = True
                        if success: break
                    except:
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
    print("\n✅ 清單產出成功，請檢查 live_list.txt")
