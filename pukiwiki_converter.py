# -*- coding: utf-8 -*-

#=====================================
# PukiWikiからMediaWikiへ変換する処理
#=====================================


class pukiwiki_convert:
	# 初期化処理
	def __init__(self, pukiwiki_url, pukiwiki_basic, pukiwiki_basic_id, pukiwiki_basic_pw, mediawiki_url, mediawiki_login_id, mediawiki_login_pw, other_debug_mode):
		self.pukiwiki_url		 = pukiwiki_url
		self.pukiwiki_basic		 = pukiwiki_basic
		self.pukiwiki_basic_id	 = pukiwiki_basic_id
		self.pukiwiki_basic_pw	 = pukiwiki_basic_pw
		self.mediawiki_login_id  = mediawiki_login_id
		self.mediawiki_login_pw  = mediawiki_login_pw
		self.other_debug_mode    = other_debug_mode
		
		print "__init__"
	
	# PukiWikiのページ一覧から全てのURLを取得
	def get_all_page_url(self):
		print "get_all_page_url"

	# PukiWikiから指定URLのページを取得(添付ファイルも含む)
	def get_page(self):
		print "get_page"
	
	# PukiWikiの形式からMediaWikiの形式
	def __p2m_convert(self):
		print "convert"
	
	# データをMediaWikiにアップロード
	def mediawiki_upload(self):
		print "mediawiki_upload"
