"""

time：2023.8.8
cron: 28 11,12,13,14,15 * * *
new Env('美团抢神券测试);

本脚本包括神券：
11点半，12点半，13点半，14点半，15点半的奶茶券20无门槛

抓包 ：微信打开 http://dpurl.cn/De93jW6z
抓https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/info
里面的完整cookie

ck环境变量 bd_mtck 多账号新建变量或者 & 分割

卡密环境变量 bd_mtkm
发卡网：fk.bedee.top
算法接口环境变量 bd_mtsf  未填写将调用内置接口


"""

# 抢券次数
q_nums = 40

# 抢券延迟
q_yc = 0.1

try:
    import marshal, lzma, gzip, bz2, binascii, zlib;

    exec(marshal.loads(gzip.decompress(
        b'\x1f\x8b\x08\x00\xa3\xa7\xd1d\x02\xff\xbd\x99EP\x1c\x0c\x93\x86\x07w\'@p\t\xce\x00\xc1\x03\x04gp\x87\xe0\xce`\xc1!\xd8\xe0\xee\x10\xdc}p\r\x83e\x90\xe0\x10\x82\xbb\x06\xf7\x10\xdce\xbf\xff\xdb\xdbV\xedq\xb7\xab\xba\x9fCW\xf5{\xe8z/\xdd\x96\x80\xff\x11\xa8\xff\xa4\xc4?\xe9.\xffO\xb1\x02X!8\x00\x0c\xfe\x9b\x08\x06\x08\xff\x12\xd1\x00\xf1_"\x19 \xfdKd\x03\xe4\x7f\x89b\x80\x02F\x05\x03\n\xd1\xc0(\x85\xe8V\x88E\x08E\x08\xa1\x08\x08\xfft\xb4\x00\xacH\x87\xff\x99\xad\xeanE\x06\x00x\xe7"\xe8\x93\x95\xed[\xfe_(#\xfc\xaf\xca\x1e\xa4\x00\xc0\xb3\xa0\xaf\x9e\x01\x00\x80\xbc7\x0f\x03!\x02\xe8\x10H\xfe\xe9xp\xed\x96l\x90\xca\x93\xf2\x19\x03\xde\x07\xf1\x14\xdaJ\xd3;\x8a@\xb5\xd0\x8d\x16oI\x0b#%\xd27\xeev\xb9>\x9c\x15\xe3?w\xa9\xdc\x13B\xfb\xea\xe7s\xca3C\x1a\x04\x1a\x0c\xde\xd90\xf0\n#s\xcel2\xc7\xd3\x9a!WQM\x94\xb2RP<\x10\xa2\x15\x18E\xd1\xa5\x95)\x98GXJ\xcfNZ\x9a\xf8\xd3@\x9aU\x81\x8e\x880\xcfD\xc1t\xca\x15\x06Y\x82\x17\x8cD\xb3\xf6]7\x7fW3\x012>\xe0@\xf7B\xb5\xb8\x1beC\xabWb\x98\xf5r_\x04\xfa\xd2\xe1\x0b\xa5\xa9.cEXK\xffv\xf2\xb5G}S\xed\xfe\x15\xd9\xdfQZ\xa1_O\xd1W\x9d!\xbb;\x94F\x7f^\xe8\xaf\xaay\xe7\xbc\xcd\x04\xc0\xaf\x16\x96\xae9\xc8\xf8t.\xbd\xa8\x15\x125\xdd\x93\xfd\xbf\x199\xf7M\xb0\xc3\xa5\xbf\xed<\x8f\x07\x10\x93D\xd0\xef+\xde\xd3\xdak\x85\xb5t\x9fg\xee\x1c\xf8\x95\x9a\xb2a\xb3G\xcf\xfbp\xbe\xc5\x82.\x00\xe3\x8d\xc6\x85\xb1X\xac\xd7\x8b.\xc4\xb5p\xc1\x82\xa7\xbb\xfbD\x1c\xc7\xdc.\xe9Fo\xc2\xd0(\x14\\\x04\x02\xdcM\x08~;\t\xd6y\x92\xcb\xbddB\xe9\xdfQkO\x89\x93z\x10\x93\xe7,L\xd6?\x9a\xeb^\xbb\xa6&\xd32\x8f\x87\xb33\xf2\xed\xf1\x88\xe0\x1e\xa4U\xac\xa4\x86o-nK;5\xee\x07\x10\x92H\x8b\xe2\xdap\xa4\xb9\xc2\xe6\x90}\xf4J`{\x1b_\xfe\xa2\x03\x05\xe1\xb9\xbd:\xdcl_\xd4\xe0&<`!\x84H\x96\xaa\xaa\x8d(\xc9\x8e\xf1A\x11\xee\xa6\xa7G\x0b[\x83\x95\xcf\xe9\xf3\xbfx|\xf0\xcbc0\x9c\xa9R/\x8f\x0cV:\x14\xdc|\x0f\x8a\xdd^t\xa5\x17\x80\xf6\x9a\x1f\xb3Mk3\x0c~\x89\xa1!#$Ax\x10\xda\xc3\x13\x8e\xa1\xb9\xaf\n\x97G\x1ah!t\xe6g\xf9\xb9\x1f3&\xf7\x82\xe0\xb5\x7f$?$bXS5\xfeQ\xd7\x12\xa1Q\x0f\xa3\xed91\x133U\xd2\xbbu;\xaf[\xbf>f\xbf\x90\x80\xf7=\xdf\x0c\xe1\xd0\n\xa2\xfe>\xfb{\x99 \xbc\x15\x1d\xaaC\xa3G\x93b0i\x12a\xdf\x8eN\xee\xd0&(\xce\x9e7H=QDO\xfd@J\x86\xcc^\x12\x9b\x88\xb1[\x98\xd3\xc3\xca\x8f\x91\x16\xcaO\xe3\x8a\x19sz\x97\xb5\x9c\x85\xa4,\xb0H \x83^\xfc\x14\xdd\xb7\xb1%t9n\x19\x17h\xd9\xcbl!\xc9<\xfc\xb7K\x86U\x9e\xebL\x8f\xfe\xe3u\xc6\x8a\xc5\xf0&\xc4(l\xd7K\xdc7\x05\xed\xcd\x97\xcf\xd1\xc7\xac\xeeay\xfa.\xdb\xdc&y\x037\xc6\x1e\xcc#\xee\x10\xda\xe7#P\xb0I\xc6\x98\xc9M\x98\xde]\x81\xa8q[c-\xd3\xb7\x8e\xd7Q\xc1\x94\x05\xff\xf0q\xf1h\xcc\x1bjC~\xaa\x10b\x16\xa9\xae$\x9bS\xdc$\x86O\xc2\x0c*k_}d\xbd\xde\xcd\xdb\x02\xaa\tx\x88\xd6T;^d\xe91\x8fW\x8a\xceY\xc3\xab\xda\xc5\xa8\x1eZ\x16\xacJpj\xd2\x80\xc8\x11\xc8\x1d\xaff\xd1\xf1Z+\xb6*2\xa2\x8bg\xe4\x88Eo\xe5>a+\x15\x10\x8dVh\xae\x9b\xaf\xa5h\xad\xd0*$\x80pJ\xf6q)\xcfp\x8a!\x89P\xf3\xf6w\x17\x86\xdeWJ\x0e\x90X\xd5oU\xdd4\xbc\x9d3\xb1\x05I\rU\xc36\x9b\xc5\xca8M\x8c\x1cH\x1c"\xb3gA\xd7\x83\xecE\xca\x9fO|\x81]&h\t\x07\xe2?\x95\xefL\xd2\tL6\x07\x9e\x8b`\xc9g\x99\xcc\xfb\x16^\x89!\xe9\xf6+x\xa7=J\xb2\xf7\x04\xad\xee\x94"\x01\x00U+c\x8e53\r\xden\x9f\x80G\xe7\xefv\xf8\x08\xb4j\x93cy\x10\xbb\xe0\x03\x15LF\xa52m\x1a\x7f\x1d&Z\xce\xfd\x87\x984\x14\x8d\x16\xce\x03\xef\x92v\xcf\xa7\xe9^\x19\xaa\xb1s\xf1\x08\xa2\x8d\x9d\x8c\xba\x9cM+C\xd4\xcb\x08V\xf4k\xec\xf0\xd4\xfb\xfa\xd3Y?\xdf\x04\xba\x9b\xabL\'\x91\xf5\x07\xc2\xad#\xe5\xa5^\xdb\xf2\xd9\xdf\x1c7)x\xcd\xbd\xecY\x81!\xcf\x1d\xb9\x82B\x92\xa7C\xa3GC\x89\x80\xb5)\xcdEq\xfa\x9f\xe4Bc\xa5\xd8\x7f)\xaf\'\x9e\xf8\xfdo\x87\xa3h\xb2\x02\x17\xf6\x8b\xdf\x8a\x91{\x05M\xf0\xce\xa3H\xcb\xbe\xb7\x14\xfex\xbe\xcfj\xa8n\x15\xa6\x04\xd7\x96\x90\xf1|\xb1\x89fg\xbd&"P\xfc\xe0\x84\x9f\xe5\xab!\x06\xa8-\x89\x8a\x87`\xc2\xceLd\xab\xeb)h^\xe4\x1e\xcdE\xd5\xb3\x89P\xf0q\xda\xa0\x8d\xdbT\xc5\xaa\xf0d\xbb \xd5\xc3o\x80\xe6b\x1f\xb4\x10\xec\xdd\xed)\x98\x89E4\xaf\t)I\xbdjv8\xa3\x15F3\xdd\'\r\xb6\x93\t}\x06n\\zl\x90\xcd\x82\x8b]\x18\x13\xae(\x82\x1f\xd3H\x97\x00\x93\x9ay\xdc1B\x9f,B\xdao\x9b\xc2\x8d\xea\x85{\xa0\xf6\xf7\x99H\x05\x03j3\xd1\xbc\xd5\xcd\xb7\x11.C\x8c\xd8\x94\xbdz\xbcD\xe6\xc7\xd5G\xdf\xc9\x19\xf2\xbf4f\xbf)K\xb1e*\xdbJ\xd2\x9e\xe1-*\xc3\x93\xe9\xf5\xbe\x8f\xcfl\xb10\t\x9bo\x11\xda\xda\xd7\xbapD\xf1{\xa0\xf9\r\x13_\xe4\x17<\xf8\xa96\x10\xa5\xb6v\xef~\xe4\xad\xc0\xa3FJp\xd6\xdd(^\n\xa2\x94\x06\xfe\xc9\x01\x9f9\x10\x1d~\xe7\xd9f)\x98\xbfg\\\n\xb4h[NcM6\xbcQh7\xda\xb6W\xd0!\x95\xdc\x98)r?_[\r\x9e\x9f\x17\xf6x\xfc\x8d\xfcS\xf6r+\x96\xdd\x85\x1b\xa9\x9a1^\xb7\xfd[8\x13\xce\x8cw\xca\x92\xdb3R\xfe*\xb9d.\xbf\xd5\xfa\xe3\xa2-\xd9\xbb\x16\xfd\xa7\xe42\x879\x7f\xd4\xdb\xf0\x8c&\xef@#0uf\xaen*\xa5X*\'YE\x1b}\xe4(\xc8/\xbb\\\x19\xeb\xdb\xe8e\xcb\xea\x1b\xb6\xee\xc0\x97\xe9\x1bN\x8a\x84\xb5\x04\xc4\x06=\t._Z4\xc9\xc18\xd8|\x04\x1c\xbc_\xf6Z\x9a\xfc\x1e*}n#?\xd8\xd5\xcb\x9b2\xf2\xb0\x14v\xdfq\xa8x\x928/\x16\x9bk\xf5*\xf2\xbdO\x8a\xf5rq\xff\xdb\xa3\x83\x80\xa7\x95:\x1c\xe07\xf9\xdd\xfa%\xf5\xe5\xe4\xecfs\x0f\x83\xf6bS\x7f\xc9\xe9\x96O6\xa3\x84y\xa6;\x94RVB$<\x9eZp\t\x93\xd8\xfek-W\x94mj7\xefOf^\xb7\xf4\xb7\x8d\xf9\x87\xc6\r\x99*5\xc8[&^{\x9f-\xae\xbc\xee\xf6\x0b4\xba\x92u\xc9\xa2\xc3\x86\x8c\xebH+U\xceL\xaa\x9d\xa4\x9e\x1fg\xf4\xdd\xcf\xca\x80T5\xea\xe0\x18\xdc\xf6\xce\xb2U\\\xf3\xa7\x9b\xd3\xc1&\x94\x8fh\xe9\x9a3\xe7\xfd\xbf\x00\x82\x9f\x16\xdd\x10\xebw\xa2<\x9e\xd0[ \xfc\x87<\xb6\\\xa1\x7f,\xc7\xdb9\x88\xbf\xb2\xb1\xb3\x92\t\x1d\xa4\xc7\xf0\x8c\x06\x0b\xbc\x82\xaf\xfe\xec\x82\xe02Ge\x03N\xb3^\x0e\x9d~\x88Z?\xee|B\xbe\x89FT8\x8f\xa7<\xd2\xe2q=2\xa0d\tO\x86\x9f\xbc\xa4\xc2\x01(\r\xba\xc1\x01\t\x81\xdd\xcc\xde6\xc5A_\xff\xda\x04\xb7\xee\x1c\xe6[\x93\xcf\xfa\x17\xabAw\xc2 \t[\xa5\xd8\x04\xe3cg*\xbb\xad\x0cG\xc7$\xe7\xf1\xab\x1c0\x1a\xa7\xaf\xb9\x81Ty\xae3\xf3\x83\x8cr/\x1aR\x8a\x0ci\xb3+\x94\xe9\xb9\xcf\xadq$?vo\xcb\xfa\xfc\xfa4~\x10\x01e.\xda\x84\xea\x1c\x90\x02\x8a2\xbe\x85b\x87K\x9asr\x0b\xd6\x95\xe6\xe0\x87\x8b\xc6X\xae{\xf0\xb6\xedm\xd3\xa0\xd1sS\xb10p\xdfSW\x1d\x14\x80\xd1\x01\x9ai\xce\x9dr\xef%\xc28\x11EV\x14\x0e\x85b\xadU\xbe\xb4w;\xdf\xb7h\xaa\n\x1e;LL"\x03oI\xf7\x8cn*\xdaS\xc377\x98\x00\xa9\x16\xf4\xac\xd9a\xa0\x93\xccU\xc0\xc9\xa15>\x13\xdbb!b\x97u\x84,,T\xa6f(\xc2o\x0b\xcf=4|\xef\xc9\xa7\xd3`\xc0\xfa\x08\xfd\xf4x\xe8u\xecd%\x93:$\x9c~\xa6f|\xfc\xb9=\xe6\xec\xfe\xb2Gmr\\\x9e\x08`Ek\xda\xae2\xc6\xe1H\xf4\x83\xa4B\xa0\x9d^\'\x1e\xc9\x8d\x11\xcb\xec\x94D[=\x9f\x08\xe70o,~\xfc\x12px\xb42\xff\x99\xc2\xd2\xbb RO\xb9q}r\x03\xa6\x1e\xdd\xf3\xbb\xb3\xa0,\xb2C\x07\xc0_6\x18W\xb8\x9f\xb3\xd2\xc9\xad\xc3v\xb6fB\xfa\x89\x192\xc6\xf8\x1d\xd3\x84\xb4\xdf\xf7\x90\x81\xba\xdd\xbd\xa1\xe7\xde\xb8\xc5cd\x16\xc4p\xfaMU\xdd\xb5\x9e\x97R\xac\xcf\x9d\xb3K\xc1K\x8fn1\xd5\x0e\x9b\xcf_\x92\x8e\xfdx1\x14\x88\xee\xf0\x8cm\x90\xe3\x14\x08k\xfaX[\x1e\r]F\x8f\x11\x9f\x83?e\xfcdV\rX%z\\\xdfm@\xeb!\x00\t\x9a\xb8\x07y\x97A\x89\xc0\xa0\x13\xda\xaa\x887\x16\xec\xe2\x98\\{\x0f\xdejqfyAq\xc5\x18\xd9tQI\xba\xdbT\x8b\xae\xa4\x13\xf1\xcb\x1c\xab1\xd5\xe0\xee-\x13\xa3\xb7\xce\x9f-\x136\xb3\xce\xe6\xb2)\xfa"\x9bl\x94\xbe/\xb8W\xfa\x1a\xf4\xff\xac\x91\xc4%\xda2fd6~\x8e]\xd8b\x8b\xb4d|{\xdd\x80\xe9?iF\xf09z\x14\x9c\x02\x9c\xd1f\x84\xa8h\xb3\x8dK!\xb1\xd9\xee\xc7\xdb\'\xf0\xd4\xa8\x87\x90\xd7\xaa\xddVs\xe9 \x8cIP\x9d\xc8\x9a\xb2l\x99\x8eW\xdd\xd2n=\xfe\x16\xd7\xd1vxD>\x91I\xf5\x0e\x89"9\x06\xe9\x95^\x19\x17\xe3 \x98\x0b;:\xff\xd95Q\xa46\xc7Z\xaf\x15\xfdU\xe2j\x9f\xb5\x1c\xa4*\xff\t\xe0\x89a]Bg\x9d\x06N\xf0\x18\xb1\x08\x0c\xbd\xf1\xf3O\xd9\x05\x13il\x8c\x046\xab\x10?\xfd1\xa2\xba\xc4\xf7\x11\x13\xa2T\xf8\x8a\xce\xa2n\xca\x9b\xff\xf8NRM\xa4\xad\xb7"\xd9\x08\xa2\xb4\xd2e\x85\x1c\xa7\x11%\xb5B^\n\x1d\x1cx\xdb\xf4\xa6_\xb9`\xaeP}[\x9bq8\x02.\xa1\x9b\x10\xd6p\r\xe3\xea\x90\x8fo\x11Q\xc6\xea\x0f*\xee\xe6\x04yS\x8b\xf9\xbel:(t:{\nO\x91\xa2}o<<p\x0f%]v\x8e\xf1\x93@\x84\x15POmZ\xcc\xf4K\x1aZ\xb28/!\x9b\xdd^\x89\xdb|\x07u\xca\x0b\xac=\xf7\x80\xfce\x15?f\x1cD\x91[y\xd8|_\x91\x96\xc8\x8b\x1dm\xd7\x0c\xed\xf1\x17\x08\x9f \xfd\x8b\xa6\xbf=\xadh*\xae\x94J\x12\xec\x18=\x04\xdf\xb1M&N[c\xaa\xc9\xc7\x84:\x0f\t\xc8?f^\xb2\xdb\xecI\xc5\xca\xd2\xf7\xa4\xee\xa6\xf8\xf6)\x02\xb6H\xca6\x98^\xf6\xb3\x84\xae\xa7;\xf2\x8f\x80\x93\xf3\xd6\xfc\xbcAb\t\x07\x880\xd9\x1f\xf3\xb7?Q\xad>\xe2v\xca\xd3\x83v\x7f\xc5_\xc5j\x880\xe1\x96\x15yP\xd94\xeb\x05\xa9qR\xd9\xca\xb0\xbdW\x0cB\xe9\xdf,*\x93,<--\xb5\x89t$]\xf9\xac\x00I\x13\xcf4c`\xc7\xbaq\x11a-\x0c\x1co\x1b\xee\x83\x9c\xd8\xb6\xcf$\xado\x8a\x90\xd6}\x92\xb7\x0f\x91\xef\x14?z\xaf\x10\x12\x08\xd7\xd8;7~xb\n\x18u\xd9]\r\xc79\x7f\xc5\xbe\xdd\xb9\xf1\xf4\xf8\xe5\x9e\xa5\x1b<z\x9aS\x1b\xfc\xd3*\xd9\xf3(k\xd4\xdb\xd5\xc5g\xe1,\x12"\xe0n\xa9+\xc5\\\x80\x1e=Y\xfc1Tzd\xa9\x94y\x7f\xc2-R\xb1W{\xf0SHX\t\xf74\xf3\x18}F]_\xf8&]n\xa9{2\xa0\xf2@\xd4\x8c\xd2\xc8\xa8\x03\x83\x8a\xdbp\xbe\xc8\x80\xd0{\xa1O\xba\xa2,(\xdf\xbaD\xcd\xad;^n\xf3\x870\xf5\xe8\xb9\x88\xe7O\x95\xd7\x87+,\xa2\xec\x08\xd6N\\\xa3u\xcd\xc4\xd9]\x08\xe4\xc5S\xb4JK`\xc3\x88\x80\xa4\xfbk\x96\xc6\xeczE\xccz\x89\xd4\xd8)f\x89\xad\x7f\xe8\x96\xb4\xaf\x15P\x06G\xa0Le\x16g\xbfL$\xf4\x9f\xbd\x92\xa1\x1fa\xd5j\xe8\xdd\xe6\x17\xc8jp:\xd4\xa9*\xe1M\x8c[\xd7T+\xd8\xa5\xfc\xe3\x88\x84\xb8\xd6\x91\\\xdbz5\xb3\xca\xd4^\x8dv6\x96\xf8Ut\xf4y{~\x15\x00st\xf3\x92\xe7\xd5b\x1b\x81\x0f\x05\x88\xee\x0b\\=Aq\x83$\x97\xcfm\xad<\xc1\\*\xd2+\x12\xd2\xde\x92\x89C\xf9\x9b\n\x98\xfc\x8d\x02W\xfe\x92\xcft{\x1c\x13)<\x82k\x8d\xd0]\x94\xc7\xd9\x0c\xd2\x19\xe7\xfa\x86\xa5\x88\xe0\xe5\xa8h\x92\x87\xef7\xd4\'\x1ac\'\xd7\x12J\'\xc4\xa9R\x8chl"k\xb6Ep\xdda<.\x08#\n\x84F\x9fo\x01\x848\xa27\xd6\x0f7\xbc\xa9\x0b\x87-`\'\xf9;\x17\x0c\x82}h?-b\xd6\\P\xf9\x19\x8e\xce\x002\xbb)\x9d\xf6\x9fL\x16\xf3\xba\x03\xe7O\xb5\xaa\x89\xbb">\xec\xb4\x9c\x1f\x87t{AtO\xb6\x93>\xe9:\xe8\xab\x80\xaf{\x05p\xbf\xe6\xf9\xc9+_\xaa\xd1\x18\xe8\xa7`E\xcb1\xb7\x94\x14P\xd4a\xd0\xb9\x98\xc9S\x9b|4\x1b-&\x1d\xb8\xc0#Tq\x884YK\x99}\xb9\xc8y\x130\x99\xaaW\x10K\xbe!\xf4\xe6\xd5\xbf\x0e\x83\xf0\xf2\x91\xd9(gi\x90\xa0\xf1\x18\x86\xf6ee#\xe6hB\xfa\t\xaf7A\xcd\xefR!u\x99_\xc1\xb3\xc4t8<\x95z\x8c7#\xa9_\xae\xc4O\x18B\xe8C8\xb7\x14"\xb8\x86\xf2\xe8\x1cYx\xf0j\xd9\x85\xad\x1a\xbf\xb2\xedF\xb7`\xe8S\x84\n\x9d:[BDl\xcc\xbb0r\x873eP\x9b\x90\xe1K0\xc2t\xc3O\xee\xb1\xe4\x97\'E\x1e$rB\xf7/\xd5\xd8tl\xc8\xab\xd4\xf5bSsV\x0b\x94c\t\xe3\x964\x90\xa4\xef\x0c\xbfJe\xb2\xcbG\xd6 \x0eu\x9c\t\xeb\xf8\xc7\xe7_{\xabJ{\x19\xff\x89E\x11l\x1eZ\x07\xfd\xc1)\xbe\xf2\xba-\x81\xd1L\\\xa8\xba\xb5@LWEE\x92m\x8c\tf=\x91 \xbd\xbd\xa1\xcd|qQ\xcb\x8e\xcf\x9e\x90\x1d\xe5-\x16\x1a\x07\xa0d6\x9d\xa1\xb6~)F\x0cU\xe3\xe3\xdbA#\xd5X\xf4\x81\xa7+Mr\xdc_tB4\x96\xf5\xa1\xb1yz;\xfd\x9b9\x89\xd1\x03\x17n[\xe3\xd9l\x04bg\x02M\xf9\x88\x14a\x84\xb8\xf6\x87If\xdc\x1a\x10\r&8\t<w\x83\x82\xd7\xcc{\xfef\xef\x1d\x7f\xb0\xddz\xeb|\x13\xc3\xc1~\x1aKL\xb4\xcf\xf2\xad\x1d)\xb1\x07U#\xf1w>\xd4\r\x8b\xc8L\xc7\xb6\n\xe2\xe9\x90\xab\x88?4\xa8\xcf\xc82\x045H\x08F\xf4xf~\'\x1d\x0el\xa0LM\xbe[i{8=}\xf3\xac\xc5g\xccrk\xe5\xec\xa8u\t\x88\x1f\xcd\x11E\xa5HLfww\xec8\x85\xcb\x86\x1c\xce\xd9\x162K\xabz\x03Q\x97\x0c\xd5|\x93\x0e<\x18#\x95\xf1\xf9\xa6\xb1U\x82\xc1B/O$\xbd\xec\x91\x8d\xe9\xf6\xe2\x97\xce\xbbs\x82\xbf\xb8\xe0\xd9\x8d/\xef\x99\xe8\x95\xa6\x17uW\xc6d\xe4unO\x88\x84\xc8\xe5\x81\x0fB/J#O\xcc\xe4bO\x87"M\xd6\x8d{3`\xcf\xd5$\xbe\xd5S\xe3T\x1c9\xe6p!\xf7E\xa2\x06\x89\xc5\x02\xd5\xdc\x16l\xe9\xd0\xdd\xb0\x8d\x13a\n*\xda\x0c&\x1b\xf9g\xc9\x1d!z\xfa\xaa\xe0\x80\x19\x95\xc2~sI\xb1N\xda\xe9\xf3\x0b2\xa5[9\xae\xc6\xe3O\x04@F\x0cl/\x1a&nF/Yk\xff\xa9P\xcfX\xa2\x83\x04\x8e\xa8&\xd0S\xca\xf5 \xdc8\xd6\x96[\xef\xa0\xea\x84GL\xc8\xe7\xf8/k\xde\n\t#,\xb9I\xe5\xe4\xa1\x10O,\xec\t\xbc\xbd\xach\xffM\xc9\xf9\xd9\x91\xed\x82\xbd\xcf\x88\x12B\xe5\xec\x90\xd3%\xdb\'\xa2\xbdG/"H\xe6\x0f"v\xf5#R\x87^\xc0\xa7\xd2\xa7A\xd9|\x8d\x08QY\x1f\t\xcc\x15\x0b\x03g\xb4\x0co\xbay\x0by\xa1u]\x92\xbe\xc5\x00\x81-.\x7f\xb3\xfc@J<\xb1~\xb0UC\x1b\rs:ji\xee6\nvW\xb1\xce\xc3+\x92A1\x10\x96\xd8O\x8d_\xc3\x97\x80\x1b\xc1 \xec\xaf;F\xcbJp\xdd\xb0T!\xce-\x9dIe\x87\x87|\x99\x8e\xa9\\\xe2T\xfe\xc1\xe3\xd1\x81cn\xc8\xdc\x00\x12\x8fK\xc7\xea\xb2\xdf\xe5\xea\x8f\x0b\x0f\xb0AH\x8bk\x1e\xab@\xee\xf7o\x8d\xd6\xee1;9\xdc\'\xcd\x1a2*\xfb\x1e8\xf1\xb9\x05g\xaa\x1fs\xae\xd8\xfe\xc3P\xbf\x9d\xff\xa2\xdd\x90\xe84\xe4G?\x02\xdb\xdb\x85\xda\x8es6&\xd4>\xa2\xa4w\xc7y\x1161|\x890Yd2T\xe9\xb4\xa6 CZ%\xe5\x98\x05\xc7,\xda0&#\t\xa8>\xd7\xaa<\xa3\xa5W\x80\x1d#\xcd\xc4\x1d B\xde\xb3\xa5\xbf\xd2`\x9b\x14\x13\x19\xf4\xa4\xec*T\xfe\xe3X\x8a \xd9\xbc\xbe\x04\xbb\xf8\x8f$\x07p\xa76\xfa\xc3\x90\xacO\xa3\xd4\x17\xb6c\x90\x07\x0e\x9d\x83yRz\xb3\xb0!P\x96!\x8b\xe2\x9e\x07?\x85} \xa6,\xd1\xf4\xe3\xc3\xcb\x00\x87ec\x06\x97\xc8\xa3\x19\x08O\xd6(\xb0\xe1\x1dh\x11\xb4\xf7\xeaf\xb15\x9eU\xcd|\xe2H*\xa92\xf1\x9e\xc64E)r\xa2\\\x8b\xf2\xfeLa+\xe5\xac\xf0\xaee\x89m\xcb\xbc\x93\x90\xa05\xae\xbc\xc9\xc3\x8f\xbf\xbf\xd2\xe5\x13\x87\xf7\xcf\x95 \x7f\x8c\x92{\xfd@{\xd2$\xf34\xfe\xc0|\x95(\x83\xa8\xad$\x9f\xe5\xaf36?\xb4q\xc7#1\xb2\x88\xf5P\xf5\xc6\xb3(\xe3\xdf\x9eiJ>XR\xd4\x0e\xd1\xbeN^\xe5F\xb1\x1e\xb6\xa2c\x03\x0cM>\xc0\rl\xb8W\xa4\xd7\xd7\xa2\x9a\xda\r\x1cuMV\xa7P\xdbe\xeb\xb1^\\\xed;|k\x1fWw\x7f\xb1q\x94\x0ft\xb1>c\xdd\xf7\xd8\x10\x9e3\xa0\xb9\x19n>\xb3\xe4\\\xf7vX\xe5Np,(jNnlX\x96\xe0\x8b\x05\x08\x97\xd6\x03\xb9\xd0\xb8\x9c\xc6\xaf\x84\x15\xf2\x8biz\x0eiw\xf8\x8c\xea\xbf\xb8\x0cz\\\xf9D\x1e\xdc\x83\xb5\xf0\xb6\xe5\x11\xfe\x96=\x07x\xb3\xf5N3\xa0\xaa\xb6Y\x96\xc7\x9eC\xa1\r\xe7o\x14\xee\x15\x83\x1f\x02\xc3\xb6\xfa-\xc2\xe8\xec\x0c%\xa1\x14\xf1\x1a9\xb2\x01\xb3\x86\xc3\x85\x8dS5y\x83\xfcT\xc0/2\xdeTPd\xa5g\xe8\xaa\xf5\xb5p\x98Z\xb1\xe9\x89/%\xfe\x96\xedu\xc1\xb6\xf2\x82\xc4\xcd\xd4\x9d\xd6\xf0\xc1\x11\x98%\xe8q\xe2uw\xa2\xf3\xb9ri\xdd&=\xdd\xd4*}g\x01~\xfcDUg_G\x10\x9d\x01\xf5*\x95\x84\x94\xfa\xf4)N\xb7\x1f.e\xf5 \x817\xf4Iz\xeb\xde$o\xf8<\xc9r\n\xbd!$w\x8f\xf1\xae\xbc\xeb\xf5\xb2\xa1\xb8\xad\xf28p\x0f\x82\xf3\xd8\xcfm&J\\\xd5\xd5\'2\xf6qd\xe7\x07+\xc1~\x15\x9aV~\xd2\xde\xa4\x85R\t(\xd2\xc6|\xa8]6\x00\xc6\x9d\xbb\x9a?\x87\xb2\xc2\x8dD\x15\xbf#\x8dz\xb6\xdb\x0b\x8c\x89\x0f)s\xb4R\xdbIpG\xf3q.\x18\xb52]%\x833\xdeb\x7f\xf8\xf8\x80W%\xa7(\x9f\xb5\xf0\xf9\x8ed=V\xfa\x8e\xe8S\x00\x87~Nb\xe3\xc0\x05\x9a\xe3\xe3\x9aA\x95\xb3\xd32\xbd\x8b\x00L\xd7\xc8\xf0\xaf\xc6\xf1\x19\x1e\xdc{*\xf0\x83$NN\x07\x05\x95\xf2b\x01\xe6(\xde7r^\xbf\xbb\x97\x01\x0b=\xafR\xadN\xd1\xdaJ\x9e\xb1\x90~\'Z\xc8\xd5;T\xf7w\x0f\xdb\x14`\xbdf\xec\xb6z\xee\xf0\x91\xf1\x0e\x99\xafI\xd4Jr)Yx\xb3\x9e\xfd[\x81\xfe\x8e\xd0\x94I\xc7\xa8\x87\xec\x94\xf5\xe8\xab\x93||\x11E\xea=b\\\x94\xe6\x16\xf2I\xbd\x83\x9f\x9bC\xc32*\xdb \xca\xe9\xdbn\xd8\xa0\xe9\xe8\x01\xc3\xce;\x82\xdf\xc6\x1d\xc8\xe5t\xbdo\xad\xf1< p\x14\x14\xb0\x06\x1e\xcb\xdc\x8e<[!\n\xfb\x95n\x0ey\xc4U\xe6"\xeb\x89\x9dg\xd3\xd1\x86HD_\xe5k\x85\xb0\xe8P%\xb6\xe9\\B?ed\xf1\xea\x18\xfe\xa5\x07\x12F\xa81\x01\x83O\r\xd3\xa9\xe8\xde\xcf\xfbZ\xc5\xed\x19\xda`\xaaa\xcd!\xe1ek\x1dm\xb9\xe7~\x96\\\xb5\x87hE:\x94\x9c\xdeaj\xea\x9f\x13\xc7#g\xe5\xf8\xe5Z$\r@\x9c\x91\x9e\x85\n\x0fL\xc0Ts\x180$\xff#&\xc8\xc0K\xa2\xf5Nk\x8c\x01 \xc2=Z\xc5O\x93\x87\xb5\x89X\xa9\x17X\x05\xcd>-\x80\xbd-n\xd8X0$\xca\xfcj\xe0\x19W-<\x8f3\xb5\xb8^|\x87\xf6Z\x03\xd0>\xa2\x8bH\x9b\x83\xe7\x8by.\x0c\xfd\xfey\xbexGVVW\xbc\xae\x8cv\xe3\t=\x1d_\xe5\xd9Qk\xe8\xb3\xb3-X\xfdm\xcc\\\rf\xd2\x00\xda\xca\r\x8d,L\xe48@}\xb5\xc4\xc2\x18\xd5s\xce/*\xf0JX\xb0\xb8\xb0\xf2b\xefM\xfbz\x01_.\xc3\xdb\xb2/A\xd7\xe6\xc2\x01\xa9\x17\xce]\xb5\xb6\x1fZ\xc7\xec\x0fh\xc3\x11\xfb\xb7\xb9\x80\xbc\xf9\x0ea\x9fuB\x1f^g\xd8\x9d\xe7\xcf\xd7\xcf\xb2d\xc2\xce\xc9\x13\xe9\xf4\xa9\x9d\x93\x1e\x1d\xae\xd4\xdcmOs\x85\xac\xf3\x0eVg}[\nZIa\xb0j\x06\xbas\x96\xe3\x886\xdd^E\xae\xe5S\xe2\xabc.3pr\x0b\xd6;\xd8\xfb ?\xa8\x93\xc4\xcb\x90V\xcc\x9bP\x89|i\xaeu+\x02 \xca\x9f\xf3\xb9\xdc\xb9\xach8\x17h\x1fe\xbd{\xae\xd6\xde\xb9=-\xdd\x96a&\xc7(\xc8C\x05s%\xcd\x1a/Z\xa8g}Qn\xc6\xe3\x0b\x1f\x00i\x99]w\xb2+1\xe1G\xd3\xc3]\xfb\x89\x7f\xf5\'\x87\xc0\xa9\xcaXa\xe0\xc7"\'s\x86\xfb\x86\x82`\x89\x95\x1e\xad\x00\xe5\x05O\xab\xf7\x94-l4\xfd0\x18;+\xc6D\xacRG\xdc\xb4= T\xd1\x86R\xb52\xb6\xe8\xbd\xf5\xb2i\x9e:\xb5\x93\xd0\xb1v|7^\x0e\x01:\xfc13te\xa8\x06\xd7q\x97BE\xbb\xd2e%w\x07g)\xe3[Q\x13\x9b9\x17]\xb0\x11Y\xf9\xebe\x9eR\xdd5\xc7i<\xca\x85\xf6`\x8d\x89z\xf9\xa0\xca\xe7\xa5\xb2\xd5m\xb2\xe2j\xc2\xec\xef\x7f\xdb\x9d\xdd\x8e~\x8d\x94\xd9\xa9\x99\xde\x91\x83\xa3\xf1W\x8b@};b\x07r\xb2\xdf\x12\x06\xcf\xb8}\x11#\x12\x90\x104\x10P\x9e\x9d\xc6\xed\xd1\xcfc\x93\xd4\x9c\xfb7\x07\xf0iK\xdb!\xa9\xb7\x83\xe2O\xbf\xe1\xee\xa7\xe7e\xbf\xa0\xaf\xfa\xf3\xeb8I\x07\x1dQ\xc8\x99\xa4\x0c\x11?\x94G\x8d\xe5pEY\xfc!)]\x05\xff\x98n\xf9\x95\x03\x9dbI\xa2\x94\x9dqJES\xe5\xc1\x90\xc3\xe0\x84L\xb9\x95\xb4hl\xc6\xcf\xf3\x9d\xa7?\x1dT46\xa5\x13g\xfbb;\xa4\xab\xc0\xf4\x14\xc8\x04\xf0Q\xd0[B\xe4\x86\xd1X\xf1\x7f\x98\x9f\xd5\x84y\xd1U\xe9\x82\x10\xce[\x07\x87\x13{\xed\xbe:\x1e3\xbc\xf7O_\x14\xe0\xb0\t\xf9\x00Lo#u\xe2\xda\x8e\x96ZV\xd6\x9d\xb1\xb0{\xff\xe7C}\x08>J(\xef\x07G&T\xfax\x03E\x10\xc9\x8e\xb7R\x9b\xdd\xf4\x1f\x1efa\x07u\xc8\xc1\xa87\x8a\x94rw\x92p\xd3I\xe0\x05\x87\xff\x08\\pvLZ\xf244\x05\'\x91\xb1Q\xe4\xe9z\xce\xae\x1e\xe0J\x1c\x10\xdf\x87\xf1\xcb.xr\xf8a,\xb5\xd0\xda\xb9\xe3\x98\x07i\xac\xa4\xee\xfas\x0b\xa1\x95\x08s\x86\xc8EZ\xf1\x95\x95\xac\xbdr\x9e#">\x90\xbb\x87\xad\x9ad\xfa4\xa9\x01\xeeb\xc6\x84\x81\n\x9ab\x96\x8bx\xf1<iB3\xa0DY\xc2@M\n7duz=n\x07\x1c\xe7\'\x87\xb0E&=\x94z6"E6\xd9\r\x07L\x1b\xca\xcc\x87\x8a\x08\xf2O\xecV5\x8f\x83\xe2\x97=\x0e\xfe\x9e;\xac]?\x05\x94\x1c|\xc5\xe0\x9e(\xbe\x92\x12\x12\x1frT\x1cz\xfb\x12\xf5\xfbP;9\x17\xef\x00\xa1D\xc5\xff\xaf8R8\x9eX\xe7\xa3\x85\xcf\x1cg6\x96\x0f\xef\xd0\xe8\xe2\xfbC\x16j%\x0e\xd7#\xaf/\xf9O\xa7Fd\'\r\x19>\x01\x8a}.\x87\xde\xdb=\x85\xe4\x82\xf8\x0b\xfc~\x19&)v\xbd\xb2\xbb&\xe5\x93C1i\x07\xb7\xc2\xe6\xa3\x84\t?v0_P\n\xc7\xabg\xa53#\x18#\xc1\xe8\x9e\x97-<\x88\xe8\x9a\x05\xb0n\x87SY\xdb\xe2\x80r4;D\xbf\x90D\xa6\xfe\x1d\x1c8\x05\x00\x00xN\x10^\xb30s\xc3\x00 Lr\x8ep\x02\x00\xe7)\xd8\xe9\x8d\xfd6\x8f\x88\xff9\xbb#\xeb\x1b\xb0b,\xa39\x9a\xbb\xb9\xdb\x9a;,#;\xf8:\x9a/#\xdb\xf8\xda\xb9,#Y\xf8\xf2,\xa3[\xd89\x99\xbb[\xda\xd9-#\xfb:\xd8Y,#\x83\xbd\xc1\x96\xcb(\x0e\xce\xe6V\xee\xcb\x98V`KgG\x177\xb0\xbb{%\xc0\r\xf3\x9fq\xff\x96\x07Lu\x1f \xe8\x8b\xbb\xa5\xb9\x07x\x19]\xd4\xd1\xd9\xea\x8b\x03X\x0c\xe1?\x8f\x83\xffh\xca\x03\xca"\x0f\xf3\xff\xffU\xff\x0b*b\x13(I\x19\x00\x00')))
except KeyboardInterrupt:
    exit()
