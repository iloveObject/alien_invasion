#
# Mr.peng--2021/3/13 8:19 下午

class Settings:
    """存储游戏《w外星人入侵》中所有设置表"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # 设置飞船速度
        self.ship_speed = 1.5
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        

