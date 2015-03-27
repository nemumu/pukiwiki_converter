# -*- coding: utf-8 -*-
from pukiwiki_converter import *

#=============================
#       PukiWikiの設定
#=============================
# PukiWikiトップページのURL
PUKIWIKI_URL = ""

# PukiWikiのページ閲覧にBasic認証が有るか
# (Trueなら有り、Falseなら無し)
PUKIWIKI_BASIC = True

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

#=============================
#    ライブラリ呼び出し処理
#=============================

if __name__ == "__main__":
	# PukiWikiからデータの取り出し
	# (この時は変換されていない)
	wiki_converter = pukiwiki_convert(PUKIWIKI_URL, PUKIWIKI_BASIC, MEDIAWIKI_URL, MEDIAWIKI_LOGIN_ID, MEDIAWIKI_LOGIN_PW, OTHER_DEBUG_MODE)
	
	# PukiWikiのデータをMediaWikiの形式に変換

	# MediaWikiにアップロード
	print "Fin"
