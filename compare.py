msg = [
        "你是天边最美的云彩",
        "我也想过过过儿过过的生活",
        "我也想看看看看看过的世界"
        ]

# jieba
import jieba
# pkuseg
import pkuseg
pku_seg = pkuseg.pkuseg()
# thulac
import thulac
thu_seg = thulac.thulac(seg_only=True)
# pynlpir
import pynlpir
pynlpir.open()


segmenter_map = {
    'jieba': jieba,
    'pkuseg': pku_seg,
    'thulac': thu_seg,
    'pynlpir': pynlpir
}

def segmenter_by_key(seg_key, sent):
    """
    return word list
    """
    segmenter = segmenter_map[seg_key]
    if seg_key == "thulac":
        result = segmenter.cut(sent, text=True).split()
    elif seg_key == "pynlpir":
        result = segmenter.segment(sent, pos_tagging=False)
    else:
        result = segmenter.cut(sent)
    return list(result)

# compare segment result
for sent in msg:
    for seg_key in segmenter_map:
        words = segmenter_by_key(seg_key, sent)
        print(seg_key+':'+' '.join(words))
    print()


