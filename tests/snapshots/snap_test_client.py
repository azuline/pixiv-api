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

snapshots['test_fetch_followers 1'] = {
    'next': None,
    'user_previews': [
        {
            'illustrations': [
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=11111111 name=User1>')
        },
        {
            'illustrations': [
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=22222222 name=User2>')
        }
    ]
}

snapshots['test_fetch_following 1'] = {
    'next': 30,
    'user_previews': [
        {
            'illustrations': [
                GenericRepr('<Illustration id=78836488 user=千>'),
                GenericRepr('<Illustration id=78709721 user=千>'),
                GenericRepr('<Illustration id=64253519 user=千>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=14936402 name=千>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=87555678 user=nonokuro>'),
                GenericRepr('<Illustration id=87488330 user=nonokuro>'),
                GenericRepr('<Illustration id=85900987 user=nonokuro>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=14544133 name=nonokuro>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=79221516 user=郵>'),
                GenericRepr('<Illustration id=78022277 user=郵>'),
                GenericRepr('<Illustration id=76747694 user=郵>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=265590 name=郵>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=84625904 user=なんこ>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=22688361 name=なんこ>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=85711595 user=Renos>'),
                GenericRepr('<Illustration id=84188262 user=Renos>'),
                GenericRepr('<Illustration id=82788314 user=Renos>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=799177 name=Renos>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=86782351 user=漫画素材工房>'),
                GenericRepr('<Illustration id=86521567 user=漫画素材工房>'),
                GenericRepr('<Illustration id=86465969 user=漫画素材工房>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=16776564 name=漫画素材工房>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=86278270 user=零＠通販始めた>'),
                GenericRepr('<Illustration id=84215645 user=零＠通販始めた>'),
                GenericRepr('<Illustration id=83523673 user=零＠通販始めた>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=74184 name=零＠通販始めた>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=66817374 user=ジョー>'),
                GenericRepr('<Illustration id=63542628 user=ジョー>'),
                GenericRepr('<Illustration id=63500646 user=ジョー>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=24976253 name=ジョー>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=87479619 user=ともわか>'),
                GenericRepr('<Illustration id=87479609 user=ともわか>'),
                GenericRepr('<Illustration id=87377158 user=ともわか>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=2733167 name=ともわか>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=87597736 user=toshi>'),
                GenericRepr('<Illustration id=87349228 user=toshi>'),
                GenericRepr('<Illustration id=87324862 user=toshi>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=637016 name=toshi>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=87188253 user=HxxG / ホン>'),
                GenericRepr('<Illustration id=87053374 user=HxxG / ホン>'),
                GenericRepr('<Illustration id=86055915 user=HxxG / ホン>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=1193139 name=HxxG / ホン>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=87504129 user=siki>'),
                GenericRepr('<Illustration id=85602057 user=siki>'),
                GenericRepr('<Illustration id=85503899 user=siki>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=6558698 name=siki>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=85180824 user=织布机loom>'),
                GenericRepr('<Illustration id=84049530 user=织布机loom>'),
                GenericRepr('<Illustration id=82831794 user=织布机loom>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=13695413 name=织布机loom>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=87314047 user=ごとー🌱>'),
                GenericRepr('<Illustration id=87033380 user=ごとー🌱>'),
                GenericRepr('<Illustration id=86992778 user=ごとー🌱>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=2956783 name=ごとー🌱>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=87583225 user=SH>'),
                GenericRepr('<Illustration id=86873466 user=SH>'),
                GenericRepr('<Illustration id=86143934 user=SH>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=2865617 name=SH>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=86683212 user=中山>'),
                GenericRepr('<Illustration id=84543085 user=中山>'),
                GenericRepr('<Illustration id=83720988 user=中山>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=54851546 name=中山>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=86053040 user=☺︎>'),
                GenericRepr('<Illustration id=85920000 user=☺︎>'),
                GenericRepr('<Illustration id=84392796 user=☺︎>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=9544495 name=☺︎>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=85423051 user=￦ANKE>'),
                GenericRepr('<Illustration id=85372147 user=￦ANKE>'),
                GenericRepr('<Illustration id=84811237 user=￦ANKE>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=24218478 name=￦ANKE>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=87356221 user=ㅤ>'),
                GenericRepr('<Illustration id=86955669 user=ㅤ>'),
                GenericRepr('<Illustration id=86650553 user=ㅤ>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=1079073 name=ㅤ>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=86464612 user=YD>'),
                GenericRepr('<Illustration id=86343645 user=YD>'),
                GenericRepr('<Illustration id=86221471 user=YD>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=853087 name=YD>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=84504000 user=モ誰>'),
                GenericRepr('<Illustration id=84210175 user=モ誰>'),
                GenericRepr('<Illustration id=83176771 user=モ誰>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=1878082 name=モ誰>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=79322467 user=mimo>'),
                GenericRepr('<Illustration id=74445409 user=mimo>'),
                GenericRepr('<Illustration id=74075737 user=mimo>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=29811192 name=mimo>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=82510919 user=NaO>'),
                GenericRepr('<Illustration id=82040117 user=NaO>'),
                GenericRepr('<Illustration id=81862923 user=NaO>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=41431583 name=NaO>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=86881847 user=へちま>'),
                GenericRepr('<Illustration id=86881826 user=へちま>'),
                GenericRepr('<Illustration id=82847277 user=へちま>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=1069005 name=へちま>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=85819570 user=咲良ゆき /사쿠라 유키>'),
                GenericRepr('<Illustration id=84259303 user=咲良ゆき /사쿠라 유키>'),
                GenericRepr('<Illustration id=83950549 user=咲良ゆき /사쿠라 유키>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=1661253 name=咲良ゆき /사쿠라 유키>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=87326569 user=EB十>'),
                GenericRepr('<Illustration id=87033406 user=EB十>'),
                GenericRepr('<Illustration id=86871412 user=EB十>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=2345928 name=EB十>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=81095945 user=一只水饺>'),
                GenericRepr('<Illustration id=80589712 user=一只水饺>'),
                GenericRepr('<Illustration id=80585824 user=一只水饺>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=50258200 name=一只水饺>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=86690745 user=おおむね鶴川>'),
                GenericRepr('<Illustration id=82584816 user=おおむね鶴川>'),
                GenericRepr('<Illustration id=81301190 user=おおむね鶴川>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=42926072 name=おおむね鶴川>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=86959403 user=たくぼん@お仕事募集中>'),
                GenericRepr('<Illustration id=86857256 user=たくぼん@お仕事募集中>'),
                GenericRepr('<Illustration id=86410354 user=たくぼん@お仕事募集中>')
            ],
            'is_muted': False,
            'novels': [
            ],
            'user': GenericRepr('<User id=23030728 name=たくぼん@お仕事募集中>')
        },
        {
            'illustrations': [
                GenericRepr('<Illustration id=86843753 user=あいだ>'),
                GenericRepr('<Illustration id=85668529 user=あいだ>'),
                GenericRepr('<Illustration id=85546694 user=あいだ>')
            ],
            'is_muted': False,
            'novels': [
                GenericRepr('<Novel id=14620056 user=あいだ>'),
                GenericRepr('<Novel id=14558775 user=あいだ>'),
                GenericRepr('<Novel id=14508049 user=あいだ>')
            ],
            'user': GenericRepr('<User id=8966556 name=あいだ>')
        }
    ]
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

snapshots['test_fetch_user 1'] = GenericRepr('<FullUser id=2188232 name=wlop>')

snapshots['test_fetch_user_bookmark_tags 1'] = {
    'bookmark_tags': [
        {
            'count': 3,
            'name': '9S'
        },
        {
            'count': 1,
            'name': 'CLIPSTUDIOPAINT'
        },
        {
            'count': 2,
            'name': 'FGO'
        },
        {
            'count': 1,
            'name': 'FLCL'
        },
        {
            'count': 3,
            'name': 'Fate'
        },
        {
            'count': 4,
            'name': 'Fate/GrandOrder'
        },
        {
            'count': 1,
            'name': 'Free!'
        },
        {
            'count': 155,
            'name': 'HANDYMONSTERS'
        },
        {
            'count': 1,
            'name': 'ICO'
        },
        {
            'count': 1,
            'name': 'ID:INVADED'
        },
        {
            'count': 4,
            'name': 'MOTHER'
        },
        {
            'count': 1,
            'name': 'MOTHER2'
        },
        {
            'count': 4,
            'name': 'MOTHER3'
        },
        {
            'count': 6,
            'name': 'NieR:Automata'
        },
        {
            'count': 1,
            'name': 'Perfume'
        },
        {
            'count': 1,
            'name': 'RO'
        },
        {
            'count': 2,
            'name': 'Re:ゼロから始める異世界生活'
        },
        {
            'count': 2,
            'name': 'SIREN'
        },
        {
            'count': 10,
            'name': 'Splatoon'
        },
        {
            'count': 1,
            'name': 'Undertale'
        },
        {
            'count': 40,
            'name': 'VOCALOID'
        },
        {
            'count': 41,
            'name': 'YOI【腐】'
        },
        {
            'count': 4,
            'name': 'mother3'
        },
        {
            'count': 1,
            'name': 'splatoon'
        },
        {
            'count': 3,
            'name': '★魚'
        },
        {
            'count': 1,
            'name': 'あんさん腐るスターズ!'
        },
        {
            'count': 1,
            'name': 'うごイラ'
        },
        {
            'count': 1,
            'name': 'きんいろモザイク'
        },
        {
            'count': 6,
            'name': 'けものフレンズ'
        },
        {
            'count': 1,
            'name': 'ご注文はうさぎですか?'
        }
    ],
    'next': 30
}

snapshots['test_fetch_user_bookmarks 1'] = {
    'illustrations': [
        GenericRepr('<Illustration id=54798429 user=ひでこ>')
    ],
    'next': None
}

snapshots['test_fetch_user_illustrations 1'] = {
    'illustrations': [
        GenericRepr('<Illustration id=87492458 user=wlop>'),
        GenericRepr('<Illustration id=87180953 user=wlop>'),
        GenericRepr('<Illustration id=86979680 user=wlop>'),
        GenericRepr('<Illustration id=86454354 user=wlop>'),
        GenericRepr('<Illustration id=86261514 user=wlop>'),
        GenericRepr('<Illustration id=86248394 user=wlop>'),
        GenericRepr('<Illustration id=86044539 user=wlop>'),
        GenericRepr('<Illustration id=83492653 user=wlop>'),
        GenericRepr('<Illustration id=83471825 user=wlop>'),
        GenericRepr('<Illustration id=83451391 user=wlop>'),
        GenericRepr('<Illustration id=83431165 user=wlop>'),
        GenericRepr('<Illustration id=83409040 user=wlop>'),
        GenericRepr('<Illustration id=83380879 user=wlop>'),
        GenericRepr('<Illustration id=83222944 user=wlop>'),
        GenericRepr('<Illustration id=83222943 user=wlop>'),
        GenericRepr('<Illustration id=83197731 user=wlop>'),
        GenericRepr('<Illustration id=83173860 user=wlop>'),
        GenericRepr('<Illustration id=83150157 user=wlop>'),
        GenericRepr('<Illustration id=83129810 user=wlop>'),
        GenericRepr('<Illustration id=83109676 user=wlop>'),
        GenericRepr('<Illustration id=80096963 user=wlop>'),
        GenericRepr('<Illustration id=75523989 user=wlop>'),
        GenericRepr('<Illustration id=75508638 user=wlop>'),
        GenericRepr('<Illustration id=74503110 user=wlop>'),
        GenericRepr('<Illustration id=74502130 user=wlop>'),
        GenericRepr('<Illustration id=73755434 user=wlop>'),
        GenericRepr('<Illustration id=73165062 user=wlop>'),
        GenericRepr('<Illustration id=73042381 user=wlop>'),
        GenericRepr('<Illustration id=72596225 user=wlop>'),
        GenericRepr('<Illustration id=72461417 user=wlop>')
    ],
    'next': 30
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
