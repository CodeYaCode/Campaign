# propConf.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'propConf.py'
'@author LiuChen'

# The configurable properties in the editor

propConf = {
	'player' :  {
		'campPid': 'campPid',
		'name'	 : '玩家名',
		'x'		 : 'X',
		'y'		 : 'Y',
	},
	'generals':  {
		# 需要和archive中的字段名匹配
		'brief' : {
			# 主面板显示的信息，key对应archive中的字段名，value为显示的字段名
			'armyId': 'ArmyId',
			'gid'   : '武将id',
			'name'  : '武将名',
		},
		'detail': {
			'generalId': '武将id',
			'name': '名称',
			'att': '攻击力',
		}
	},
	'buildings': {
		# 需要和archive中的字段名匹配
		'brief' : {
			# 主面板显示的信息，key对应archive中的字段名，value为显示的字段名
			'bid'   : '建筑id',
			'name'  : '建筑名',
		},
		'detail': {
			'generalId': '武将id',
			'name': '名称',
			'att': '攻击力',
		}
	},
	'slave_buildings': {
		# 需要和archive中的字段名匹配
		'brief' : {
			# 主面板显示的信息，key对应archive中的字段名，value为显示的字段名
			'x'  : '建筑id',
			'y'  : '建筑名',
			'hp' : '兵力',
		},
	},
}