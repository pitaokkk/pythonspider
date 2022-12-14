import jieba
from wordcloud import WordCloud

def chinese_jieba(txt):
    wordlist_jieba = jieba.lcut(txt) # 将文本分割，返回列表
    txt_jieba = " ".join(wordlist_jieba) # 将列表拼接为以空格为间断的字符串
    return txt_jieba

#stopwords = ['这些', '那些', '因为', '所以'] # 噪声词
stopwords=open('./chinesestopwords.txt','r',encoding='gb18030').read().split()

with open(r'./young.txt',encoding='gb18030') as fp:
    txt = fp.read()
    txt = chinese_jieba(txt)
    wordcloud = WordCloud(font_path = './simhei.ttf', # 字体
                          background_color = 'black', # 背景色
                          max_words = 30, # 最大显示单词数
                          max_font_size = 60, # 频率最大单词字体大小
                          stopwords = stopwords # 过滤噪声词
                        ).generate(txt)
    image = wordcloud.to_image()
    image.show()