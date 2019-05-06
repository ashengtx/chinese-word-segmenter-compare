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


segmenter_map = {
    'jieba': jieba,
    'pkuseg': pku_seg,
    'thulac': thu_seg
}

def segmenter_by_key(seg_key, sent):
    """
    return word list
    """
    segmenter = segmenter_map[seg_key]
    if seg_key == "thulac":
        return segmenter.cut(sent, text=True).split()
    return list(segmenter.cut(sent))

# compare segment result
for sent in msg:
    for seg_key in segmenter_map:
        words = segmenter_by_key(seg_key, sent)
        print(seg_key+':'+' '.join(words))
    print()


