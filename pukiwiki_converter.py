# -*- coding: utf-8 -*-

#=====================================
# PukiWikiからMediaWikiへ変換する処理
#=====================================


class pukiwiki_convert:
	# 初期化処理
	def __init__(self, pukiwiki_url, pukiwiki_basic, mediawiki_url, mediawiki_login_id, mediawiki_login_pw, other_debug_mode):
		self.pukiwiki_url		 = pukiwiki_url
		self.pukiwiki_basic		 = pukiwiki_basic
		self.mediawiki_login_id  = mediawiki_login_id
		self.mediawiki_login_pw  = mediawiki_login_pw
		self.other_debug_mode    = other_debug_mode
		
		print __name__
	
	# PukiWikiのページ一覧から全てのページを取得

	# PukiWikiから指定URLのページを取得(添付ファイルも含む)
	
	# データをMediaWikiにアップロード

