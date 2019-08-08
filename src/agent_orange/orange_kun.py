# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/AgentOrange
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.2


import anki
from aqt import mw
from anki.hooks import wrap
from anki.sched import Scheduler
from anki.schedv2 import Scheduler as SchedulerV2


def wrap_fuzzIvlRange(sched, ivl, _old):
    ret=_old(sched,ivl) #invoke defuzz
    card=mw.reviewer.card
    if card:
        # print("using agent orange")

        # fix uneven distribution caused by constrain
        mi=max(1,card.ivl+1,ret[0])
        mx=min(sched._revConf(card)['maxIvl'],ret[1])
        return [mi if mi<mx else mx,mx]
    return ret

Scheduler._fuzzIvlRange=wrap(Scheduler._fuzzIvlRange,wrap_fuzzIvlRange,"around")
SchedulerV2._fuzzIvlRange=wrap(SchedulerV2._fuzzIvlRange,wrap_fuzzIvlRange,"around")

#TODO:
# allow backwards fuzz by 1% when max cap is reached.
# wrap _updateRevIvl
