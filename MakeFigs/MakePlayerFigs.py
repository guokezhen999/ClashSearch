import datetime

import matplotlib.pyplot as plt

from MakeFigs import *
from LocalClasses.LocalPlayer import LocalPlayer
from Accounts.ClashDatabase import ClashDatabase
from BasicData.SelectMode import PlayerType

# 设置 Matplotlib 样式
plt.style.use('seaborn-v0_8-darkgrid')

# 这里使用一个列表，Matplotlib会尝试列表中的字体，直到找到一个可用的。
plt.rcParams['font.sans-serif'] = [
            'PingFang SC', # macOS 苹方简
            'Heiti SC',    # macOS 黑体简
            'Arial Unicode MS', # 广泛支持多语言的字体
            'SimHei',      # Windows 黑体
            'Microsoft YaHei', # Windows 微软雅黑
            'WenQuanYi Zen Hei' # Linux 文泉驿正黑
        ]# 解决负号 '-' 显示为方块的问题，或者不正确显示的问题
plt.rcParams['axes.unicode_minus'] = False



class MakePlayerFigs():
    def __init__(self, players: list[LocalPlayer], database: ClashDatabase, playerType: PlayerType):
        self.players = players
        self.database = database
        self.playerType = playerType

        self.infos = []
        self.playerTags = [player.getInfo("Tag") for player in players]

    def processData(self) -> list[tuple[str, list[datetime.date], dict[str, list]]]:
        playerTagDict = {}
        for player in self.players:
            playerTagDict[player.getInfo("Tag")] = player.getInfo("Name")
        datas = self.database.getPlayerInfoTrack(self.playerType, self.playerTags, self.infos)
        returnList = []
        for key in datas:
            data = datas[key]
            dates = []
            name = playerTagDict[key]
            picData = [[] for i in range(len(data[0]) - 1)]
            for combo in data:
                dates.append(combo[0])
                for j, info in enumerate(combo[1:]):
                    picData[j].append(info)
            picInfoDict = {}
            for i, info in enumerate(self.infos):
                picInfoDict[info] = picData[i]
            returnList.append((name, dates, picInfoDict))
        print(returnList)
        return returnList

    def makeFig(self):
        filePaths = []
        if self.playerType == PlayerType.MY_PLAYER:
            dir = "pictures/figures/myPlayers/"
        elif self.playerType == PlayerType.FOCUS_PLAYER:
            dir = "pictures/figures/focusPlayers/"
        elif self.playerType == PlayerType.ROBOT:
            dir = "pictures/figures/robots/"
        else:
            return [] # 如果没有匹配的类型，返回空列表而不是None

        datas = self.processData()
        names = []
        xData = []
        yData = {}
        for info in self.infos:
            yData[info] = []
        for data in datas:
            names.append(data[0])
            xData.append(data[1])
            for info in self.infos:
                yData[info].append(data[2][info])
        print(yData)
        nameFile = ""
        for name in names:
            nameFile += f"_{name}"
        today = datetime.datetime.now().date()

        for i, info in enumerate(self.infos):
            plt.figure(i, figsize=(12.0, 4.8))

            # --- 计算当前图表所有线的Y值范围，用于确定动态偏移量 ---
            all_y_values_for_current_info = []
            for y_line_data in yData[info]:
                all_y_values_for_current_info.extend(y_line_data)

            if len(all_y_values_for_current_info) > 1:
                min_y = np.min(all_y_values_for_current_info)
                max_y = np.max(all_y_values_for_current_info)
                y_range = max_y - min_y
                # 如果Y范围太小（比如所有值都相同），设置一个默认的最小范围，避免除以零或过小的偏移
                if y_range == 0:
                    y_range = np.mean(all_y_values_for_current_info) * 0.1 if np.mean(
                        all_y_values_for_current_info) != 0 else 1.0
                # 基础偏移量，通常是Y轴范围的1%到3%
                base_vertical_offset_unit = y_range * 0.02
            else:  # 如果只有一条线或没有数据，则使用默认的固定偏移
                base_vertical_offset_unit = 0.05  # 一个合理的默认值

            # 确保即使在极端情况下也有一个合理的最小偏移
            if base_vertical_offset_unit < 0.05:
                base_vertical_offset_unit = 0.05

            # --- 优化文本标注部分 ---
            for j in range(len(xData)):
                x = xData[j]
                y = yData[info][j]
                plt.plot(x, y, label=names[j])

                lastB = None
                last_labeled_idx = -1
                max_labels_per_line = 15
                # 动态调整标注间隔，避免过密
                label_interval_points = max(1, len(x) // max_labels_per_line)

                # 为每条线计算一个独特的垂直偏移系数
                # 奇数线向上，偶数线向下，并逐渐增加偏移量，以避免相互遮挡
                # 例如：线0: +1, 线1: -1, 线2: +2, 线3: -2, 线4: +3, 线5: -3 ...
                vertical_offset_factor = (j % 2 * 2 - 1) * (j // 2 + 1)

                # 最终的垂直偏移量
                dynamic_vertical_offset = base_vertical_offset_unit * vertical_offset_factor

                for k, (a, b) in enumerate(zip(x, y)):
                    should_label = False

                    # 1. 总是标注第一个点
                    if k == 0:
                        should_label = True
                    # 2. 总是标注最后一个点
                    elif k == len(x) - 1:
                        should_label = True
                    # 3. 如果Y值发生变化 并且 距离上次标注的点有足够的距离
                    elif lastB is not None and lastB != b:
                        if (k - last_labeled_idx) >= label_interval_points:
                            should_label = True
                    # 4. 如果是长线条且数值变化不大，确保每隔一段时间也有标签
                    elif (k - last_labeled_idx) >= label_interval_points * 2:  # 比常规间隔更大一些
                        should_label = True

                    if should_label:
                        # 使用动态计算的偏移量
                        plt.text(a, b + dynamic_vertical_offset, '%.0f' % b, ha='center',
                                 va='bottom' if dynamic_vertical_offset >= 0 else 'top', fontsize=9)
                        last_labeled_idx = k  # 更新最后被标注的点的索引

                    lastB = b  # 更新lastB为当前Y值，用于下次迭代比较
            # --- 优化文本标注结束 ---

            plt.legend(loc='best')
            plt.title(f"{info.replace('.', '')} 数据趋势")
            plt.xlabel("时间点")
            plt.ylabel(f"{info} 数值")

            filePath = f"{dir}{info.replace('.', '')}{nameFile}_{today}.png"
            plt.savefig(filePath)
            plt.close()
            filePaths.append(filePath)
        return filePaths

