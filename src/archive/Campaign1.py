{
	'campId': 1,
	'mapId' : 10001,
	'intro' : '',
	'conf'  : [
		{
			'player': {
				'campPid'  : 0,
				'name'	   : 'player',
				'x'		   : 1,
				'y'		   : 2,
				'top'      : 5,
				'bottom'   : 4,
				'left'     : 3,
				'right'    : 4,
				'initFood' : 100,
				'initWood' : 100,
				'accFood'  : 10,
				'accWood'  : 10,
			},

			'generals': [
				{
					'armyId': 1,
					'gid'   : 16,
					'lv'    : 1,
					'name'  : '关羽',
					'att'   : 200,
					'def'   : 0,
					'hp'    : 1100,
					'speed' : 1,
					'init'  : 0,
				},
				{
					'armyId': 2,
					'gid'   : 17,
					'lv'    : 1,
					'name'  : '张飞',
					'att'   : 200,
					'def'   : 0,
					'hp'    : 1100,
					'speed' : 1,
					'init'  : 0,
				},
			],

			'buildings': [
				{
					'bid'    : 1,
					'name'   : '主城',
					'lv'  	 : 8,
					'lvNeed' : 1,
				},
				{
					'bid'    : 2,
					'name'   : '民居',
					'lv'     : 1,
					'lvNeed' : 1,
				},
			],

			'slave_buildings': [
				{
					'x':  62,
					'y':  63,
					'hp': 100,
				},
				{
					'x':  32,
					'y':  23,
					'hp': 100,
				},
			],
		},
		{
			'player': {
				'campPid': 1,
				'name'	 : 'player1',
				'x'		 : 2,
				'y'		 : 3,
			},

			'generals': [
				{
					'armyId': 1,
					'gid'   : 18,
					'lv'    : 1,
					'name'  : '刘备',
				},
				{
					'armyId': 2,
					'gid'   : 19,
					'lv'    : 1,
					'name'  : '诸葛亮',
				},
			],

			'buildings': [
				{
					'bid' : 1,
					'name': '主城',
					'lv'  : 8,
				},
				{
					'bid' : 2,
					'name': '民居',
					'lv'  : 1,
				},
			],

			'slave_buildings': [
				{
					'x':  26,
					'y':  15,
					'hp': 200,
				},
				{
					'x':  42,
					'y':  5,
					'hp': 200,
				},
			],
		},
	],
}