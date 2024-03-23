import json

result_map = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
}

achieve_map: list = json.load(
    open('Data/_ExcelBinOutput/AchievementExcelConfigData.json', encoding='utf-8'))
daily_task_map: list = json.load(
    open('Data/_ExcelBinOutput/DailyTaskExcelConfigData.json', encoding='utf-8'))

filtered_achieve_map = list(filter(
    lambda x: x['TriggerConfig']['TriggerType'] in ['FinishQuestAnd', 'FinishQuestOr', 'DailyTaskVarEqual', 'FinishParentQuestAnd'], achieve_map))

for achievement in filtered_achieve_map:
    if achievement['TriggerConfig']['TriggerType'] in ['FinishQuestAnd', 'FinishQuestOr']:
        a = next((task for task in daily_task_map if str(task['QuestId'])[:-2] == (achievement['TriggerConfig']['ParamList'][0]).split(",")[0][:-2]), None)
        if a:
            result_map[a['CityId']].append(achievement['Id'])
    elif achievement['TriggerConfig']['TriggerType'] == 'DailyTaskVarEqual':
        a = next((task for task in daily_task_map if str(task['Id']) == achievement['TriggerConfig']['ParamList'][0]), None)
        if a:
            result_map[a['CityId']].append(achievement['Id'])
    elif achievement['TriggerConfig']['TriggerType'] == 'FinishParentQuestAnd':
        a = next((task for task in daily_task_map if str(task['QuestId'])[:-2] == achievement['TriggerConfig']['ParamList'][0]), None)
        if a:
            result_map[a['CityId']].append(achievement['Id'])
    else:
        raise Exception('Impossible')

print(json.dumps(result_map, indent=4))

# Exceptions
#
# Liyue
# 84506 QuestGlobalVarEqual
#
# Inazuma
# 84536 FinishQuestAnd
# 84541 FinishQuestAnd
# 84542 FinishQuestAnd
# 84552 FinishQuestAnd
#
# Sumeru
# 84543 QuestGlobalVarEqual
# 84550 GroupNotify
