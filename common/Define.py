# -*- coding: utf-8 -*-

"""
声明、定义
"""

class RETURN_CODE:
	SUCCESS = "SUCCESS"   # 成功
	FAIL    = "FAIL"      # 失败


	PRODUCT_REORDER         = "PRODUCT_REORDER"     # 产品重复订购
	PRODUCT_CANT_ORDER      = "PRODUCT_CANT_ORDER"  # 该产品当前无法订购
	PRODUCT_CANT_RENEW      = "PRODUCT_CANT_RENEW"  # 该产品不可续订
	PRODUCT_NOT_ORDERED     = "PRODUCT_NOT_ORDERED" # 产品未订购
	INVALID_FEE_CODE        = "INVALID_FEE_CODE"    # 无效的计费代码
	INVALID_PRODUCT         = "INVALID_PRODUCT"     # 无效的产品代码
	DX_RETURN_FAIL          = "DX_RETURN_FAIL"      # 电信返回订购失败
	PAY_TOO_FAST            = "PAY_TOO_FAST"        # 用户支付频率过快
	USER_PAY_DISABLED       = "USER_PAY_DISABLED"   # 该用户禁止支付
	INVALID_PAY_PASSWD      = "INVALID_PAY_PASSWD"  # 无效的支付密码
	PAY_MONTH_LIMIT         = "PAY_MONTH_LIMIT"     # 达到月消费限额
	INVALID_SIGN            = "INVALID_SIGN"        # 无效的签名
	INVALID_PARAMS          = "INVALID_PARAMS"      # 无效的（请求）参数
	USER_NOT_LOGINED        = "USER_NOT_LOGINED"    # 用户未登录

	CHANNEL_EXISTED_IN_FAVORS    = "CHANNEL_EXISTED_IN_FAVORS"     # 该课件已经在收藏夹中
	CHANNEL_NOTEXISTED_IN_FAVORS = "CHANNEL_NOTEXISTED_IN_FAVORS"  # 该课件没在收藏夹中
	LESSON_EXISTED_IN_FAVORS     = "LESSON_EXISTED_IN_FAVORS"      # 该课程已经在收藏夹中
	LESSON_NOTEXISTED_IN_FAVORS  = "LESSON_NOTEXISTED_IN_FAVORS"   # 该课程没在收藏夹中



class PRODUCT_TYPE:
	"""
	充值（支付）类型。主要用于PaymentOrders
	"""
	ONETIME    = 0  # 单次支付
	MONTHS     = 1  # 包月支付
	DAYS       = 2  # 包日支付

	# MONTHS      = 0  # 包月支付
	# SEASONS     = 1  # 季度支付
	# HALFYEARS   = 2  # 半年支付
	# YEARS       = 3  # 年支付

PRODUCT_TYPE_CHOICES = (
	(PRODUCT_TYPE.ONETIME, "单次支付"),
	(PRODUCT_TYPE.MONTHS,  "包月支付"),
	(PRODUCT_TYPE.DAYS,    "包日支付"),

	# (PRODUCT_TYPE.MONTHS, "包月支付"),
	# (PRODUCT_TYPE.SEASONS, "季度支付"),
	# (PRODUCT_TYPE.HALFYEARS, "半年支付"),
	# (PRODUCT_TYPE.YEARS, "年支付"),
)
PRODUCT_TYPE_MAPS = dict(PRODUCT_TYPE_CHOICES)


class PAY_STATE:
	"""
	充值（支付）状态。主要用于PaymentOrders
	"""
	WAITING = 0  # 等待中
	SUCCESS = 1  # 成功
	FAIL    = 2  # 失败


class PAY_TYPE:
	"""
	支付类型（如支付宝支付、微信扫码支付等等）
	"""
	UNKNOWN    = 0  # 未知
	PT_RMB     = 1  # 运营商平台RMB支付
	PT_SCORE   = 2  # 运营商平台积分支付


class PPID:
	"""
	平台提供商定义
	"""
	UNKNOWN   = 0
	DX        = 1  # 电信
	GD        = 2  # 广电
	LT        = 3  # 联通
	CW        = 4  # 创维


class POH_TYPE:
	"""
	platform of hardware
	硬件平台类型
	"""
	UNKNOWN = 0
	IPTV    = 1
	OTT     = 2

class BP_TYPE:
	"""
	平台业务类型
	"""
	UNKNOWN = 0
	GAME    = 1 # 游戏
	EDU     = 2 # 教育

class VIDEO_PLAY_AUTH:
	"""
	视频播放权限
	"""
	FREE = 0  # 免费
	PAY  = 1  # 付费

# 视频播放权限选择
VIDEO_PLAY_AUTH_CHOICES = (
	(VIDEO_PLAY_AUTH.FREE, "免费播放"),
	(VIDEO_PLAY_AUTH.PAY,  "付费播放"),
)



# 按钮额外标志
LINK_FLAG_CHOICES = (
	(0, "无"),
	(1, "推荐"),
	(2, "新增"),
	(3, "免费"),
	(4, "热门"),
	(5, "活动"),
)

# 首页按钮额外标志对应的图片地址，按上面顺序匹配
LINK_FLAG_IMG_URLS_HOME = (
	"",
	"/static/main/images/common/tips/index/recommend.png",
	"/static/main/images/common/tips/index/new.png",
	"/static/main/images/common/tips/index/free.png",
	"/static/main/images/common/tips/index/hot.png",
	"",
)

# 视频列表按钮额外标志对应的图片地址，按上面顺序匹配
LINK_FLAG_IMG_URLS_LIST = (
	"",
	"/static/main/images/common/tips/recommend.png",
	"/static/main/images/common/tips/new.png",
	"/static/main/images/common/tips/free.png",
	"/static/main/images/common/tips/hot.png",
	"",
)


EVENT_CHOICES = (
	(0,	        "KEY_REQUEST"),
	(1,         "KEY_DOWNLOAD"),
	(2,         "KEY_TRY_APPLY"),
	(3,         "KEY_TRY_APPLY_SUCCESS"),
	(4,		    "KEY_APPLIED_START"),
	(5,		    "KEY_APPLIED"),
	(6,		    "KEY_LOADED"),
	(7,		    "KEY_CRASH_FAST_PROTECT"),
	(8,		    "KEY_CRASH_CAUSE_XPOSED_DALVIK"),
	(9,         "KEY_CRASH_CAUSE_XPOSED_ART"),
	(10,	    "KEY_APPLY_WITH_RETRY"),
	(70,	    "KEY_TRY_APPLY_UPGRADE"),
	(71,		"KEY_TRY_APPLY_DISABLE"),
	(72,		"KEY_TRY_APPLY_RUNNING"),
	(73,		"KEY_TRY_APPLY_INSERVICE"),
	(74,		"KEY_TRY_APPLY_NOT_EXIST"),
	(75,		"KEY_TRY_APPLY_GOOGLEPLAY"),
	(76,		"KEY_TRY_APPLY_ROM_SPACE"),
	(77,		"KEY_TRY_APPLY_ALREADY_APPLY "),
	(78,		"KEY_TRY_APPLY_MEMORY_LIMIT"),
	(79,		"KEY_TRY_APPLY_CRASH_LIMIT"),
	(80,		"KEY_TRY_APPLY_CONDITION_NOT_SATISFIED"),
	(81,		"KEY_TRY_APPLY_JIT"),
	(100,		"KEY_APPLIED_UPGRADE"),
	(101,		"KEY_APPLIED_UPGRADE_FAIL"),
	(120,		"KEY_APPLIED_EXCEPTION"),
	(121,		"KEY_APPLIED_DEXOPT_OTHER"),
	(122,		"KEY_APPLIED_DEXOPT_EXIST"),
	(123,		"KEY_APPLIED_DEXOPT_FORMAT"),
	(124,		"KEY_APPLIED_INFO_CORRUPTED"),
	(150,		"KEY_APPLIED_PACKAGE_CHECK_SIGNATURE"),
	(151,		"KEY_APPLIED_PACKAGE_CHECK_DEX_META"),
	(152,		"KEY_APPLIED_PACKAGE_CHECK_LIB_META"),
	(153,		"KEY_APPLIED_PACKAGE_CHECK_APK_TINKER_ID_NOT_FOUND"),
	(154,		"KEY_APPLIED_PACKAGE_CHECK_PATCH_TINKER_ID_NOT_FOUND"),
	(155,		"KEY_APPLIED_PACKAGE_CHECK_META_NOT_FOUND"),
	(156,		"KEY_APPLIED_PACKAGE_CHECK_TINKER_ID_NOT_EQUAL"),
	(157,		"KEY_APPLIED_PACKAGE_CHECK_RES_META"),
	(158,		"KEY_APPLIED_PACKAGE_CHECK_TINKERFLAG_NOT_SUPPORT"),
	(180,		"KEY_APPLIED_VERSION_CHECK"),
	(181,		"KEY_APPLIED_PATCH_FILE_EXTRACT"),
	(182,		"KEY_APPLIED_DEX_EXTRACT"),
	(183,		"KEY_APPLIED_LIB_EXTRACT"),
	(184,		"KEY_APPLIED_RESOURCE_EXTRACT"),
	(200,		"KEY_APPLIED_SUCC_COST_5S_LESS"),
	(201,		"KEY_APPLIED_SUCC_COST_10S_LESS"),
	(202,		"KEY_APPLIED_SUCC_COST_30S_LESS"),
	(203,		"KEY_APPLIED_SUCC_COST_60S_LESS"),
	(204,		"KEY_APPLIED_SUCC_COST_OTHER"),
	(205,		"KEY_APPLIED_FAIL_COST_5S_LESS"),
	(206,		"KEY_APPLIED_FAIL_COST_10S_LESS"),
	(207,		"KEY_APPLIED_FAIL_COST_30S_LESS"),
	(208,		"KEY_APPLIED_FAIL_COST_60S_LESS"),
	(209,		"KEY_APPLIED_FAIL_COST_OTHER"),
	(250,		"KEY_LOADED_UNKNOWN_EXCEPTION"),
	(251,		"KEY_LOADED_UNCAUGHT_EXCEPTION"),
	(252,		"KEY_LOADED_EXCEPTION_DEX"),
	(253,		"KEY_LOADED_EXCEPTION_DEX_CHECK"),
	(254,		"KEY_LOADED_EXCEPTION_RESOURCE"),
	(255,		"KEY_LOADED_EXCEPTION_RESOURCE_CHECK"),
	(300,		"KEY_LOADED_MISMATCH_DEX"),
	(301,		"KEY_LOADED_MISMATCH_LIB"),
	(302,		"KEY_LOADED_MISMATCH_RESOURCE"),
	(303,		"KEY_LOADED_MISSING_DEX"),
	(304,		"KEY_LOADED_MISSING_LIB"),
	(305,		"KEY_LOADED_MISSING_PATCH_FILE"),
	(306,		"KEY_LOADED_MISSING_PATCH_INFO"),
	(307,		"KEY_LOADED_MISSING_DEX_OPT"),
	(308,		"KEY_LOADED_MISSING_RES"),
	(309,		"KEY_LOADED_INFO_CORRUPTED"),
	(350,		"KEY_LOADED_PACKAGE_CHECK_SIGNATURE"),
	(351,		"KEY_LOADED_PACKAGE_CHECK_DEX_META"),
	(352,		"KEY_LOADED_PACKAGE_CHECK_LIB_META"),
	(353,		"KEY_LOADED_PACKAGE_CHECK_APK_TINKER_ID_NOT_FOUND"),
	(354,		"KEY_LOADED_PACKAGE_CHECK_PATCH_TINKER_ID_NOT_FOUND"),
	(355,		"KEY_LOADED_PACKAGE_CHECK_TINKER_ID_NOT_EQUAL"),
	(356,		"KEY_LOADED_PACKAGE_CHECK_PACKAGE_META_NOT_FOUND"),
	(357,		"KEY_LOADED_PACKAGE_CHECK_RES_META"),
	(358,		"KEY_LOADED_PACKAGE_CHECK_TINKERFLAG_NOT_SUPPORT"),
	(400,		"KEY_LOADED_SUCC_COST_500_LESS"),
	(401,		"KEY_LOADED_SUCC_COST_1000_LESS "),
	(402,		"KEY_LOADED_SUCC_COST_3000_LESS"),
	(403,		"KEY_LOADED_SUCC_COST_5000_LESS"),
	(404,		"KEY_LOADED_SUCC_COST_OTHER"),
	(450,		"KEY_LOADED_INTERPRET_GET_INSTRUCTION_SET_ERROR"),
	(451,		"KEY_LOADED_INTERPRET_INTERPRET_COMMAND_ERROR"),
	(452,		"KEY_LOADED_INTERPRET_TYPE_INTERPRET_OK"),
)
EVENT_CHOICES_DICT = dict(EVENT_CHOICES)


EVENT_DICT = {
     #  KEY - PV
	'KEY_REQUEST':"",
	'KEY_DOWNLOAD':"",
	'KEY_TRY_APPLY':"",
	'KEY_TRY_APPLY_SUCCESS':"",
	'KEY_APPLIED_START':"",
	'KEY_APPLIED':"",
	'KEY_LOADED':"",
	'KEY_CRASH_FAST_PROTECT':"",
	'KEY_CRASH_CAUSE_XPOSED_DALVIK':"",
	'KEY_CRASH_CAUSE_XPOSED_ART':"",
	'KEY_APPLY_WITH_RETRY':"",
     # Key -- try apply detail
	'KEY_TRY_APPLY_UPGRADE':"",
	'KEY_TRY_APPLY_DISABLE':"",
	'KEY_TRY_APPLY_RUNNING':"",
	'KEY_TRY_APPLY_INSERVICE':"",
	'KEY_TRY_APPLY_NOT_EXIST':"",
	'KEY_TRY_APPLY_GOOGLEPLAY':"",
	'KEY_TRY_APPLY_ROM_SPACE':"",
	'KEY_TRY_APPLY_ALREADY_APPLY':"",
	'KEY_TRY_APPLY_MEMORY_LIMIT':"",
	'KEY_TRY_APPLY_CRASH_LIMIT':"",
	'KEY_TRY_APPLY_CONDITION_NOT_SATISFIED':"",
	'KEY_TRY_APPLY_JIT':"",
     # Key -- apply detail
	'KEY_APPLIED_UPGRADE':"",
	'KEY_APPLIED_UPGRADE_FAIL':"",
	'KEY_APPLIED_EXCEPTION':"",
	'KEY_APPLIED_DEXOPT_OTHER':"",
	'KEY_APPLIED_DEXOPT_EXIST':"",
	'KEY_APPLIED_DEXOPT_FORMAT':"",
	'KEY_APPLIED_INFO_CORRUPTED':"",
     # package check
	'KEY_APPLIED_PACKAGE_CHECK_SIGNATURE':"",
	'KEY_APPLIED_PACKAGE_CHECK_DEX_META':"",
	'KEY_APPLIED_PACKAGE_CHECK_LIB_META':"",
	'KEY_APPLIED_PACKAGE_CHECK_APK_TINKER_ID_NOT_FOUND':"",
	'KEY_APPLIED_PACKAGE_CHECK_PATCH_TINKER_ID_NOT_FOUND':"",
	'KEY_APPLIED_PACKAGE_CHECK_META_NOT_FOUND':"",
	'KEY_APPLIED_PACKAGE_CHECK_TINKER_ID_NOT_EQUAL':"",
	'KEY_APPLIED_PACKAGE_CHECK_RES_META':"",
	'KEY_APPLIED_PACKAGE_CHECK_TINKERFLAG_NOT_SUPPORT':"",
     # version check
	'KEY_APPLIED_VERSION_CHECK':"",
     # extract error
	'KEY_APPLIED_PATCH_FILE_EXTRACT':"",
	'KEY_APPLIED_DEX_EXTRACT':"",
	'KEY_APPLIED_LIB_EXTRACT':"",
	'KEY_APPLIED_RESOURCE_EXTRACT':"",
     # cost time
	'KEY_APPLIED_SUCC_COST_5S_LESS':"",
	'KEY_APPLIED_SUCC_COST_10S_LESS':"",
	'KEY_APPLIED_SUCC_COST_30S_LESS':"",
	'KEY_APPLIED_SUCC_COST_60S_LESS':"",
	'KEY_APPLIED_SUCC_COST_OTHER':"",
	'KEY_APPLIED_FAIL_COST_5S_LESS':"",
	'KEY_APPLIED_FAIL_COST_10S_LESS':"",
	'KEY_APPLIED_FAIL_COST_30S_LESS':"",
	'KEY_APPLIED_FAIL_COST_60S_LESS':"",
	'KEY_APPLIED_FAIL_COST_OTHER':"",
     #  KEY -- load detail
	'KEY_LOADED_UNKNOWN_EXCEPTION':"",
	'KEY_LOADED_UNCAUGHT_EXCEPTION':"",
	'KEY_LOADED_EXCEPTION_DEX':"",
	'KEY_LOADED_EXCEPTION_DEX_CHECK':"",
	'KEY_LOADED_EXCEPTION_RESOURCE':"",
	'KEY_LOADED_EXCEPTION_RESOURCE_CHECK':"",
	'KEY_LOADED_MISMATCH_DEX':"",
	'KEY_LOADED_MISMATCH_LIB':"",
	'KEY_LOADED_MISMATCH_RESOURCE':"",
	'KEY_LOADED_MISSING_DEX':"",
	'KEY_LOADED_MISSING_LIB':"",
	'KEY_LOADED_MISSING_PATCH_FILE':"",
	'KEY_LOADED_MISSING_PATCH_INFO':"",
	'KEY_LOADED_MISSING_DEX_OPT':"",
	'KEY_LOADED_MISSING_RES':"",
	'KEY_LOADED_INFO_CORRUPTED':"",
     # load package check
	'KEY_LOADED_PACKAGE_CHECK_SIGNATURE':"",
	'KEY_LOADED_PACKAGE_CHECK_DEX_META':"",
	'KEY_LOADED_PACKAGE_CHECK_LIB_META':"",
	'KEY_LOADED_PACKAGE_CHECK_APK_TINKER_ID_NOT_FOUND':"",
	'KEY_LOADED_PACKAGE_CHECK_PATCH_TINKER_ID_NOT_FOUND':"",
	'KEY_LOADED_PACKAGE_CHECK_TINKER_ID_NOT_EQUAL':"",
	'KEY_LOADED_PACKAGE_CHECK_PACKAGE_META_NOT_FOUND':"",
	'KEY_LOADED_PACKAGE_CHECK_RES_META':"",
	'KEY_LOADED_PACKAGE_CHECK_TINKERFLAG_NOT_SUPPORT':"",
	'KEY_LOADED_SUCC_COST_500_LESS':"",
	'KEY_LOADED_SUCC_COST_1000_LESS':"",
	'KEY_LOADED_SUCC_COST_3000_LESS':"",
	'KEY_LOADED_SUCC_COST_5000_LESS':"",
	'KEY_LOADED_SUCC_COST_OTHER':"",
	'KEY_LOADED_INTERPRET_GET_INSTRUCTION_SET_ERROR':"",
	'KEY_LOADED_INTERPRET_INTERPRET_COMMAND_ERROR':"",
	'KEY_LOADED_INTERPRET_TYPE_INTERPRET_OK':"",
}