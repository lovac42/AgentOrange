# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/AgentOrange
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1


from aqt import mw

def test_distribution_probability(grade):
    assert 2 <= grade <=4
    if mw.state!='review':
        print('This must be run in the Reviewer')
        return

    card=mw.reviewer.card
    old_ivl=card.ivl
    dict={}
    for i in range(10000):
        mw.col.sched._updateRevIvl(card,grade)
        nx=card.ivl
        dict[nx]=dict.get(nx,0)+1
        card.ivl=old_ivl

    for k,v in sorted(dict.items()):
        print("%d: %0.2f%%"%(k,v/100))

mw.test_distribution_probability=test_distribution_probability
