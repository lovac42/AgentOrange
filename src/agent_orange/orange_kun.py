# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/AgentOrange
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.3


# Use Refuzz?
REFUZZ = True

# If current card's ivl is the max ivl,
# the next ivl will be 100% of current ivl,
# or no fuzz. This causes all cards to be stacked
# on the same date. So we remove this constrain,
# and allow for backwards fuzzing when there is an
# overflow. Forwards fuzzing is still capped at max ivl.



import anki
import random
from aqt import mw
from anki.hooks import wrap
from anki.sched import Scheduler
from anki.schedv2 import Scheduler as SchedulerV2


overflow=None


def wrap_fuzzIvlRange(sched, ivl, _old):
    global overflow
    overflow=None

    ret=_old(sched,ivl) #invoke defuzz
    card=mw.reviewer.card
    if card:
        # print("using agent orange")

        # fix uneven distribution caused by constrain
        mi=max(1,card.ivl+1,ret[0])
        mx=min(sched._revConf(card)['maxIvl'],ret[1])
        if mx<=mi:
            overflow=ret
            mi=mx
        return [mi,mx]
    return ret

Scheduler._fuzzIvlRange=wrap(Scheduler._fuzzIvlRange,wrap_fuzzIvlRange,"around")
SchedulerV2._fuzzIvlRange=wrap(SchedulerV2._fuzzIvlRange,wrap_fuzzIvlRange,"around")



def wrap_updateRevIvl(sched, card, ease):
    if overflow:
        cap=sched._revConf(card)['maxIvl']
        mi=max(min(overflow[0],cap-2),1)
        card.ivl=random.randint(mi,cap)

if REFUZZ:
    Scheduler._updateRevIvl=wrap(Scheduler._updateRevIvl,wrap_updateRevIvl,"after")
    SchedulerV2._updateRevIvl=wrap(SchedulerV2._updateRevIvl,wrap_updateRevIvl,"after")
