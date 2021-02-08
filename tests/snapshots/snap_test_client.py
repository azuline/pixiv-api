# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_fetch_bookmark 1'] = {
    'is_bookmarked': True,
    'tags': [
        {
            'is_registered': False,
            'name': 'ghostblade'
        },
        {
            'is_registered': False,
            'name': '风玲'
        },
        {
            'is_registered': False,
            'name': 'ボディチェーン'
        },
        {
            'is_registered': False,
            'name': 'プランジングネック'
        },
        {
            'is_registered': False,
            'name': 'オリジナル10000users入り'
        }
    ],
    'visibility': GenericRepr("<Visibility.PUBLIC: 'public'>")
}

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

snapshots['test_fetch_illustration_related 1'] = {
    'illustrations': [
        GenericRepr('<Illustration id=71647063 user=Aoi Ogata>'),
        GenericRepr('<Illustration id=86064668 user=綠雉>'),
        GenericRepr('<Illustration id=87045501 user=笑笑菌>'),
        GenericRepr('<Illustration id=86772050 user=紅シャケ＠お仕事募集中>'),
        GenericRepr('<Illustration id=51940103 user=Krenz@三日目東す02a>'),
        GenericRepr('<Illustration id=85144813 user=李牛>'),
        GenericRepr('<Illustration id=81891098 user=へちま>'),
        GenericRepr('<Illustration id=44745753 user=wlop>'),
        GenericRepr('<Illustration id=82966960 user=银色骐骥>'),
        GenericRepr('<Illustration id=82021578 user=T5>'),
        GenericRepr('<Illustration id=59564981 user=曦晨晨>'),
        GenericRepr('<Illustration id=81948142 user=えいひ>'),
        GenericRepr('<Illustration id=83681927 user=TOKKYU>'),
        GenericRepr('<Illustration id=83197731 user=wlop>'),
        GenericRepr('<Illustration id=85100959 user=karory>'),
        GenericRepr('<Illustration id=19665321 user=ハモンド華麗>'),
        GenericRepr('<Illustration id=73393936 user=モグモ>'),
        GenericRepr('<Illustration id=78552073 user=方向錯亂>'),
        GenericRepr('<Illustration id=82735340 user=福寿丸>'),
        GenericRepr('<Illustration id=79151599 user=Bae.C>'),
        GenericRepr('<Illustration id=78428914 user=ずいま>'),
        GenericRepr('<Illustration id=77941081 user=Bae.C>'),
        GenericRepr('<Illustration id=87416249 user=Lebring>'),
        GenericRepr('<Illustration id=69972787 user=mocha＠ネオケットB11>'),
        GenericRepr('<Illustration id=86982520 user=河CY>'),
        GenericRepr('<Illustration id=68481038 user=Aoi Ogata>'),
        GenericRepr('<Illustration id=78717394 user=ATDAN->'),
        GenericRepr('<Illustration id=70078815 user=mocha＠ネオケットB11>'),
        GenericRepr('<Illustration id=87033623 user=Miv4t>'),
        GenericRepr('<Illustration id=87347843 user=日向あずり>')
    ],
    'next': 30
}

snapshots['test_fetch_illustrations_following 1'] = {
    'illustrations': [
        GenericRepr('<Illustration id=87609354 user=sheepD>'),
        GenericRepr('<Illustration id=87608832 user=クメキ>')
    ],
    'next': 30
}

snapshots['test_fetch_illustrations_ranking 1'] = {
    'illustrations': [
        GenericRepr('<Illustration id=87535782 user=赤倉＠ジャケットご予約受付中>'),
        GenericRepr('<Illustration id=87549112 user=しろまんた>'),
        GenericRepr('<Illustration id=87550228 user=のう>'),
        GenericRepr('<Illustration id=87564564 user=新挑限>'),
        GenericRepr('<Illustration id=87535224 user=鳴海アラタ>'),
        GenericRepr('<Illustration id=87557970 user=mocha＠ネオケットB11>'),
        GenericRepr('<Illustration id=87550203 user=のう>'),
        GenericRepr('<Illustration id=87535316 user=banishment>'),
        GenericRepr('<Illustration id=87557715 user=おむたつ/omutatsu>'),
        GenericRepr('<Illustration id=87566017 user=鉄一>'),
        GenericRepr('<Illustration id=87556580 user=旧都なぎ>'),
        GenericRepr('<Illustration id=87550307 user=我美蘭☆エアコミケ２委託中！>'),
        GenericRepr('<Illustration id=87556574 user=torino>'),
        GenericRepr('<Illustration id=87535250 user=防人>'),
        GenericRepr('<Illustration id=87536478 user=majamari>'),
        GenericRepr('<Illustration id=87543800 user=そふら(sofra)>'),
        GenericRepr('<Illustration id=87570840 user=寺田てら>'),
        GenericRepr('<Illustration id=87535238 user=あすてろid>'),
        GenericRepr('<Illustration id=87542573 user=ヤマコ>'),
        GenericRepr('<Illustration id=87562431 user=ポ～ン（出水ぽすか）>'),
        GenericRepr('<Illustration id=87550981 user=チャイ>'),
        GenericRepr('<Illustration id=87546514 user=ふゆ>'),
        GenericRepr('<Illustration id=87556893 user=ファジョボレ>'),
        GenericRepr('<Illustration id=87559623 user=カフェ>'),
        GenericRepr('<Illustration id=87535230 user=ののこ>'),
        GenericRepr('<Illustration id=87535211 user=佐倉おりこ@単行本発売中>')
    ],
    'next': 30
}

snapshots['test_fetch_illustrations_recommended 1'] = {
    'contest_exists': False,
    'illustrations': [
        GenericRepr('<Illustration id=86336261 user=ハヤブサ🐤>'),
        GenericRepr('<Illustration id=86317105 user=弾>'),
        GenericRepr('<Illustration id=86320669 user=猫屋敷ぷしお>'),
        GenericRepr('<Illustration id=86324762 user=Prophet初>'),
        GenericRepr('<Illustration id=86314031 user=まるごし＠54BURGER>'),
        GenericRepr('<Illustration id=86316045 user=子野日🌸お仕事募集中>'),
        GenericRepr('<Illustration id=86313492 user=Aventador>'),
        GenericRepr('<Illustration id=86325951 user=柳家いづ>'),
        GenericRepr('<Illustration id=86316463 user=kukie-nyan>'),
        GenericRepr('<Illustration id=86341020 user=栞しい>'),
        GenericRepr('<Illustration id=86325459 user=coa>'),
        GenericRepr('<Illustration id=86309959 user=kajin>'),
        GenericRepr('<Illustration id=86311515 user=ひろ@お仕事募集中>'),
        GenericRepr('<Illustration id=86307089 user=KEN＿お仕事募集中>'),
        GenericRepr('<Illustration id=86314842 user=オスティ>'),
        GenericRepr('<Illustration id=86322328 user=ウラシマ/お仕事募集中>'),
        GenericRepr('<Illustration id=86321274 user=\u3000Monet>'),
        GenericRepr('<Illustration id=86333131 user=はづき>'),
        GenericRepr('<Illustration id=86339906 user=富士茄 鷹>'),
        GenericRepr('<Illustration id=86333557 user=ぺんたごん>'),
        GenericRepr('<Illustration id=86333576 user=ひだね>'),
        GenericRepr('<Illustration id=86306651 user=pen助@お仕事募集中>'),
        GenericRepr('<Illustration id=86330815 user=EYYY (岩盐盐)>'),
        GenericRepr('<Illustration id=86318439 user=あおい青羽＠ラブライブ！大好き>'),
        GenericRepr('<Illustration id=86336189 user=Vardan>'),
        GenericRepr('<Illustration id=86312311 user=na2>'),
        GenericRepr('<Illustration id=86306720 user=原田いすか>'),
        GenericRepr('<Illustration id=86312124 user=せゆーら@お寿司>'),
        GenericRepr('<Illustration id=86320876 user=月見草>')
    ],
    'next': {
        'max_bookmark_id_for_recommend': -1,
        'min_bookmark_id_for_recent_illustrations': 0,
        'offset': 30
    },
    'ranking_illustrations': [
    ]
}

snapshots['test_fetch_trending_tags 1'] = [
    {
        'illustration': GenericRepr('<Illustration id=87521667 user=Nagisssa摸鱼中>'),
        'tag': '甘雨(原神)',
        'translated_name': 'Ganyu (Genshin Impact)'
    },
    {
        'illustration': GenericRepr('<Illustration id=87530695 user=マコミック>'),
        'tag': '女の子',
        'translated_name': 'girl'
    },
    {
        'illustration': GenericRepr('<Illustration id=87514094 user=上倉エク>'),
        'tag': 'オリジナル',
        'translated_name': 'original'
    },
    {
        'illustration': GenericRepr('<Illustration id=87550307 user=我美蘭☆エアコミケ２委託中！>'),
        'tag': 'GenshinImpact',
        'translated_name': None
    },
    {
        'illustration': GenericRepr('<Illustration id=87515945 user=SanMuYYB>'),
        'tag': '初音ミク',
        'translated_name': 'hatsune miku'
    },
    {
        'illustration': GenericRepr('<Illustration id=87529229 user=冷色调咖啡>'),
        'tag': '百合',
        'translated_name': 'yuri'
    },
    {
        'illustration': GenericRepr('<Illustration id=87527799 user=hex_D>'),
        'tag': 'FGO',
        'translated_name': 'Fate/Grand Order'
    },
    {
        'illustration': GenericRepr('<Illustration id=87521445 user=日下氏>'),
        'tag': 'アイドルマスターシンデレラガールズ',
        'translated_name': 'The Idolmaster: Cinderella Girls'
    },
    {
        'illustration': GenericRepr('<Illustration id=87514130 user=桜ひより>'),
        'tag': 'VTuber',
        'translated_name': 'virtual YouTuber'
    },
    {
        'illustration': GenericRepr('<Illustration id=87550228 user=のう>'),
        'tag': 'VOCALOID',
        'translated_name': None
    },
    {
        'illustration': GenericRepr('<Illustration id=87543992 user=そふら(sofra)>'),
        'tag': 'にじさんじ',
        'translated_name': 'Nijisanji'
    },
    {
        'illustration': GenericRepr('<Illustration id=87529927 user=鯨丸>'),
        'tag': 'Fate/GrandOrder',
        'translated_name': 'Fate/Grand Order'
    },
    {
        'illustration': GenericRepr('<Illustration id=87520237 user=いくらうに>'),
        'tag': '東方Project',
        'translated_name': 'Touhou Project'
    },
    {
        'illustration': GenericRepr('<Illustration id=87535487 user=ぐらしおん>'),
        'tag': 'プリンセスコネクト!Re:Dive',
        'translated_name': 'Princess Connect! Re:Dive'
    },
    {
        'illustration': GenericRepr('<Illustration id=87519785 user=ポ～ン（出水ぽすか）>'),
        'tag': '創作',
        'translated_name': 'creation'
    },
    {
        'illustration': GenericRepr('<Illustration id=87535316 user=banishment>'),
        'tag': '風景',
        'translated_name': 'scenery'
    },
    {
        'illustration': GenericRepr('<Illustration id=87532633 user=カフェ>'),
        'tag': 'ポケモン',
        'translated_name': 'Pokémon'
    },
    {
        'illustration': GenericRepr('<Illustration id=87535258 user=月うさぎ＠お仕事募集中！>'),
        'tag': 'イラスト',
        'translated_name': 'illustration'
    },
    {
        'illustration': GenericRepr('<Illustration id=87514204 user=京田スズカ>'),
        'tag': '東方',
        'translated_name': 'Touhou'
    },
    {
        'illustration': GenericRepr('<Illustration id=87514788 user=紅シャケ＠お仕事募集中>'),
        'tag': 'アークナイツ',
        'translated_name': 'Arknights'
    },
    {
        'illustration': GenericRepr('<Illustration id=87546844 user=ＫＫ>'),
        'tag': '黒スト',
        'translated_name': 'black stockings'
    },
    {
        'illustration': GenericRepr('<Illustration id=87535299 user=まんなく>'),
        'tag': '着衣巨乳',
        'translated_name': 'clothed breasts'
    },
    {
        'illustration': GenericRepr('<Illustration id=87535238 user=あすてろid>'),
        'tag': '背景',
        'translated_name': 'background'
    },
    {
        'illustration': GenericRepr('<Illustration id=87544985 user=絹谷ゆたか>'),
        'tag': 'ケモミミ',
        'translated_name': 'animal ears'
    }
]

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
