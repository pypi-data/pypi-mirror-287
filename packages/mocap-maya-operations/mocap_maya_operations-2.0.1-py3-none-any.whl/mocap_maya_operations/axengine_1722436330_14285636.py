class WupiError(Exception):
    pass


class WupiLicenseError(WupiError):
    pass


from enum import IntEnum


def _axe_init():
    import ctypes as _c


    class Interface(_c.Structure):
        _fields_ = [('a', _c.c_uint), ('b', _c.c_uint), ('c', _c.c_char_p),
            ('d', _c.c_longlong), ('e', _c.c_longlong)]
    import base64
    buffer = base64.b85decode(__axe_data)
    interface = None
    errorList = []
    _axe_init.cpsrt = _loadCpsRT(errorList)
    if _axe_init.cpsrt == None:
        raise RuntimeError('Could not load cpsrt library:\n' +
            _formatErrorList(errorList))
    import os as _os
    interface = Interface()
    interface.a = 2
    interface.b = 10
    interface.c = buffer
    interface.d = len(buffer)
    interface.e = 0
    _axe_init.cpsrt.Init(_c.byref(interface, 0))
    if interface.e == 0:
        raise RuntimeError('Could not initialize cpsrt session')


class WupiErrorCode(IntEnum):
    WupiErrorNoError = 0,
    WupiErrorLicenseNotFound = -2,
    WupiErrorStateIdOverflow = -16,
    WupiErrorNoBlurryBoxHandleAvailable = -17,
    WupiErrorCodeMovingFunctionNotFound = -21,
    WupiErrorUnitCounterDecrementOutOfRange = -22,
    WupiErrorInternal = -23,
    WupiErrorNotPossible = -24,
    WupiErrorInvalidParameter = -25,
    WupiErrorWibuCmNotRegistered = -26,
    WupiErrorNotImplemented = -100


import os as _os
import sys as _sys


def _getWibuPath():
    return _os.environ.get('WIBU_LIBRARY_PATH')


def _addWibuPath(array):
    wibuLibPath = _getWibuPath()
    if wibuLibPath is not None:
        array.insert(0, _os.path.normpath(wibuLibPath) + '/')


def _is64Bit():
    import struct
    return struct.calcsize('P') == 8


def _isArm():
    try:
        return _os.uname().machine == 'armv7l'
    except:
        return False


def _isArm64():
    try:
        return _os.uname().machine == 'aarch64' or _os.uname(
            ).machine == 'arm64' or _os.uname().machine.startswith('arm'
            ) and _is64Bit()
    except:
        return False


def _isWindows():
    return _sys.platform == 'win32' or _sys.platform == 'cygwin'


def _isLinux():
    return _sys.platform == 'linux'


def _isMacOS():
    return _sys.platform == 'darwin'


def _getLibraryExtension():
    if _isWindows():
        return 'dll'
    if _isMacOS():
        return 'dylib'
    return 'so'


def _getLibraryArchitecture():
    if _isWindows():
        if _is64Bit():
            return '64'
        else:
            return '32'
    else:
        return ''


def _getLibrarySuffix():
    return _getLibraryArchitecture() + '.' + _getLibraryExtension()


def _getLibraryPrefix():
    if _isWindows():
        return ''
    else:
        return 'lib'


def _buildWibuDLLName(dll):
    return _getLibraryPrefix() + dll + _getLibrarySuffix()


def _getSDKPaths(result):
    if _isWindows():
        axProtectorSdk = _os.environ.get('AXPROTECTOR_SDK')
        if axProtectorSdk is not None:
            result.append(axProtectorSdk + 'bin/')
        programFiles = _os.environ.get('ProgramFiles')
        if programFiles is not None:
            result.append(programFiles +
                '/WIBU-SYSTEMS/AxProtector/Devkit/bin/')


def _getDllPaths():
    result = [_os.path.dirname(_os.path.abspath(__file__)) + '/', '']
    _addWibuPath(result)
    _getSDKPaths(result)
    if _isMacOS():
        result.append('/usr/local/lib/')
    return result


def _tryLoadLibrary(file, errorList):
    try:
        import ctypes
        if file.startswith('/') and not _os.path.exists(file):
            return None
        library = ctypes.cdll.LoadLibrary(file)
        return library
    except Exception as e:
        if errorList != None:
            errorList.append([file, e])
        return None


def _loadDLL(dllName, errorList=None):
    dllPaths = _getDllPaths()
    for path in dllPaths:
        file = path + dllName
        library = _tryLoadLibrary(file, errorList)
        if library is not None:
            return library
    return None


def _loadWibuDLL(dll, errorList=None):
    return _loadDLL(_buildWibuDLLName(dll), errorList)


def _getCpsRTSdkPaths():
    result = []
    arch = 'x86'
    if _is64Bit():
        arch = 'x64'
    if _isArm():
        arch = 'armhf'
    if _isArm64():
        arch = 'aarch64'
    _current_os = 'win'
    if _isLinux():
        _current_os = 'lin'
    if _isMacOS():
        _current_os = 'mac'
    result.append(_os.path.join('cpsrt', _current_os, arch))
    if _current_os == 'lin':
        result.append(_os.path.join('cpsrt', _current_os, arch + '-musl'))
    return result


def _tryLoadCpsRT(path, libname, sdkPath, errorList):
    file = _os.path.join(path, sdkPath, libname)
    library = _tryLoadLibrary(file, errorList)
    if library is not None:
        return library
    file = _os.path.join(path, libname)
    return _tryLoadLibrary(file, errorList)


def _loadCpsRT(errorList=None):
    lib = 'cpsrt'
    libname = lib + '.' + _getLibraryExtension()
    sdkLibName = _buildWibuDLLName(lib)
    sdkPaths = _getCpsRTSdkPaths()
    dllPaths = _getDllPaths()
    for path in dllPaths:
        for sdkPath in sdkPaths:
            library = _tryLoadCpsRT(path, libname, sdkPath, errorList)
            if library is not None:
                return library
            library = _tryLoadCpsRT(path, sdkLibName, sdkPath, errorList)
            if library is not None:
                return library
    return None


def _loadCoreDLL(errorList=None):
    if _getWibuPath() is not None:
        _loadWibuDLL('cps_wupi_stub')
        _loadWibuDLL('cpsrt')
    return _loadWibuDLL('wibuscriptprotection', errorList)


def _formatErrorList(errorList):
    result = ''
    for e in errorList:
        result += '\t' + e[0] + ': ' + str(e[1]) + '\n'
    return result


__axe_data2 = (
    b'YAAADTWpb/8s-IqK1inbTAeOaooH8RG4SDEAAAAAAACgAQAAYACAAMAAoAAAAAAAEAPAEAAAQAAAAwAQAAqbI+b7lci+HadJlQMBAl5UXWhJigSWG4YK4n3QIS0ZdIag1laaMf3VVbjahlGAt4gVboswcmX4zw6ldiZA/XCJ9FVHTMHL1oHmlatOZxzbThAF05qPwtqhbMlnNY1saEXR4YiCrkBncAfI0adAE6N0y0VMbvXQA8YYlb2dYBrtNsr2GIGXUtcEr8E9qjhgk3zAoa8gVvMDvMFg7QQImTofm80wrw/mArRQB2QpCH4kN+HAnNNaXw2IMZ+jP6xRDNtbQrs4HBilFbOiTb8dZ4iWwVtT9dZiesdsjq2eWap4DxD3Y+YkR0ztpoRA7k9dMshVPKknfReePmJunH+JBc0jDCy1hykv/MEpFxbkfBB39gQLnsit0VeprndC5aEd64g9Kgb2rwUTKFQfrRlfGvsQIAAACMAAAAEAAAAAAACgAIAAAAAAAEAAoAAAAEAAAAYAAAAEmY/X9XKJNIoZ8IRNZMPUyMA7qLGiWOOQLjmtikvsPQkeg4WrnJ61HE6YFeU+tFQrX9IKAxHsn6zGZQmwAAAABxyGtZUtkDaAg1PLLWKMJ1V+BXDDTKhAsU5gxJAAAAAAAACgAQAAcACAAMAAoAAAAAAAABbJZbAAQAAABgAAAA/klilGUqxPxCAaieYtm0VQ+ZYEly25CSvShzSolRsYujfnjOkkeeMDphCo4tw28ZLk4kyQ2NLexmODuTAAAAAI1y1M+WcRMaBOjnvQfXnHfqI4GaZeL4sed0PykAAAAAn1XMN./FXXQeAAA/dwpzWBtKmswr4WVS8v'
    )
__axe_data = (
    b'5C8xG000UA5C8-K2mlNK3IG5AbOita<OBc!1ONa40{{R3Py+w}gaH5m1ONa4!u<dL1ONa4ZUF!QFoFSUFoFRXpaTK{0s;gF9qTPH3I+%&hDgpm1OoyvB{3B+69xlS1PTlcS4l!uEmK)jR7FiwF$^#Y1_M<D0}KO9P)jf#7Y#5lFflMOFfcGMFfdvd4Kp<{GBYtUGc`FiIa)9!F%>Wq1_M<D3JeTaNkUaEQ(03~MNLyN3@{1?162eA3<E<@OE69_5C#V-hDgpm0s#gED}e+6Ap<%91k-ntXa5D=6K{~sW7I^~O`$;y{%C+W(4)4wjd4S+nvbi)DPf8Ft|m3ZG71D#F4Y;qVYvB#5rGu|Kr;2F9h{rkbRT_`O11gKT0YdUf)xO{hA#6J29q~0Ryz2K6Lt#eI<@Mf6EG1l4+aBO9TNco{{#gv0|5a5FbW0;DuzhTJp=;+13&;UJpvs7|D@<)(Qb6;n8gXKY|scRWVh;U0Z=q7fN0hf0vvX|XB5qh4W0BWpSfey^nnB`*%FzZ$ksi#5ZnL&KK}pz1ONa4v;hDBFoFTFFoFSIpaTK{0s;iG&~L9W3I+%&hDgpm1OoyvF)<Y|69xlS1PTlcS4l!uEmK)jR7FiwF&How1_M<D0}KyWX<~IPP;zf%bz^jCZ*DLi7Y#8rFflMOFfcGMFfdvd4Kp<{GBYtUGc`FiIa)9vF%U2g1_M<D3JeD}FfcMQI5aT~FbW0(RRjYJ158j$FitQK1_vsJNX|V10R{ytfdl{{13CZ%Q|;uCAR8(PpBrw&GFb)g7U|lDdCcAmF_xC@-seLZaw(|^AGqah%$9Dh^hZJuAZ|m;J(J2DffWFhpz`%2fI3;mt0!JNv!e86!tXbN6#zgo^`;%1o7i+8eUwVI`NUd2)UcycFi<cL1_M<c69EDL1O+ey0RaFo4+aBO9S;Ek{{#gC0{{;IFf0ZND+U1s0fO5_0|5a6{{$QVb{OAs16!7C|9B7Ifn5Rr-+^8M|KEXM0sk-x1_&yKNX|V30|Em;05ClQ9RTW$U-H-ofM5Ou0VlN5ho>d#j_#t2!++9_+S>vgGuY`Wt*#XYs4{C%!E-9m7}x#kzV4Oi!hlvw000I62mk~C1^@s61ONa4d;tIeFoFSiFoFRnpaTK{0s;iG&|VlY3I+%&hDgpm1OoyvCNUK-69xlS1PTlcS4l!uEmK)jR7FiwF%2*a1_M<D0}KRGZ*O!k9v2NUH83$SF)%PNFfcG$7Y#EtF)}kTGBY(fH91-^F)<Y|69xlS1PTlcS4l!uEmK)jR7FiwF&How1_M<D0}KyWX<~IPP;zf%bz^jCZ*DM7Fc1a@DuzhTJpus+1uKCB03ic900c5O-B9JArKvdLh(|UP5;-QZ!ut_YcfKKrMZKor6zuWQnFWt`1$cn%JjH|g?+Ll&fY**N@=Adf0C=QmSylFTGD+xHY${zy`@8DK;(`?bl%VqUBY-+t#;Ye@JF}wnWy0?_qZTj}FcJm>RUH!n0sjODFa`ku{{jI4FbW0;DuzhTJp=;+13mySI|3XsGB%9Ju?GRlw)*q11NjapqGVY}!-O&t{g%f98+8(|n{r_PaK1#?$*6vGYs<;o`yLamnPW?_hyVZp5C8xG000UA3;+NC2mk~C3IG5A2mk;8Pyhe`KmY&$a|-Luh(z`Lz&@te!#!gFvi$iC%Ry8;`u-^700000C0@zhW?Qx}E?+jRIctAI>}mG-Q6M6-Y=|+Z00000000I62mk~C1^@s61ONa46aWAKxrQ$D6$X<xFIGDEiW7DU={mLQz#jkrZ~y=R0RR91v`laz8QZYJ0E@kjWvAXjE2vYpb1Ni<ADaj@F6g<|Pfbq!JX7&AYXx0D(s*|Pqh6+v(H2sJ`eJs??^s-BCT??;GSsYavV3v;uMTB9z!N6aXRZWkBi|l<*;v#;N$Yi;wa*><V<e8{MzgY-r|+yOehVb?=ZA0yBE95ac!=L^tib1Q8${~FI=*=Vd%QAL{JT;TbT0NMt(zjcI7T&91#QzmG_)3_Z;QZO<!84G+^TT2mBF(AQL6LYy%k>>@JZrd;56#fKO3Uz7#D;YQPI^1E+GMTgQPa-zd~WyszsEc_q=!lUy`9h3NmvwPom<kO)shaLlm2_A`$+v`k^J~$KtHl5t1tPwhi0u;wP$Q<eocHZLEd#+TT=k;>X6ZNW7qr2sKrh(ijHS*_KLBp6IlmgY@GxVX$=3@{&^j!Q^9`&Pa*}Lk1)tCm5x)aVrns%3{8XNU8j;p*i1#*cSU;*`c!i6+vvq@>$B>V);vzW!wd&uw0Zd1(9!V2qI?5<oj@74MZ4)gWq>g^isG4kvN`m238syZ(e`<10v7Wpq|wFW4HaugKyJR7TkRFH!7~+H$56peS6<q={Dnlu{2RCy-<EMJ!K5HBfeCY5l&)!gRBGFcCr>TyG1B_YZ}Ph#u;awSGaKDDr{Ke3PhC@z*FNyl9g={wJg^UXG#XLg?uOc_FZGuwMLW+g1VjtYMr}j1F)5*Lm~>U06aLT5OjmJ$m;D?A*lPFTBbxHo$W)jYViJ*V}ju4$T^)0_H?RvWPMrJK&#qCsOi~;f$2HFt<q7wR%*sr4V+ePH5I4!q^|A}i>DT`r47%vmVMacv;6GI^S)F4w4I3Dcf`XFOI!vJdjbK?lAKWWn}n3WOA9C{^qJH229)FX{HiZiZ<3}@K<>a%0P?}O)Y%3-5SaEH>tb`9|8N9doSlrTjU7~La2dQ~qt72Y%YPzeTW3=u-CcoI0gI$yc(vb;H6kN+3;FR%4eN^b=4%3RB3e?(_BCqxO_OIL4g13Q+|RLmkOOYEC^AX-U@b#q%V=Ubw9KP}O&q1zC+p4_HHi3Rp7`ZrZZs12z5R?>M9`5$gJ;&<e`<{M;a3rj((sLfDuI9La@&WyqXj{NmD3*sNTK@?HZCm3`}}hc1lO=N#}Y{MM-Jj^-oN%Ko*ZB<uf?B*<qFO8yAvT3{|(kh)BuWgfgxyXj!nl$9n<$*({o@vZZ@BJ#qUZW3M}~Pa7Xf}BIipok+w5n<|9p?=Y1aIAcCl1Y0i6bu1l1hzW^W-0ABNzE0nl$!sDG=B;z2F7fwrS4t(Q@?zlW%{aPkAw9>pOq9QOHAMIY&nc?I|<^`OOZH6r^7@4e#ZZli)UYQT0TUg!8v+&S1b*6L2zE$TWxjjLun!2n3s>ZL;_h4MVQkJ4z3yS(!ctm5sKZ5Mpec(O(jfki&-v)PIqCVr7p#Yhv^Q{FGNMUoB=%m)uAR|uH-?n6BtS5(_!`%Q^&ti2o>gHrl3WDlpPsLEPB0jC!6KdhiSQxo*mqq9vP7)epfCk<LO4U2}Bl0zHs8vD+&(KQwqb`M=0zM(bYOF`pD7J%Z44_7q<?w9M*=z*v0&C0?FdGg9^r}JNjAHTF{oDX`mVhP~rux;@cQj>?2MP-vicUZe!wtg^cV;WFYw^%!*U$~jNTcrSO0BB=*QN9IUujXt#gz^>|JU5pAMGA}L#gZ)mu-q2eKDO}8h@P?H9Ar--R<1|{za*bIx^fD_tT{AcvqxAK)yfY)^{uvsJMf3DRw@o!LL0<k_nvO$!XDH+xDwnXZ=>pCg1hH3W^%zU6B2`B3M~B)Hz#O5x9VPSxJ*0RXY)_+?`5n{OCBwE;ti0Jt+Rv@C3bkFnpU3E}^mb-Kusx?IpWWFP=LTDuR1M6xj?KyG`96*8z#Z)A=iMT8(y@`?|M@I@d)8+rGZv6=&USJ>O<XwIWki`$4c(R~s}i(1@X=CIHgm>Y*TrGD!ww(R<z7i$fTGA_FLO{2*ustG#=IL8&{n(9RKqf(CVDawcB&@jm3O1soEDO)MW?O78RrST@-O@BLR3-VX3|bhJmPzYL3#52YzxY+K)Er#AFpZ|q^$K0qcO3T8zdcQyt3ZnI3lB2h5c44I;y0gufJ+t!%W#ixkFp3jP&sovkClqrbS8PhRA%sr{6Y$=$uyehu+B4RvXk|IPLKS?)gnjQ2VB#q3JzHxg|#Ov|HA@ou?-(h7^Y;J?x%I760xrN$^1Jl0xk(W##erxeW5KoyqS3s{#HC-iO{l2j=I#x*NL*ekV&+J9jW6Jwt<5znl2-ZIJKq)_0i+M>WgM8uS)5Kynt_6-#n5a>xeuP;b>15@DPy^z)Tl1-5(3)ct2skIgsvY&<y|I@C<iv1oqVyL))=e&9Whq_A@JM$az}NJtlC&i?8jXRzplIBktrmEQF{Gd$??a)5T^9N?o;gVLCfigU?`8Fi1jZ^*#Bm%71$@126x4p8+aW%LI~-6ock^~e0SoA-xjkK0R;4vCSPc?6zOj7D5_<MQAE5)(2_Yq5i+D9hV{l#UjY(wB@M0DtyT1lcjRp7T-K;~L?h?EmTvw_fE({F@XrEW>h!)BZg5Rvv1}6EaI2p~N{ly91xEGhg<HXj$_FtvEzG&gv*FynCw)HD=wfvMPxCcgHTc_!wbR~ghaeQg)ji>Ve3LtFEK-h@);6`_gZCAet#O*LrVBS{F!Nb$bfG;<0v25tx7K9%!o+xpXPpEGGw5*hA^p;44U_;)o<=7qdPTnRSrY39p=?}s7*44ek(pC6Gk6=Wu%46<bomKyiHGI*aY)XDZ^Vv>H&$2BpixXu;kse`*lzsOlmIfESuqOM%k)FoPUqL^fU{AQKEdC>TW-D3cdWA!%6-#;XS}=Ntss=CD7Q^|KJMP#*(WxQ0uMlXjSjC_EwBqS>Yi3RNV2puP7{7oR01uTP`;GWg5Q3z0aNBmfI^+3kLNcVAz>%nTGZy!wY&j&}N6~wQH3}Wt3z@UJG+YHvz_G%iX>4IolDBm35N21uEKtM!ZW98K5F-^G8GLH&Vw$l(zG?Yc1dLc=xIS>M@{c76B_h4ZT+2cP6y@^&55_i3tc@9da#2QLo{;yQ&`RQ|B;0F14;b|o@Fyp-N-#hORF>{U@+LO5N!gIeAs^9IpI5fq{@sw|hZAaJmxIgZH7v@82$-||S5S~WTOv)c!1m||-sw;U_U2Z3eD3+G0;w6aw<en(5#Vcxs^>F246G^}qN65C6rUx4tq87&Y-kOOacpX3sWeB=0ifG7Zi=0!jS&Ri<;mpZV)V)SimI7sDId&8GhM8?#Ai84EBow+tHYnBDh8tffQS=!981-OebIT|0R9T&i|4HUWp1A+EwYlzZ&pZG=x#(06zrTjAKQqVwp_;Y!6PWn6k-)`J;Vu1JXs<p+}{yzuG!cUJn)*4)zYs`Xx4)Iz&iQ9E>QZnnk?=+DRrNatWNf`+7;=WPfSt}2<3J9_y*#wCWYhx-k1E*M>p-rqkZ!9_1!Dm`iV(<CioBtVD1<R*ozK1{Q9>C=R6vRl_^C&n8Mj)DQ!-H=QPWL@+KQaO2W!c=XCaD{ZYF=`ab|7Z@<n}ZF$iF&WxONuuGmrVI}DMF(JN{;Av9V`MeJ$P<?8J+RvmM*_k)a9&rgfEKrZ>4HZtD%i@Z$R{hZ+2+K{xkmH4>+sc^VuGf`TNjV52F?`*S(~+ooWaWUK<U)g0lDgQ*0iVh#JmU}E&)TQACiXNR)rWuR6M9BX9(~V_`#AT)>Usa&gW_nHNkURe+9K{TBH(i|5Hw6lJ)M?<)U~UA2{y=Zm{T7>OuTmIXC}SQ`!Wt((gUvAtOX{d*^5EtxLGjGqN=Z?(x9o^tu`)I!Gj5Y6|ZpQ4AsKiZA`YadLs>wiG^@eiq?t1Z2Xeh@H<B90UL$I4>M1lPtQqeOp7#E<s)&w*~ORE!_#x$fRV{-o9M^#OMfX%lS){ZeTL;HrkiWHjiP*NnCv_9y*k?0YFJ~{&G`{Oywa)~0(TXgH&2pp?(BQ`HD;s-ePV14F!~0Gln>8L8`Lzv6E~*{jeid-niNLoZHPd&=^^Upy1W+m<?bjN`rll!UyG8m$su^$dzsTh@(w)@2fA^sC)64toJUjGw<8Pv8u%P%krrH8N0urzX1p(mpd8=$VU;}fYCyAPj3p@V#n^TZuA)IFyq{!%^OdKu3?S34JehTz^&kh#8G*RLo*p{x5&($TJocv4jhiAwMXC3q_b$uJwQAqQ%M^&m2z@d<abJ+qqv~m|3TwJe&o|f11?2+THlnI!q)qT94wK_ZnH?Rt)foO4r_l7tERBqPx9injX6|Kz>4%J8HY-ST!*3qviW#&z+2+h~wo;`_i9<VP?7to0f<Ps^qlbEjD-s?nP<IME7zs6beV%WNYalVjKWjGPT<U5|U#3f2KaLeb2|D(vv6?T;O{a74QK_V9?{1N5!jq*8fNPvR(lVpz)GMpEUu@ULt?OS~cBzZX%n9sAYbZO_y%w!|^1sK=;q^ZdD;O_}mYMa-{*WM*AFfUqheZhEYYS}`febAOJY@Kf7E?I8K3lto0-#xiyajme#G5exI@k|9MNx4}%-&_r-glo84n<j%*TT%szZBC!g|=ng=O6Zi-y_}vA?#S#g*~1N)(5-WIx%Oz#E7dgt!!Jmpy>A85{D<dti+xMBO&9r!(F=@AEK0~2_!)DsPS8sGr5A^3-Ot4FzL6`$+)k_?T18R(Tg>eaTOcCcFED8Xbs3?Jwz&4RxrTG%p{2XDxWnfU{8OZZF+O=CfnFn9=C7|QtKIc>1e%9em{Yn(3*OEDBG7<yb#?Y3zMt_kV`IAWc%-#Ol^JK!NMY3vA6x1x5+`Km?_vkl5kH9>tqyZ`<9U;8sc}kIQ&vT1b#wQRV{*9!Xo<=Xd2Mk0iJE1Ihs?K@*_G<@|X~Q;#(%^!Yt|;lzK8zI_dm!DOt9$=f0oUGNC7xvH}_9(xvDMC<LX(Gr893Mf!Zs*wy^_O_7zWPKF$n1A|crqNo0$<~X3nP06+mT9Mj7yuXea94}l-74ayMA()2&$hJa)1gx_!a2$!@lm@bMA~zVf-X1Phdjw!}{ugyiY7RJXgYhyKJFghe;)#qE*0rcun%t8lu0NiMq;P_z-@%yQpNapZr`{6l<K>Ut*C7MlpT(;i5Yh0xd(ogD2N-xZRPq&!K`ruPscABrdWTHilR?=;a{2JH>THHg$HLf`06NINUZ8H7>fnTlk5O?H@nwKXsIOLtkre(28<a;x3Ps1H++Q*PPaGfW*zzPjSOgHN|LxS2p>8y@!iEAozjmUo{nfcGDyBztp^{585V%J)CZ-KU20ZCMTMGp_mSZy^GP|CRl`ZMknad8i^ga`s0_-T{MgOoB1JYwU)7v#`@l0!1)=_QXufY(|(^3=Q4{er2gw2%J?`nvq;fnwukcLwZ^wZF=zFYap<G^`?9xAv^&gmwze7g>-{Cmmc@1EXf2!qgdBk8i%5@7+loYOXi%2HJ~5?~G6stX{ldhnO7xa_{`K8y+@FDpd(yzd)27)9opersZo`tKGS-1;F1<HS-@)hTjw`l<U8qsMxTs7Cqb350eBuJ|3IgFKshLv_YMgT}#q=LvO84;0X9!|e-WPbNJ@c*0alAe7X_k7P#5Q5dbIHkKEiCdB%yeNfF@$FNU=<kQE(jH;_-Q2$<}rX7KK_T=i^ELd+UYmnYGN+Sr+cQRCRVXAvELcaZ?>D0@4JV+tBCb5kCZOuI0HNJvz`B{^K`rQE+uPtD>oe7ti$p*H2*l@308<b*r!o#EN($wNxBcRFaRw-E=>-t^o+sua|w&V5B;$BMJyfv=z_L_t_rFJ+<deTJ1B)s2~CvvBIvz>bEzo=~MZo=a0n3imuRGFELmMCV&N-xaLt`{)}#P8)YGtn8I=b@V0)O{XGlrmF4S>qR|33nJ%re^{}j85Qd8zNC7{<cS^B)RQ1>r=pi6n!j4bjzvUQuf9AMVE%{9am2-&^-+J`7ny03e4<NvL|9=E1?tmu3{N4ve6wwk#9NsZH}OD2c|8AeU16)&Cj+;+!Vh>U)7U@#V>dV&%e7A%<)r&@?{M~t<@EZUdnlA2$PzJPzgr$D-*=be<r6B7O1*6*MGnO$ouojqB7&?jQeu{XHPth284Eb(yeO3uPVQ9N)@njH-uv4kk2hJYCQN|IZOjzWkA>B!lz$y_3T+05!;q9D!aDPKKSa(<eU4D&AQa?r*CoZwwzJpvMk3PEF6gm6wp@`U#yTr-JE?U%rIL_`o{2JEF+R=%)Qe{h{A9vXLMK1g1?mipUi)cwrLebJY=+4gicF4V&=Z9UK<k#(jE8dj$%@4(fxajvi~>qzg?=_fO7Mr$F6-uxVh4UVIklRBs(kQ`K+{|Vmc>P(BM3s$Ykp|X8IebQXh5Mdu9u4U_8beVr};8Lo$>U9wL3SDUzT94&4zrH-LC7m~bLvt?>5XofucBR|Mq+cOZ+hHPOa4n?r+St|)X#HlKZVW{|<?zpPidFqlGms707n@Y_rTYS&l%9OY83U5121L}Gje+N85u@USmXBCLo@VuRM6*WD$NVT<Ka-jJVcaao`Fu(CXyGYAKaWY-_;-m=l45eFvoFkA1Gm-6~$m6N_9`j8P1=)*neT2n7^eTsl0d3n&%ID?5Y%^4q{>MvE1AO`5M1AX8W4J^0*q(x~c&Y@w-S?hzLRmE^J)tt`Hwx2s-ZbNv8%)axGW0%K=ka+f^JCe7(<9*8`meI6E$g*_Jz|in;Q7}Vhn{dh_F=OU8rY+no+ZSE88?dF*NM9i*P5sG~2g@AyNa(q4NWUG8<7-fp9UAH!09dj|HC=lP&_eS#^a`J8rr^s54bbbGQn@{+RXNiPsXLH^2;&nYkmumueH_0x@aYXW-2VDY50vWL!1~5ZfII(#sK!+>yBaTKnq_*d6)`HMMQKo#oko_FR*J4q^h#*d!6$(IwtT4KeoOau|H2)UU#PY%i{mOGcpoDMd|*cDa~iLpSn?#@2I<1;TonZ100H0FH8U*T4|e~B$8@G+u09!@z@@Hh0jz}$yvXrAyWzlGdP>9GIQRlc^EBbXrPupfsz9LXAU2-D40>}?YfbZ~-Ol3=oCLkOVVeBY#z8mZ6zk+~;8^pNkK&-nC?+2d3$wkak6o>*%y_~d&Xf?P^++<h{1u=zuV2H}t|76)&7WY+{k_ssOKa0s7D_>>sf(^O_alfo>uv^&w8Dy)^HcS=HKE78%&Cg#3bqp{OfcC_cfv&fJ8hxO@|^#TM>HMa$GkTh8w~KS9fAbm7r@%iv~$#J4f0NoHgUiKO}N3qNAe7IVShB;7^0EOgV3V~AG}YbH!6AsYhle6{WOe^<|UI5gZ<!<HCk=$`W9bd3XB<0w1rPIN4yR@yK0%^W+sZO+LsfQn2k{Qo-xxW|HRX{TO$Sl>dtWuL@*LP%Gzbri-OGRH6y%D;o6hs-DFU_6M*+`xu#-~6kA2k&^4x3bJfRh>r|eX4+NX)xUQ!Dj(EV9f>KHb#*^`FlGl2WJjXQz@y%(vu%Zh<uHYNF#@m9Y=VlWsVr8hhmw)DeA^vRcnGED?TPc`nNC8vug0<jL)V-Z~bdC0KO9x{-EJ2@sm1@qg6~({wJIa(LLJ8ga0&dNvkt-7Roi(uYNJH}@b`F$(r?bn<d%A5+k>Jk3E3B~m!a(pgTD-Lzw_F_rMWGw-122_Y$D2WI-8|c5whamnxWg<*T(1y%Q|2Qf#WYeo$e@L8g_(lO_nsKH|5U&;6<MWPfwDR2&0^Vz{e4>$vqSLn+MN>CP5%&(9UpiNc?Je{VpgO|EDjW?*<JN<f{V9ihbSoJXLgbt00gtyKL^X4-|S9E$!%Vv4n_&7?W-o%VZhM_lH)URaGu&RqbnoZ*D@o$J|v!?@3-{?B@o4>5SisKM){L@6_vvRj2(L!f`x^8I2fCNb_c(aHgHu|y^zPQYMY5_P)f)<*akd=++AarRcJ70W?Hkm_z>AvZ#T?am92YL1Z^P^?Rc$NMRgnI+#Nyfn#3vG8&)V5Qp!w84Z-!D7*6QZ>|d;VGq#PuI;C50UhTaJ?S$dxvjv23UG0{kK25QFyJ&X>#0Co(yVI&jsM%|Hg^GN{Wo<zhM!2($MliiRwNVEUtsewJ;n&&2n)%X#yrLq3;d?P;7^My$nm4g``Ys`a(nn%~K1Z6ef2%9F^-F_M>whH6he)a(dLaUKA~16aB<xgYR^d+K$A}6EzwX52Ukwt}#36kH47;xUjVKme=qR`UtCnw8+x}yRcYUEu@~e6dq^sANS1QcCj3pN;0A5%O!idY7ndNs=^kbw-v}KIeFkL%tB2y^wafBRBbx{hOWYKdqitOjKf0dEF0hf8Id?HVeUBdF=#}jBR_nI;!3-KJ32Lhzc{=DMRJl+VTF^^H-tCC^c>`7@2yvh;72c>}Z!Gy{?5TtSjSe}jx3y%sI4V<MpBUUb}mx>fH8UM7J`K}9AJaYE6a5ncsH7b%VKVGH{1$rRvhTD({F`+}^R2D?~&@t{-E>_hZ;5pUxL<y(k$INTF!S3Wq!?Z9peyvO~P<4r?mB=Ha&^Pd@hnU{k{Vt$|DG{Ig(exR($7Y$&6KzS63&w=@;LnlV!&FblwxaH@Mf%z&(pB=?tdX+oP+dhsS`=PIhBH5$LUDLkynwi=E3SrM@6Tb4h944XOmqY&H&@4%awk2^^Ba%S)>ylH6O1bYp_1Rj5X(Nf&}^I1pE=vXP6lakYOVdh>-bBN&iTGrc3j1u11j`RAk9VspW)_(mF#-!<;+xjJ(77Anb9#~EyfgHH=9rN(7gDA;v`6qG=F4TdFrxF9np?kp^YB4Vw`dwz8i3V7$Ndf6BU(U1+7EAq)0IrONtbCJE#T_(>)C*yy`S9p*<7*k75o@HMPk8S-pw%h?dj+CIuo+;P^|H)^}Tfu$ceJ92Bsu_EMZ2_ZxH#hLu~^=u=vVwE+avL@QINUv1x5V7i@dIdb5u(BbeG9XuAyuH5{Y?YSqnUCyZyuA3bo%+KG?0tF+&9Ckbxxy5k{U&Sp%xzXUL0YHyQn-4qy5MAZ?U(f>Baw~AQy><^oniqJjmW;DXH>y9LUjvk&Cf}*|W<m@bbDg%pk>X#RvJl4->R#({zkdX?GkP2^q;{4Bt!XoUSSf}9zx~OOHOg|r-psi&7yWEjZO@H3D^XBnH)D2mb$OLQQFY3YT=Z9?><B2+hW?TlQuG*sN;m+>WP%JM4_)&D%`Uk-US-%f*Q#+nL0)pZk*Q6sfy`)Gfz*e-^x2x{QBtMALC@iRKL<*50(?=RBA@-@LW~SZYM#<Ymxt^;7}DfS8aiT-u#r5sM@lZ#XBB5yWbYBx);#9IF&rj@SzCA^Z!n&Aj#eb%UhyMuMdK8Ig0v(3Nwj@1eON=OH&jbObde{sXt?w$`NQ>^661-B6M`|%qj{=8+pwq4gA94JX5c3;79AaSsT}`dyXK45>?YwL3jtb5#X9HtN5%G9<NWQUkMXjKT_3#_{2Lcd5D#fA@cD)#UAsG4J{fWCICkQBAtHJj_eItf*j@(epdova#)`TdSm-JP?*{Bd+D6#X<K?z(yWBwAGInv^PhAl=1BS3;RE}cPi}xiSq*<Seg4c9ujVNOrNTi{XTt_BIZt#~XuyS!ch$-2JcY-fXBdolRZhrm&(<(oQku~jPe{QUZ{{g5(_xp6WCk<1;oDC!udL?u8%=t*!yoIk<_VOAgpaQ~Q>|)HQq8m*G2G|@T81hB?qObWtvI3;AIQRjlxfws_o17oGbdU9G1?9J%nHR&Zj_{cP6a{Ud(Eln4#z2^g51u;zNKUgnIzk5d{uvz)xoEq39V%FR8o5L5%DxgwpRnZn^M>vq^7j7YDpG~n6UzH-h~%79fKVsCm%;P7Wx<$Lgw~>+ZQ6@gr+plK7KnxfJCn~JzMIA-$g#!ZR$tI++N^Vl2DC&}8<C4bV{l|H&7eSjcGqk5ie}LzJ^!i7)Tp}uf=wt&T3JA;o3WS*K4T{l(@{ODEkIlGXHQFO=2N=ovYuvMxUiDjV^c|f?B4vVc8jY$G!QH=P_!_JTIVX`)r_5l#;YlL_Nvn>tX8CF`PDfJSnrgKLEdm4*<zgojeJ{E1JxtPu)wjB6}z{&0kgdp5H6Uh?5O+dx{p9pH;e`84jLpxuo5WKT(}(3qZtlB1U<0t<6dSBL#PAkzXkP&Y9eEf+st`8U^}LVw8B(q7Nq-rfEybr4}pLceUm~Pb2X+;`udN08qEnrFJh=rXzy?tt5fo&PO1-0{dmty+kwwA5VM9)a^|#38Hawe>k#_`VJr<YF&l^ki8n>~!sAx%&D;L>ryjwV7-eI}$K=xk3q*in5z)5@>Sa5;(Vc;@LpJk!+0bYB!1DCJe<tr^xB$PcRVZ^YMGo@yh!QOf'
    )
_axe_init()
