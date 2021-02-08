# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_fetch_illustration 1'] = GenericRepr('<Illustration id=86979680 user=wlop>')

snapshots['test_fetch_illustration_comments 1'] = {
    'comments': [
        GenericRepr('<Comment id=112771847 user=Neptunes>'),
        GenericRepr('<Comment id=112589345 user=Qimo>'),
        GenericRepr('<Comment id=112555672 user=昔人>'),
        GenericRepr('<Comment id=112513468 user=xi ix>'),
        GenericRepr('<Comment id=112451838 user=Hasoya>'),
        GenericRepr('<Comment id=112427689 user=sywx>'),
        GenericRepr('<Comment id=112411403 user=sss>'),
        GenericRepr('<Comment id=112395755 user=adamfitzwate884>'),
        GenericRepr('<Comment id=112392972 user=Byron68405>'),
        GenericRepr('<Comment id=112389725 user=小鳄>'),
        GenericRepr('<Comment id=112388118 user=derricktanks239>'),
        GenericRepr('<Comment id=112388027 user=パラパラ>'),
        GenericRepr('<Comment id=112387293 user=joehorn678834>'),
        GenericRepr('<Comment id=112387046 user=marlongoetsc664>'),
        GenericRepr('<Comment id=112385969 user=iragleason57692>'),
        GenericRepr('<Comment id=112383962 user=西莉卡>'),
        GenericRepr('<Comment id=112383100 user=師臣-明遠>'),
        GenericRepr('<Comment id=112375512 user=guzhaoyuan>'),
        GenericRepr('<Comment id=112372917 user=Stacy90193>'),
        GenericRepr('<Comment id=112371510 user=Pamela72162>'),
        GenericRepr('<Comment id=112371243 user=Christine22848>'),
        GenericRepr('<Comment id=112369699 user=趋心若鹜>'),
        GenericRepr('<Comment id=112367280 user=milesmonroe8670>'),
        GenericRepr('<Comment id=112355021 user=眼镜猫>'),
        GenericRepr('<Comment id=112348504 user=578778152>'),
        GenericRepr('<Comment id=112346707 user=崩塌γ>'),
        GenericRepr('<Comment id=112342851 user=jarvisvillar342>'),
        GenericRepr('<Comment id=112335811 user=Monsieur Morte>'),
        GenericRepr('<Comment id=112334847 user=Leong36>'),
        GenericRepr('<Comment id=112333580 user=夜瑟>')
    ],
    'next': 30,
    'total_comments': 51
}

snapshots['test_search_illustrations 1'] = {
    'illustrations': [
        GenericRepr('<Illustration id=87180953 user=wlop>'),
        GenericRepr('<Illustration id=87151353 user=lefthandchi>'),
        GenericRepr('<Illustration id=87078857 user=杏花村>'),
        GenericRepr('<Illustration id=86979680 user=wlop>'),
        GenericRepr('<Illustration id=86966556 user=MeEpo>')
    ],
    'next': None,
    'search_span_limit': 31536000
}
