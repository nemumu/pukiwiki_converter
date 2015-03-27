# -*- coding: utf-8 -*-

import requests
import re

#=====================================
# PukiWikiからMediaWikiへ変換する処理
#=====================================


class pukiwiki_convert:
	# 初期化処理
	def __init__(self, pukiwiki_url, pukiwiki_basic, pukiwiki_basic_id, pukiwiki_basic_pw, mediawiki_url, mediawiki_login_id, mediawiki_login_pw, other_debug_mode, data_cache_directory):
		self.pukiwiki_url		 = pukiwiki_url
		self.pukiwiki_basic		 = pukiwiki_basic
		self.pukiwiki_basic_id	 = pukiwiki_basic_id
		self.pukiwiki_basic_pw	 = pukiwiki_basic_pw
		self.mediawiki_login_id  = mediawiki_login_id
		self.mediawiki_login_pw  = mediawiki_login_pw
		self.other_debug_mode    = other_debug_mode
		self.data_cache_directory= data_cache_directory
		
		print "__init__"
	
	# PukiWikiのページ一覧から全てのURLを取得
	def get_all_page_url(self):
		page_list_url = self.pukiwiki_url + "index.php?cmd=list"

		sess = requests.session()

		# Basic認証が必要な場合はフィールドを追加
		if self.pukiwiki_basic == True:
			response = sess.get(page_list_url, auth=(self.pukiwiki_basic_id, self.pukiwiki_basic_pw))
		else:
			response = sess.get(page_list_url)

		html = response.text

		matchedList = re.findall(r'<li><a href=".+?">', html)


		for i in range( len(matchedList) ):
			matchedList[i] = matchedList[i].replace('<li><a href="', '')
			matchedList[i] = matchedList[i].replace(self.pukiwiki_url + 'index.php?', '')
			matchedList[i] = matchedList[i].replace('">', '')
		
		print "get_all_page_url"
		
		return matchedList

	# PukiWikiから指定URLのページを取得
	# 添付ファイルも含めてディレクトリに保存
	def get_page(self):
		print "get_page"
	
	# PukiWikiのURLから指定ディレクトリ内に添付ファイルを保存
	def __get_attach(self, wiki_url, directory):
		print "get_attach"
	
	# PukiWikiの形式からMediaWikiの形式
	def __p2m_convert(self):
		print "convert"
	
	# データをMediaWikiにアップロード
	def mediawiki_upload(self):
		print "mediawiki_upload"
