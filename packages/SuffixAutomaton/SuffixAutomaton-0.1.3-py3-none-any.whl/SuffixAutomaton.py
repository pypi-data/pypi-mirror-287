import math
import collections
import copy
from typing import List, Dict, OrderedDict

import logging

# logger = logging.getLogger("SuffixAutomaton")
logger = logging.getLogger()
logger.propagate = False
logger.handlers.clear()
logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler("log.txt")
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s- %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter(
    "%(asctime)s- %(filename)s - %(lineno)d - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


class State:
    def __init__(
        self, position: int = -1, length: int = 0, next=None, link: int = 0
    ) -> None:
        self.position = position  # in line
        self.length = length  # max_len
        self.link = link  # back
        if not next:
            next = {}
        self.next = next  # transation


class SuffixAutomaton:
    def __init__(self, line: List[str]) -> None:
        # self.sequence = [x for x in line if x]
        self.sequence = line
        self.last = 0
        self.size = 1
        nodes = [None for _ in range(2 * len(self.sequence) + 3)]
        nodes[0] = State(link=-1)
        # nodes[0].link=-1
        for i, x in enumerate(self.sequence):
            nodes = self.insert(i, x, nodes)
        self.nodes = nodes[: self.size]

    def insert(self, position: int, token: str, nodes: List[State]):
        current = self.size
        self.size += 1
        # new
        nodes[current] = State(position=position, length=nodes[self.last].length + 1)
        logger.debug(f"状态{current}添加到后缀自动机")
        logger.debug(f"上一个节点状态是{self.last}")
        logger.debug(f"状态{current}的长度是{nodes[self.last].length + 1}")

        # 如果后缀自动机最近转移里面没有当前字符，则添加该字符，并将状态指向当前状态 继续沿着后缀连接走，进行上述操作直到到达第一个状态或者转移中有此字符
        p = self.last
        while p >= 0 and token not in nodes[p].next:
            logger.debug(
                f"状态{p}的转移:{self._dict2str(nodes[p].next)}{('','不')[nodes[p].next.get(token) is None]}包含字符{token}"
            )
            nodes[p].next[token] = current
            logger.debug(f"把{token}添加进状态{p}的转移")
            logger.debug(f"开始查找状态{p}的后缀链接...")
            p = nodes[p].link
            logger.debug(f"后缀链接为状态{p}")
        # 如果后缀链接走到底了，没有相同的，则后缀链接指向0状态，即空字符串
        if p == -1:
            nodes[current].link = 0
        # 如果找到上一状态的转移里有c字符,找到转移c的另一状态
        else:
            q = nodes[p].next[token]
            logger.debug(f"在状态{p}的转移中找到了字符{token}，{token}指向状态{q}")
            # 如果q状态与p状态相连，则当前状态的后缀链接指向q状态
            if nodes[p].length + 1 == nodes[q].length:
                nodes[current].link = q
                logger.debug(
                    f"状态{p}的长度比状态{q}少1，把当前状态{current}的后缀链接指向状态{q}"
                )
            # 如果不相连则开一个新状态,长度为p状态的下一个状态，后缀链接与转移指向q
            else:  # new
                clone = self.size
                logger.debug(f"状态{p}的长度与状态{q}的长度不连续，新建状态{self.size}")
                self.size += 1
                nodes[clone] = State(
                    position=position,
                    length=nodes[p].length + 1,
                    next=copy.deepcopy(nodes[q].next),
                    link=nodes[q].link,
                )
                logger.debug(f"新状态{self.size}的长度为状态{p}的长度加1")
                # 搜索状态p，若c转移为q，则指向新状态，并搜索后缀链接的状态重复指向新状态 直到状态转移不为q，跳出
                while p != -1 and nodes[p].next[token] == q:
                    logger.debug(
                        f"状态{p}转移中{token}的转移是状态{q},把指向{q}的转移改为指向新状态{self.size}"
                    )
                    nodes[p].next[token] = clone
                    logger.debug(f"查找状态{p}的后缀链接...")
                    p = nodes[p].link
                    logger.debug(f"后缀链接为状态{p}")
                # 把当前状态与q的后缀链接指向新状态
                nodes[q].link = nodes[current].link = clone
                logger.debug(
                    f"把状态{q}与当前状态{current}的后缀链接指向新状态{self.size}"
                )
        logger.debug(f"当前状态{current}的长度为:{nodes[current].length}")
        logger.debug(f"当前状态{current}的后缀链接为:{nodes[current].link}")
        logger.debug(f"当前状态{current}的转移为:{self._dict2str(nodes[current].next)}")
        logger.debug(f"当前状态{current}建立完成")
        # 状态索引占位
        self.last = current
        return nodes

    @staticmethod
    def _dict2str(dct):
        return " ".join(f"{k}->{w}" for k, w in dct.items())

    def __str__(self):
        pts = ""
        for k, w in enumerate(self.nodes):
            pts += f"状态{k}: 长度:{w.length}  后缀链接-->{w.link}  转移:{self._dict2str(w.next)}\n"
        return pts

    def sub_seq(self, endpos, length, output_lcs=True):
        """
        output_lcs=False for faster and saving memory
        """
        pos = self.nodes[endpos].position
        start = pos + 1 - length
        T = None
        if output_lcs:
            T = self.sequence[start : pos + 1]
        return start, T

    def lcs1(self, t: List[str], min_len: int = -1, output_lcs=True):
        """
        return [(lcs:str, start:int, cand_start:int)]
        default min_len=-1, then return longest one
        """
        p = 0  # 当前节点
        length = 0  # 当前
        longest = 0  # 全局
        cands = [None] * len(self.nodes)  # 候选
        for i, x in enumerate(t):
            if x in self.nodes[p].next:  # 匹配
                cands[p] = None
                p = self.nodes[p].next[x]
                length += 1
            else:  # 失配
                while p != -1 and x not in self.nodes[p].next:
                    p = self.nodes[p].link
                if p == -1:  # 从头再来
                    p = 0
                    length = 0
                else:  # 止步
                    length = self.nodes[p].length + 1
                    cands[p] = None
                    p = self.nodes[p].next[x]
            if length > 0:
                longest = max(longest, length)
                endpos = p
                cand_start = i - length + 1
                if cands[p] and cands[p][1] >= length:
                    continue
                cands[p] = (endpos, length, cand_start)

        if min_len <= 0:
            min_len = max(1, longest)
        cands = [x for x in cands if x]
        ans = []
        for endpos, length, cand_start in cands:
            if length >= min_len:
                (start, T) = self.sub_seq(endpos, length, output_lcs)
                if ans and start <= ans[-1][1]:
                    ans[-1] = (start, length, cand_start, T)
                else:
                    ans.append((start, length, cand_start, T))
        return ans

    def lcs2(self, doc: List[List[str]], min_len: int = -1, output_lcs=True):
        """
        return [(lcs:str, start:int, cand_start:int)]
        default min_len=-1, then return longest one

        # 计数排序 https://www.cnblogs.com/xiaochuan94/p/11198610.html
        # 按照可能匹配串的长度降序，匹配成功向上传递，用以优化效率
        # count = [0]*(len(self.sequence)+1)
        """
        count = [0] * self.size
        for i in range(1, self.size):
            count[self.nodes[i].length] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        result = [0] * self.size
        for i in range(self.size - 1, 0, -1):
            result[count[self.nodes[i].length]] = i
            count[self.nodes[i].length] -= 1
        lengths = [x.length for x in self.nodes]  # 起始该节点全匹配
        for t in doc:
            result, lengths = match(self, t, result, lengths)

        longest = max(lengths)
        if min_len <= 0:
            min_len = max(1, longest)
        ans = []
        for endpos, length in enumerate(lengths):
            if length >= min_len:
                (start, T) = self.sub_seq(endpos, length, output_lcs)
                if ans and start <= ans[-1][0]:
                    ans[-1] = (start, length, T)
                else:
                    ans.append((start, length, T))
        return ans


def sam_lcs1(sam: SuffixAutomaton, t: List[str], min_len: int = -1, output_lcs=True):
    return sam.lcs1(t, min_len, output_lcs)


def lcs1(s: List[str], t: List[str], min_len: int = -1, output_lcs=True):
    sam = SuffixAutomaton(s)
    re = sam_lcs1(sam, t, min_len, output_lcs)
    return re


def match(sam, t, result, lengths):
    now = [0] * sam.size  # 当前匹配长度
    tmp = 0  # 当前长度
    p = 0  # 起始节点
    for i, token in enumerate(t):
        if token in sam.nodes[p].next:  # 匹配
            tmp += 1
            p = sam.nodes[p].next[token]
            now[p] = max(tmp, now[p])
        else:  # 尽力
            while p >= 0 and token not in sam.nodes[p].next:
                p = sam.nodes[p].link
            if p >= 0 and token in sam.nodes[p].next:  # 继承
                tmp = sam.nodes[p].length + 1
                p = sam.nodes[p].next[token]
                now[p] = max(tmp, now[p])
            else:  # 从头再来
                tmp = p = 0

    for i in range(sam.size - 1, 0, -1):
        v = result[i]
        fa = sam.nodes[v].link
        if fa >= 0:
            now[fa] = max(now[fa], min(sam.nodes[fa].length, now[v]))
    for i in range(sam.size - 1, 0, -1):
        lengths[i] = min(lengths[i], now[i])
    return result, lengths


def sam_lcs2(
    sam: SuffixAutomaton, doc: List[List[str]], min_len: int = -1, output_lcs=True
):
    return sam.lcs2(doc, min_len, output_lcs)


def lcs2(query: List[str], doc: List[List[str]], min_len: int = -1, output_lcs=True):
    sam = SuffixAutomaton(query)
    re = sam_lcs2(sam, doc, min_len, output_lcs)
    return re


if __name__ == "__main__":
    # http://123.57.137.208/ccf/ccf-4.jsp
    raw = """
    ASE : International Conference on Automated Software Engineering
    ESEC/FSE : ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering
    ICSE : International Conference on Software Engineering
    ISSTA : The International Symposium on Software Testing and Analysis
    OOPSLA : Conference on Object-Oriented Programming Systems, Languages, and Applications
    OSDI : Operating Systems Design and Implementation
    PLDI : ACM SIGPLAN conference on Programming Language Design and Implementation
    POPL : ACM SIGACT-SIGPLAN Symposium on Principles of Programming Languages
    SOSP : ACM Symposium on Operating Systems Principles
    """
    doc = raw.strip().splitlines()
    doc = [x.split() for x in doc]
    # for tokens
    logger.info(lcs1(doc[1], doc[2]))  # [(14, 2, 5, ['Software', 'Engineering'])]
    logger.info(lcs2(doc[0], doc[1:4]))  # [(1, 1, [':']), (4, 1, ['on']), (6, 1, ['Software'])]
    logger.info(lcs1(doc[1], doc[2], 1)) # [(1, 1, 1, [':']), (7, 1, 3, ['Conference']), (10, 1, 4, ['on']), (14, 2, 5, ['Software', 'Engineering'])]
    logger.info(lcs2(doc[0], doc[1:4], 1)) # [(1, 1, [':']), (4, 1, ['on']), (6, 1, ['Software'])]
    logger.info(lcs2(doc[0], doc[1:4], 1, output_lcs=False)) # [(1, 1, None), (4, 1, None), (6, 1, None)]

    # for chars
    poet = "江天一色无纤尘皎皎空中孤月轮 江畔何人初见月江月何年初照人 人生代代无穷已江月年年望相似 不知江月待何人但见长江送流水"
    doc = poet.split()   
    logger.info(lcs1(doc[1], doc[3]))  #  [(2, 2, 5, '何人'), (7, 2, 2, '江月')]
    logger.info(lcs1(doc[1], doc[3], 1)) # [(0, 1, 10, '江'), (2, 2, 5, '何人'), (5, 1, 8, '见'), (7, 2, 2, '江月')]
    # for lcs of doc
    logger.info(lcs2(doc[2], doc[2:4]))  # [(7, 2, '江月')]
    logger.info(lcs2(doc[2], doc[2:4], 1)) # [(0, 1, '人'), (7, 2, '江月')]
    # faster when iterally
    sam = SuffixAutomaton(doc[0])
    for x in doc[1:]:
        print((x, sam.lcs1(x)))
    """
    ('江畔何人初见月江月何年初照人', [(0, 1, 0, '江'), (12, 1, 6, '月')])
    ('人生代代无穷已江月年年望相似', [(0, 1, 7, '江'), (4, 1, 4, '无'), (12, 1, 8, '月')])
    ('不知江月待何人但见长江送流水', [(0, 1, 2, '江'), (12, 1, 3, '月')])
    """

    # lcs() -> [(str, start, cand_start)], sort in length decending. may overlap. 
    logger.info(lcs2("布架 拖把抹布悬挂沥水洁具架 ", ["抹布架"], 1))  # [(0, 2, '布架'), (5, 2, '抹布'), (13, 1, '架')]
