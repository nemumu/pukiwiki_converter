# -*- coding: utf-8 -*-
from pukiwiki_converter import *

#=============================
#       PukiWikiの設定
#=============================
# PukiWikiトップページのURL
PUKIWIKI_URL = ""

# PukiWikiのページにBasic認証が有るか
# (Trueなら有り、Falseなら無し)
PUKIWIKI_BASIC = True

# PukiWikiページのBasic認証ID
# (PUKIWIKI_BASICがTrueの場合のみ使用)
PUKIWIKI_BASIC_ID = ""

# PukiWikiページのBasic認証PW
# (PUKIWIKI_BASICがTrueの場合のみ使用)
PUKIWIKI_BASIC_PW = ""

#=============================
#       MediaWikiの設定
#=============================
# MediaWikiトップページのURL
MEDIAWIKI_URL = ""

# MediaWikiのログインID
MEDIAWIKI_LOGIN_ID = ""

# MediaWikiのログインPW
MEDIAWIKI_LOGIN_PW = ""

#=============================
#       その他設定
#=============================
# デバッグモードかどうか
# (Trueならデバッグモード)
# ライブラリを編集するときに使うと良いかも
OTHER_DEBUG_MODE = True

# PukiWikiから取得したデータを一時的に保存するディレクトリ
# テキストと添付ファイルを保存する
DATA_CACHE_DIRECTORY = "data"
