# -*- coding: utf-8 -*-

import requests
import re
import time
import urllib
import os

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
		self.data_cache_directory= data_cache_directory + '/'
		
		print "__init__"
	
	# PukiWikiのページ一覧から全てのURLを取得
	def get_all_page_url(self):
		page_list_url = self.pukiwiki_url + "index.php?cmd=list"

		sess = requests.session()

		# Basic認証が必要な場合はフィールドを追加
		response = self.__get_data(page_list_url)
		'''
		if self.pukiwiki_basic == True:
			response = sess.get(page_list_url, auth=(self.pukiwiki_basic_id, self.pukiwiki_basic_pw))
		else:
			response = sess.get(page_list_url)
		'''

		html = response.text

		matchedList = re.findall(r'<li><a href=".+?">', html)


		for i in range( len(matchedList) ):
			matchedList[i] = matchedList[i].replace('<li><a href="', '')
			matchedList[i] = matchedList[i].replace(self.pukiwiki_url + 'index.php?', '')
			matchedList[i] = matchedList[i].replace('">', '')
		
		print "get_all_page_url"
		
		return matchedList

	# PukiWikiから指定ページIDのページを取得
	# 添付ファイルも含めてディレクトリに保存
	def get_page(self, page_id):
		# ディレクトリを作成
		try:
			os.makedirs(self.data_cache_directory + page_id)
		except OSError:
			print "Duplicate File"

		# 添付ファイルをダウンロード
		self.__get_page_attach(page_id)

		# テキストをダウンロード

		print "get_page"
	
	# PukiWikiの記事IDからディレクトリ内に添付ファイルを保存
	def __get_page_attach(self, page_id):
		# ページからダウンロードリンク一覧を取得
		page_url = self.pukiwiki_url + 'index.php?' + page_id
		sess = requests.session()

		response = self.__get_data(page_url)

		html = response.text

		file_list = re.findall(self.pukiwiki_url + r'index.php\?plugin=attach&amp;pcmd=open&amp;file=.+?"', html)

		for i in range( len(file_list) ):
			file_list[i] = file_list[i].replace('"', '')
			file_list[i] = file_list[i].replace('amp;', '&')

			#print file_list[i]

			# ファイル名を取り出す
			file_name = ""
			file_name_regex = re.compile('&file=.+?&')
			file_name_match = file_name_regex.search( file_list[i] )

			if file_name_match:
				file_name = file_name_match.group()
				file_name = file_name.replace('&file=', '')
				file_name = file_name.replace('&', '')
				file_name = urllib.unquote( file_name ).decode('utf-8')

			print "File_name:%s" %  file_name
				
			continue

			# ダウンロードしてディレクトリに保存
			response = self.__get_data(file_list[i])

			# ファイルのダウンロードに成功したら保存する
			if response.status_code == 200:
				print "Save data"
				

			break

			

		# ダウンロードしてディレクトリに保存
		print "get_attach"
	
	# PukiWikiの記事IDからディレクトリ内にテキストを保存
	# (この時点ではMediaWikiフォーマットへの変換は行わない)
	def __get_page_text(self, page_id):
		print "get_page_text"
	
	# GETでデータを取得するメソッド
	def __get_data(self, url):
		sess = requests.session()

		if self.pukiwiki_basic == True:
			response = sess.get(url, auth=(self.pukiwiki_basic_id, self.pukiwiki_basic_pw) )
		else:
			response = sess.get(url)
		return response
	
	# PukiWikiの形式からMediaWikiの形式
	def __p2m_convert(self):
		print "convert"
	
	# データをMediaWikiにアップロード
	def mediawiki_upload(self):
		print "mediawiki_upload"
	
