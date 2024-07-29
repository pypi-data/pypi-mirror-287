import csv
from collections import defaultdict

class frequenciesOfItems:
    def __init__(self, database_path, separator='\t'):
        self.database_path = database_path
        self.separator = separator
        self.frequencies = defaultdict(int)

    def getFrequencies(self):
        # データベースファイルを読み込み
        with open(self.database_path, 'r') as file:
            reader = csv.reader(file, delimiter=self.separator)
            for row in reader:
                for item in row:
                    if item:  # 空のアイテムをスキップ
                        self.frequencies[item] += 1
        return dict(self.frequencies)

# 使用例
if __name__ == "__main__":
    # トランザクショナルデータベースのパスとセパレータを指定してインスタンスを作成
    itemsFrequencies = frequenciesOfItems('/Users/satochihiro/Downloads/Transactional_T10I4D100K.csv', '\t')
    # アイテムの頻度を取得
    itemsFreqDictionary = itemsFrequencies.getFrequencies()
    # 辞書を表示
    print(itemsFreqDictionary)
