data_list = ["98109sdi72", "ais87sdh1", "09821hadi", "hgatruarr", "xkayTakadaPKN", "z9ai8daohad", "q", "qkkudsfids3", "tG8012khasd", "ioawuywe", "aqteyegr", "a", "1", "yta", "swqer", "puytar", "sx153iar", "vcdsaqurr", "gykhdia", "weqw256465", "equtr", "hhnjklhad", "yatr", "oiu012ih", "yataraK", "HaH", "jadK", "iuoiudoa97asdfa", "ioiuodsa", "Kkdaj","iuoiaiua", "oiopjpiayra", "1jhkjakjdgar", "nhbvddwqsf", "iuoiaura0", "9801923nna", "7647", "kiraKi", "ouoiaoiad1", "zswqKHAIARAja", "yhty", "kueroiuasd", "iariKakdaQ", "x1", "hhyrtG", "xkaryTR4", "asweq", "o0192yhasda", "iuoaida", "v", "uoiuoidasa", "i1231har12", "98a09da", "azk", "iouoiadakda", "j", "761HUhayK", "kadaduf", "kaanc", "h", "iad", "z", "atadydsa", "iuoai", "iuadada", "Lkauda", "urahK", "7yarkK", "zaqwetya", "sdfe", "hasWesW", "iaoida", "ahara", "kwyack", "iaidja", "ii3hKIIada", "irajYta2W", "ikdajr", "zawhdyadg", "kerTRE", "iuoiuo2K", "sdeWKrai", "kadauyhyk", "kjxkanhg", "kada", "aKajQ", "kadYT", "LqdhariT"]
# a. buat data_list menjadi berurutan dengan 2 cara yang berbeda

# cara1
data_list.sort()
print(data_list)

# cara2
data_list.reverse()
print(data_list)

# b. buat code untuk menampilkan data yang memiliki jumlah huruf yang terpanjang yang ada didalam data_list
print(max(data_list))

# c. buat code untuk menampilkan data yang memiliki 2 huruf besar contoh: "LqdhariT" 
out = [item for item in data_list if sum(map(str.isupper, item))==2]
print(out)