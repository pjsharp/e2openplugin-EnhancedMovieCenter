import six


# -*- coding: utf-8 -*-
LanguageCodes = {}

LanguageCodes["aar"] = LanguageCodes["aa"] = ("Afar", "Hamitic")
LanguageCodes["abk"] = LanguageCodes["ab"] = ("Abkhazian", "Ibero-caucasian")
LanguageCodes["afr"] = LanguageCodes["af"] = ("Afrikaans", "Germanic")
LanguageCodes["amh"] = LanguageCodes["am"] = ("Amharic", "Semitic")
LanguageCodes["ara"] = LanguageCodes["ar"] = ("Arabic", "Semitic")
LanguageCodes["asm"] = LanguageCodes["as"] = ("Assamese", "Indian")
LanguageCodes["ave"] = LanguageCodes["ae"] = ("Avestan", "")
LanguageCodes["aym"] = LanguageCodes["ay"] = ("Aymara", "Amerindian")
LanguageCodes["aze"] = LanguageCodes["az"] = ("Azerbaijani", "Turkic/altaic")
LanguageCodes["bak"] = LanguageCodes["ba"] = ("Bashkir", "Turkic/altaic")
LanguageCodes["bel"] = LanguageCodes["be"] = ("Belarusian", "Slavic")
LanguageCodes["ben"] = LanguageCodes["bn"] = ("Bengali", "Indian")
LanguageCodes["bih"] = LanguageCodes["bh"] = ("Bihari", "Indian")
LanguageCodes["bis"] = LanguageCodes["bi"] = ("Bislama", "")
LanguageCodes["bod"] = LanguageCodes["tib"] = LanguageCodes["bo"] = ("Tibetan", "Asian")
LanguageCodes["bos"] = LanguageCodes["bs"] = ("Bosnian", "")
LanguageCodes["bre"] = LanguageCodes["br"] = ("Breton", "Celtic")
LanguageCodes["bul"] = LanguageCodes["bg"] = ("Bulgarian", "Slavic")
LanguageCodes["cat"] = LanguageCodes["ca"] = ("Catalan", "Romance")
LanguageCodes["ces"] = LanguageCodes["cze"] = LanguageCodes["cs"] = ("Czech", "Slavic")
LanguageCodes["cha"] = LanguageCodes["ch"] = ("Chamorro", "")
LanguageCodes["che"] = LanguageCodes["ce"] = ("Chechen", "")
LanguageCodes["chu"] = LanguageCodes["cu"] = ("Church Slavic", "")
LanguageCodes["chv"] = LanguageCodes["cv"] = ("Chuvash", "")
LanguageCodes["cor"] = LanguageCodes["kw"] = ("Cornish", "")
LanguageCodes["cos"] = LanguageCodes["co"] = ("Corsican", "Romance")
LanguageCodes["cym"] = LanguageCodes["wel"] = LanguageCodes["cy"] = ("Welsh", "Celtic")
LanguageCodes["dan"] = LanguageCodes["da"] = ("Danish", "Germanic")
LanguageCodes["deu"] = LanguageCodes["ger"] = LanguageCodes["de"] = ("German", "Germanic")
LanguageCodes["dzo"] = LanguageCodes["dz"] = ("Dzongkha", "Asian")
LanguageCodes["ell"] = LanguageCodes["gre"] = LanguageCodes["el"] = ("Greek, Modern (1453-)", "Latin/greek")
LanguageCodes["eng"] = LanguageCodes["en"] = ("English", "Germanic")
LanguageCodes["epo"] = LanguageCodes["eo"] = ("Esperanto", "International aux.")
LanguageCodes["est"] = LanguageCodes["et"] = ("Estonian", "Finno-ugric")
LanguageCodes["eus"] = LanguageCodes["baq"] = LanguageCodes["eu"] = ("Basque", "Basque")
LanguageCodes["fao"] = LanguageCodes["fo"] = ("Faroese", "Germanic")
LanguageCodes["fas"] = LanguageCodes["per"] = LanguageCodes["fa"] = ("Persian", "")
LanguageCodes["fij"] = LanguageCodes["fj"] = ("Fijian", "Oceanic/indonesian")
LanguageCodes["fin"] = LanguageCodes["fi"] = ("Finnish", "Finno-ugric")
LanguageCodes["fra"] = LanguageCodes["fre"] = LanguageCodes["fr"] = ("French", "Romance")
LanguageCodes["fry"] = LanguageCodes["fy"] = ("Frisian", "Germanic")
LanguageCodes["gla"] = LanguageCodes["gd"] = ("Gaelic (Scots)", "Celtic")
LanguageCodes["gle"] = LanguageCodes["ga"] = ("Irish", "Celtic")
LanguageCodes["glg"] = LanguageCodes["gl"] = ("Gallegan", "Romance")
LanguageCodes["glv"] = LanguageCodes["gv"] = ("Manx", "")
LanguageCodes["grn"] = LanguageCodes["gn"] = ("Guarani", "Amerindian")
LanguageCodes["guj"] = LanguageCodes["gu"] = ("Gujarati", "Indian")
LanguageCodes["hau"] = LanguageCodes["ha"] = ("Hausa", "Negro-african")
LanguageCodes["heb"] = LanguageCodes["he"] = ("Hebrew", "")
LanguageCodes["her"] = LanguageCodes["hz"] = ("Herero", "")
LanguageCodes["hin"] = LanguageCodes["hi"] = ("Hindi", "Indian")
LanguageCodes["hmo"] = LanguageCodes["ho"] = ("Hiri Motu", "")
LanguageCodes["hrv"] = LanguageCodes["scr"] = LanguageCodes["hr"] = ("Croatian", "Slavic")
LanguageCodes["hun"] = LanguageCodes["hu"] = ("Hungarian", "Finno-ugric")
LanguageCodes["hye"] = LanguageCodes["arm"] = LanguageCodes["hy"] = ("Armenian", "Indo-european (other)")
LanguageCodes["iku"] = LanguageCodes["iu"] = ("Inuktitut", "")
LanguageCodes["ile"] = LanguageCodes["ie"] = ("Interlingue", "International aux.")
LanguageCodes["ina"] = LanguageCodes["ia"] = ("Interlingua (International Auxiliary Language Association)", "International aux.")
LanguageCodes["ind"] = LanguageCodes["id"] = ("Indonesian", "")
LanguageCodes["ipk"] = LanguageCodes["ik"] = ("Inupiaq", "Eskimo")
LanguageCodes["isl"] = LanguageCodes["ice"] = LanguageCodes["is"] = ("Icelandic", "Germanic")
LanguageCodes["ita"] = LanguageCodes["it"] = ("Italian", "Romance")
LanguageCodes["jaw"] = LanguageCodes["jav"] = LanguageCodes["jw"] = ("Javanese", "")
LanguageCodes["jpn"] = LanguageCodes["ja"] = ("Japanese", "Asian")
LanguageCodes["kal"] = LanguageCodes["kl"] = ("Kalaallisut", "Eskimo")
LanguageCodes["kan"] = LanguageCodes["kn"] = ("Kannada", "Dravidian")
LanguageCodes["kas"] = LanguageCodes["ks"] = ("Kashmiri", "Indian")
LanguageCodes["kat"] = LanguageCodes["geo"] = LanguageCodes["ka"] = ("Georgian", "Ibero-caucasian")
LanguageCodes["kaz"] = LanguageCodes["kk"] = ("Kazakh", "Turkic/altaic")
LanguageCodes["khm"] = LanguageCodes["km"] = ("Khmer", "Asian")
LanguageCodes["kik"] = LanguageCodes["ki"] = ("Kikuyu", "")
LanguageCodes["kin"] = LanguageCodes["rw"] = ("Kinyarwanda", "Negro-african")
LanguageCodes["kir"] = LanguageCodes["ky"] = ("Kirghiz", "Turkic/altaic")
LanguageCodes["kom"] = LanguageCodes["kv"] = ("Komi", "")
LanguageCodes["kor"] = LanguageCodes["ko"] = ("Korean", "Asian")
LanguageCodes["kur"] = LanguageCodes["ku"] = ("Kurdish", "Iranian")
LanguageCodes["lao"] = LanguageCodes["lo"] = ("Lao", "Asian")
LanguageCodes["lat"] = LanguageCodes["la"] = ("Latin", "Latin/greek")
LanguageCodes["lav"] = LanguageCodes["lv"] = ("Latvian", "Baltic")
LanguageCodes["lin"] = LanguageCodes["ln"] = ("Lingala", "Negro-african")
LanguageCodes["lit"] = LanguageCodes["lt"] = ("Lithuanian", "Baltic")
LanguageCodes["ltz"] = LanguageCodes["lb"] = ("Letzeburgesch", "")
LanguageCodes["mah"] = LanguageCodes["mh"] = ("Marshall", "")
LanguageCodes["mal"] = LanguageCodes["ml"] = ("Malayalam", "Dravidian")
LanguageCodes["mar"] = LanguageCodes["mr"] = ("Marathi", "Indian")
LanguageCodes["mis"] = ("Miscellaneous languages", "")
LanguageCodes["mkd"] = LanguageCodes["mac"] = LanguageCodes["mk"] = ("Macedonian", "Slavic")
LanguageCodes["mlg"] = LanguageCodes["mg"] = ("Malagasy", "Oceanic/indonesian")
LanguageCodes["mlt"] = LanguageCodes["mt"] = ("Maltese", "Semitic")
LanguageCodes["mol"] = LanguageCodes["mo"] = ("Moldavian", "Romance")
LanguageCodes["mon"] = LanguageCodes["mn"] = ("Mongolian", "")
LanguageCodes["mri"] = LanguageCodes["mao"] = LanguageCodes["mi"] = ("Maori", "Oceanic/indonesian")
LanguageCodes["msa"] = LanguageCodes["may"] = LanguageCodes["ms"] = ("Malay", "Oceanic/indonesian")
LanguageCodes["mul"] = ("Multiple languages", "")
LanguageCodes["mya"] = LanguageCodes["bur"] = LanguageCodes["my"] = ("Burmese", "Asian")
LanguageCodes["nau"] = LanguageCodes["na"] = ("Nauru", "")
LanguageCodes["nav"] = LanguageCodes["nv"] = ("Navajo", "")
LanguageCodes["nbl"] = LanguageCodes["nr"] = ("Ndebele, South", "")
LanguageCodes["nde"] = LanguageCodes["nd"] = ("Ndebele, North", "")
LanguageCodes["ndo"] = LanguageCodes["ng"] = ("Ndonga", "")
LanguageCodes["nep"] = LanguageCodes["ne"] = ("Nepali", "Indian")
LanguageCodes["nld"] = LanguageCodes["dut"] = LanguageCodes["nl"] = ("Dutch", "Germanic")
LanguageCodes["nno"] = LanguageCodes["nn"] = ("Norwegian Nynorsk", "")
LanguageCodes["nob"] = LanguageCodes["nb"] = ("Norwegian Bokmål", "")
LanguageCodes["nor"] = LanguageCodes["no"] = ("Norwegian", "Germanic")
LanguageCodes["nya"] = LanguageCodes["ny"] = ("Chichewa; Nyanja", "")
LanguageCodes["oci"] = LanguageCodes["oc"] = ("Occitan (post 1500); Provençal", "Romance")
LanguageCodes["ori"] = LanguageCodes["or"] = ("Oriya", "Indian")
LanguageCodes["orm"] = LanguageCodes["om"] = ("Oromo", "Hamitic")
LanguageCodes["oss"] = LanguageCodes["os"] = ("Ossetian; Ossetic", "")
LanguageCodes["pan"] = LanguageCodes["pa"] = ("Panjabi", "Indian")
LanguageCodes["pli"] = LanguageCodes["pi"] = ("Pali", "")
LanguageCodes["pol"] = LanguageCodes["pl"] = ("Polish", "Slavic")
LanguageCodes["por"] = LanguageCodes["pt"] = ("Portuguese", "Romance")
LanguageCodes["pus"] = LanguageCodes["ps"] = ("Pushto", "Iranian")
LanguageCodes["que"] = LanguageCodes["qu"] = ("Quechua", "Amerindian")
LanguageCodes["ron"] = LanguageCodes["rum"] = LanguageCodes["ro"] = ("Romanian", "Romance")
LanguageCodes["run"] = LanguageCodes["rn"] = ("Rundi", "Negro-african")
LanguageCodes["rus"] = LanguageCodes["ru"] = ("Russian", "Slavic")
LanguageCodes["sag"] = LanguageCodes["sg"] = ("Sango", "Negro-african")
LanguageCodes["san"] = LanguageCodes["sa"] = ("Sanskrit", "Indian")
LanguageCodes["sin"] = LanguageCodes["si"] = ("Sinhalese", "Indian")
LanguageCodes["slk"] = LanguageCodes["slo"] = LanguageCodes["sk"] = ("Slovak", "Slavic")
LanguageCodes["slv"] = LanguageCodes["sl"] = ("Slovenian", "Slavic")
LanguageCodes["sme"] = LanguageCodes["se"] = ("Northern Sami", "")
LanguageCodes["smo"] = LanguageCodes["sm"] = ("Samoan", "Oceanic/indonesian")
LanguageCodes["sna"] = LanguageCodes["sn"] = ("Shona", "Negro-african")
LanguageCodes["snd"] = LanguageCodes["sd"] = ("Sindhi", "Indian")
LanguageCodes["som"] = LanguageCodes["so"] = ("Somali", "Hamitic")
LanguageCodes["sot"] = LanguageCodes["st"] = ("Sotho, Southern", "Negro-african")
LanguageCodes["esl"] = LanguageCodes["spa"] = LanguageCodes["es"] = ("Spanish", "Romance")
LanguageCodes["sqi"] = LanguageCodes["alb"] = LanguageCodes["sq"] = ("Albanian", "Indo-european (other)")
LanguageCodes["srd"] = LanguageCodes["sc"] = ("Sardinian", "")
LanguageCodes["srp"] = LanguageCodes["scc"] = LanguageCodes["sr"] = ("Serbian", "Slavic")
LanguageCodes["ssw"] = LanguageCodes["ss"] = ("Swati", "Negro-african")
LanguageCodes["sun"] = LanguageCodes["su"] = ("Sundanese", "Oceanic/indonesian")
LanguageCodes["swa"] = LanguageCodes["sw"] = ("Swahili", "Negro-african")
LanguageCodes["swe"] = LanguageCodes["sv"] = ("Swedish", "Germanic")
LanguageCodes["tah"] = LanguageCodes["ty"] = ("Tahitian", "")
LanguageCodes["tam"] = LanguageCodes["ta"] = ("Tamil", "Dravidian")
LanguageCodes["tat"] = LanguageCodes["tt"] = ("Tatar", "Turkic/altaic")
LanguageCodes["tel"] = LanguageCodes["te"] = ("Telugu", "Dravidian")
LanguageCodes["tgk"] = LanguageCodes["tg"] = ("Tajik", "Iranian")
LanguageCodes["tgl"] = LanguageCodes["tl"] = ("Tagalog", "Oceanic/indonesian")
LanguageCodes["tha"] = LanguageCodes["th"] = ("Thai", "Asian")
LanguageCodes["tir"] = LanguageCodes["ti"] = ("Tigrinya", "Semitic")
LanguageCodes["ton"] = LanguageCodes["to"] = ("Tonga (Tonga Islands)", "Oceanic/indonesian")
LanguageCodes["tsn"] = LanguageCodes["tn"] = ("Tswana", "Negro-african")
LanguageCodes["tso"] = LanguageCodes["ts"] = ("Tsonga", "Negro-african")
LanguageCodes["tuk"] = LanguageCodes["tk"] = ("Turkmen", "Turkic/altaic")
LanguageCodes["tur"] = LanguageCodes["tr"] = ("Turkish", "Turkic/altaic")
LanguageCodes["twi"] = LanguageCodes["tw"] = ("Twi", "Negro-african")
LanguageCodes["uig"] = LanguageCodes["ug"] = ("Uighur", "")
LanguageCodes["ukr"] = LanguageCodes["uk"] = ("Ukrainian", "Slavic")
LanguageCodes["und"] = ("Undetermined", "")
LanguageCodes["urd"] = LanguageCodes["ur"] = ("Urdu", "Indian")
LanguageCodes["uzb"] = LanguageCodes["uz"] = ("Uzbek", "Turkic/altaic")
LanguageCodes["vie"] = LanguageCodes["vi"] = ("Vietnamese", "Asian")
LanguageCodes["vol"] = LanguageCodes["vo"] = ("Volapük", "International aux.")
LanguageCodes["wol"] = LanguageCodes["wo"] = ("Wolof", "Negro-african")
LanguageCodes["xho"] = LanguageCodes["xh"] = ("Xhosa", "Negro-african")
LanguageCodes["yid"] = LanguageCodes["yi"] = ("Yiddish", "")
LanguageCodes["yor"] = LanguageCodes["yo"] = ("Yoruba", "Negro-african")
LanguageCodes["zha"] = LanguageCodes["za"] = ("Zhuang", "")
LanguageCodes["zho"] = LanguageCodes["chi"] = LanguageCodes["zh"] = ("Chinese", "Asian")
LanguageCodes["zul"] = LanguageCodes["zu"] = ("Zulu", "Negro-african")
LanguageCodes["zxx"] = ("No linguistic content", "")


class ISO639Language:
	[PRIMARY, SECONDARY, TERTIARY] = [1, 2, 3]

	def __init__(self, depth=PRIMARY):
		self.depth = depth

		wanted_languages = []
		if depth == self.PRIMARY:
			wanted_languages = ["Undetermined", "English", "German", "Arabic", "Catalan", "Croatian", "Czech", "Danish", "Dutch", "Estonian", "Finnish", "French", "Greek", "Hungarian", "Lithuanian", "Latvian", "Icelandic", "Italian", "Norwegian", "Polish", "Portuguese", "Russian", "Serbian", "Slovakian", "Slovenian", "Spanish", "Swedish", "Turkish", "Ukrainian"]
		elif depth == self.SECONDARY:
			for key, val in six.iteritems(LanguageCodes):
				if len(key) == 2:
					wanted_languages.append(val[0])
		else:
			for key, val in six.iteritems(LanguageCodes):
				if len(key) == 3:
					wanted_languages.append(val[0])

		self.idlist_by_name = {}
		for key, val in six.iteritems(LanguageCodes):
			val = val[0]
			if val not in wanted_languages:
				continue
			if val not in self.idlist_by_name:
				self.idlist_by_name[val] = [key]
			else:
				self.idlist_by_name[val].append(key)

		self.name_and_shortid_by_longid = {}
		self.name_by_shortid = {}
		for lang, id_list in six.iteritems(self.idlist_by_name):
			long_ids = []
			short_id = None
			for id in id_list:
				if len(id) == 3:
					long_ids.append(id)
				if len(id) == 2:
					self.name_by_shortid[id] = lang
					short_id = id
			for long_id in long_ids:
				self.name_and_shortid_by_longid[long_id] = (short_id, lang)
