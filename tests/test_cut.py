import jieba
import jieba.posseg as pseg
import json

jieba.load_userdict('ctc_dict.txt')
jieba.initialize()
sentence = '9月的东区电信局在网用户数'

words = pseg.cut(sentence)
js = {}
condition = []
groupBy = []
target = []
for word, flag in words:

    if not flag.startswith('type'):
        continue

    for tags in flag.split('z'):  # tags: typexconditionz keyxdept    typextarget
        key_value = tags.split('x')
        # for tag in tags.split('x'):
        if key_value[0] == 'type':
            if key_value[1] == 'target':
                target.append(word)
        elif key_value[0] == 'key':

            condition.append({'key': key_value[1], 'value': word, 'relation': '='})
        elif key_value[0] == 'groupBy':

            groupBy.append({'value': key_value[1]})
js['target'] = target
js['condition'] = condition
js['groupBy'] = groupBy

print(json.dumps(js, ensure_ascii=False))
