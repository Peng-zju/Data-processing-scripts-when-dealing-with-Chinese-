
class Money:
    CN_NUM = {
        u'〇' : 0,
        u'一' : 1,
        u'二' : 2,
        u'三' : 3,
        u'四' : 4,
        u'五' : 5,
        u'六' : 6,
        u'七' : 7,
        u'八' : 8,
        u'九' : 9,

        u'零' : 0,
        u'壹' : 1,
        u'贰' : 2,
        u'叁' : 3,
        u'肆' : 4,
        u'伍' : 5,
        u'陆' : 6,
        u'柒' : 7,
        u'捌' : 8,
        u'玖' : 9,

        u'貮' : 2,
        u'两' : 2,
    }

    CN_UNIT = {
        u'十' : 10,
        u'拾' : 10,
        u'百' : 100,
        u'佰' : 100,
        u'千' : 1000,
        u'仟' : 1000,
        u'万' : 10000,
        u'萬' : 10000,
        u'亿' : 100000000,
        u'億' : 100000000,
        u'兆' : 1000000000000,
    }
    
    def convertCNToDigit(raw_money):
        '''
        将万级以下的中文数字转化为阿拉伯数字
        eg: 一千二百零三 --> 1203
        digital: 数字
        unit: 单位 eg: 1 10(十) 100(百) 1000(千) 10000(万) ...
        '''
        i = 0
        money = 0
        while i < len(raw_money):
            digital = Money.CN_NUM.get(raw_money[i])
            if digital == 0:  # eg:一百零一的零
                i += 1
                continue
            if not digital:  # digital == None  eg: 十一  一百十三的十
                if Money.CN_UNIT.get(raw_money[i]) == 10:
                    digital = 1
                    unit = 10
                    money = money + digital * unit
                    i += 1
                    continue
            if i < len(raw_money) - 1:
                unit = Money.CN_UNIT.get(raw_money[i+1])
            else:
                unit = 1  # 末尾
            money = money + digital * unit
            i += 2

        return money
    
    def handleRawMoney(raw_money):
        '''
        返回以万为单位的数值
        举例:
        80000 --> 8
        8万 --> 8
        24.387万 --> 24.387
        u'一千二百零三' --> 0.1203
        玖仟叁佰元 --> 0.93
        叁万伍仟陆佰柒拾肆 --> 3.5674
        '''
        if raw_money:
            raw_money = raw_money.strip()
            raw_money = raw_money.replace(u'萬', u'万').replace(u'億', u'亿').replace(u'元', '')
        else:
            return None

        # 纯数字的情况
        try:
            money = float(raw_money)
        except:
            pass
        else:
            return money/10000

        # 以万单位结尾的纯数字情况  eg: 8.2万 --> 8.2
        if raw_money[-1] == u'万':
            try:
                money = float(raw_money[:-1])
            except:
                pass
            else:
                return money

        # 先将汉字数字拆分成[亿, 万, 个]  举例: 一千一百二十三万四千五百六十七 拆分成 ['一千一百二十三','四千五百六十七']
        raw_money_split = []
        if u'亿' in raw_money:
            raw_money_split.append(raw_money.split(u'亿')[0])
            raw_money = raw_money.split(u'亿')[1]
        else:
            raw_money_split.append(None)

        if u'万' in raw_money:
            raw_money_split.append(raw_money.split(u'万')[0])
            raw_money_split.append(raw_money.split(u'万')[1])
        else:
            raw_money_split.append(None)
            raw_money_split.append(raw_money)

        money = 0
        for r in raw_money_split:
            if r:
                if raw_money_split.index(r) == 0:  # 亿
                    money = money + Money.convertCNToDigit(r)*Money.CN_UNIT.get(u'亿')
                if raw_money_split.index(r) == 1:  # 万
                    money = money + Money.convertCNToDigit(r)*Money.CN_UNIT.get(u'万')
                if raw_money_split.index(r) == 2:  # 个
                    money = money + Money.convertCNToDigit(r)

        if money:
            return float(money)/10000
        else:
            return None

