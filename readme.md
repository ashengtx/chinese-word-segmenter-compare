# Chinese Word Segment

## Segmenters

- [jieba](https://github.com/fxsjy/jieba)
- [pkuseg](https://github.com/lancopku/pkuseg-python)
- [THULAC](https://github.com/thunlp/THULAC-Python)
- [pynlpir](https://github.com/tsroten/pynlpir)
- [pyhanlp](https://github.com/hankcs/pyhanlp)


## Usage 

- Use virtualenv
```
sudo virtualenv venv -p python3.6
source venv/bin/activate
```

- Install packages
```
pip install -r requirements.txt
```

- Result

```
$ python compare.py
jieba: 你 是 天边 最美 的 云彩
pkuseg: 你 是 天边 最 美的 云彩
thulac: 你 是 天边 最 美 的 云彩
pynlpir: 你 是 天边 最 美 的 云彩
pyhanlp: 你 是 天边 最美 的 云彩

jieba: 我 也 想 过 过 过儿 过过 的 生活
pkuseg: 我 也 想 过过 过儿 过过 的 生活
thulac: 我 也 想 过 过 过儿 过 过 的 生活
pynlpir: 我 也 想 过 过 过 儿 过 过 的 生活
pyhanlp: 我 也 想 过过 过 儿 过过 的 生活

jieba: 我 也 想 看看 看看 看过 的 世界
pkuseg: 我 也 想 看看 看看 看 过 的 世界
thulac: 我 也 想 看 看看 看看 过 的 世界
pynlpir: 我 也 想 看看 看看 看 过 的 世界
pyhanlp: 我 也 想 看看 看看 看过 的 世界
```

## Note

- for `pynlpir`, run `pynlpir update` to download the latest license.
- `pyhanlp` need jdk.