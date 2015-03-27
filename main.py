# -*- coding: utf-8 -*-
from pukiwiki_converter import *
from config import *

if __name__ == "__main__":
	# PukiWikiからデータの取り出し
	# (この時は変換されていない)
	wiki_converter = pukiwiki_convert(PUKIWIKI_URL, PUKIWIKI_BASIC, PUKIWIKI_BASIC_ID, PUKIWIKI_BASIC_PW, MEDIAWIKI_URL, MEDIAWIKI_LOGIN_ID, MEDIAWIKI_LOGIN_PW, OTHER_DEBUG_MODE)
	
	# PukiWikiのデータをMediaWikiの形式に変換
	print wiki_converter.get_all_page_url()

	# MediaWikiにアップロード
	print "Fin"
