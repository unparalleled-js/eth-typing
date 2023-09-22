from enum import (
    IntEnum,
)


class ChainID(IntEnum):
    ETH = 1
    EXP = 2
    ROP = 3
    RIN = 4
    GOR = 5
    KOT = 6
    TCH = 7
    UBQ = 8
    TUBQ = 9
    OETH = 10
    META = 11
    KAL = 12
    DSTG = 13
    FLR = 14
    DIODE = 15
    CFLR = 16
    TFI = 17
    TST = 18
    SGB = 19
    ESC = 20
    ESCT = 21
    ELADID = 22
    ELADIDT = 23
    KARDIACHAIN = 24
    CRO = 25
    L1TEST = 26
    SHIB = 27
    BOBARINKEBY = 28
    L1 = 29
    RSK = 30
    TRSK = 31
    GOODT = 32
    GOOD = 33
    DTH = 34
    TBWG = 35
    DX = 36
    XPLA = 37
    VAL = 38
    U2U = 39
    TELOSEVM = 40
    TELOSEVMTESTNET = 41
    LUKSO = 42
    PANGOLIN = 43
    CRAB = 44
    PANGORO = 45
    DARWINIA = 46
    AIC = 47
    ETMP = 48
    ETMPTEST = 49
    XDC = 50
    TXDC = 51
    CET = 52
    TCET = 53
    OP = 54
    ZYX = 55
    BNB = 56
    SYS = 57
    ONTOLOGYMAINNET = 58
    EOS_LEGACY = 59
    GO = 60
    ETC = 61
    TETC = 62
    METC = 63
    ELLAISM = 64
    TOKT = 65
    OKT = 66
    DBM = 67
    SO1 = 68
    OKOV = 69
    HSC = 70
    CFXTEST = 71
    DXC = 72
    FNCY = 73
    IDCHAIN = 74
    DSC = 75
    MIX = 76
    SPOA = 77
    PRIMUSCHAIN = 78
    ZENITH = 79
    GENECHAIN = 80
    JOC = 81
    METER = 82
    METERTEST = 83
    LINQTO_DEVNET = 84
    GTTEST = 85
    GT = 86
    NNW = 87
    TOMO = 88
    TOMOT = 89
    GAR_S0 = 90
    GAR_S1 = 91
    GAR_S2 = 92
    GAR_S3 = 93
    SDLT = 94
    CAMDL = 95
    BKC = 96
    BNBT = 97
    SIX = 98
    POA = 99
    GNO = 100
    ETI = 101
    TW3G = 102
    WLC = 103
    TKLC = 104
    DW3G = 105
    VLX = 106
    NTN = 107
    TT = 108
    SHIBARIUMECOSYSTEM = 109
    XPR = 110
    ETL = 111
    COINBIT = 112
    DEH = 113
    C2FLR = 114
    DEBANK_TESTNET = 115
    DEBANK_MAINNET = 116
    AUPTICK = 117
    ARCOLOGY = 118
    ENULS = 119
    ENULST = 120
    REAL = 121
    FUSE = 122
    SPARK = 123
    DWU = 124
    OYCHAINTESTNET = 125
    OYCHAINMAINNET = 126
    FETH = 127
    HECO = 128
    RLC = 134
    ALYXTESTNET = 135
    DEAM = 136
    MATIC = 137
    DFIO_META_MAIN = 138
    WOOP = 139
    OPTEST = 141
    DAX = 142
    PHI = 144
    SIXT = 150
    RBN = 151
    RBN_DEVNET = 152
    RBN_TESTNET = 153
    RBN_TGE = 154
    TENET_TESTNET = 155
    OBE = 156
    EVA = 160
    WALL_E = 161
    TPHT = 162
    PHT = 163
    OMNI_TESTNET = 165
    ATOSHI = 167
    AIOZ = 168
    MANTA = 169
    HOOSMARTCHAIN = 170
    RESIL = 172
    AME = 180
    SEELE = 186
    BMC = 188
    BMCT = 189
    CEM = 193
    TOKB = 195
    OKB = 196
    NEUTR = 197
    BIT = 198
    BTT = 199
    AOX = 200
    MOACTEST = 201
    OBNB = 204
    UTX = 208
    BTN = 210
    EDI = 211
    MAKALU = 212
    SIN2 = 217
    SO1_OLD = 218
    ASK = 222
    LA = 225
    TLA = 226
    SDX = 230
    DEAMTEST = 236
    PLGCHAIN = 242
    EWT = 246
    OAS = 248
    FTM = 250
    KROMA = 255
    HECOT = 256
    SETM = 258
    NEON = 259
    SUR = 262
    HPB = 269
    EGONM = 271
    LACHAIN = 274
    ZKSYNC_GOERLI = 280
    BOBA = 288
    HEDERA_MAINNET = 295
    HEDERA_TESTNET = 296
    HEDERA_PREVIEWNET = 297
    HEDERA_LOCALNET = 298
    OGC = 300
    BOBAOPERA = 301
    NCNT = 303
    WYZ = 309
    OMAX = 311
    NCN = 313
    FILECOIN = 314
    KCS = 321
    KCST = 322
    ZKSYNC = 324
    W3Q = 333
    DFKTEST = 335
    SDN = 336
    TCRO = 338
    YVM = 345
    THETA_MAINNET = 361
    THETA_SAPPHIRE = 363
    THETA_AMBER = 364
    THETA_TESTNET = 365
    PLS = 369
    TCNT = 371
    LISINSKI = 385
    HPN = 400
    OZO_TST = 401
    PEPE = 411
    SX = 416
    LATESTNET = 418
    OGOR = 420
    PGN = 424
    ZEETH = 427
    OBS_TESTNET = 443
    SYNAPSE_SEPOLIA = 444
    ARZIO = 456
    TAREA = 462
    RUPX = 499
    CAMINO = 500
    COLUMBUS = 501
    AAC = 512
    AACT = 513
    GZ_MAINNET = 516
    XT = 520
    FIRE = 529
    FXCORE = 530
    CNDL = 534
    PAW = 542
    CLASS = 555
    TAO = 558
    DCT = 568
    SYS_ROLLUX = 570
    METIS_STARDUST = 588
    ASTR = 592
    MACA = 595
    TKAR = 596
    TACA = 597
    METIS_GOERLI = 599
    MESH_CHAIN_TESTNET = 600
    PEER = 601
    GLQ = 614
    AVOCADO = 634
    SX_TESTNET = 647
    ACE = 648
    PIXIE_CHAIN_TESTNET = 666
    LAOS = 667
    JUNCA = 668
    JUNCAT = 669
    KAR = 686
    SNS = 700
    BCS = 707
    TBCS = 708
    SHIBARIUM = 719
    LYC = 721
    TCANTO = 740
    VSCT = 741
    SPAY = 742
    QOM = 766
    OPC = 776
    CTH = 777
    MAAL = 786
    ACA = 787
    TAERO = 788
    PETH = 789
    LUCID = 800
    HAIC = 803
    PFTEST = 808
    MEER = 813
    BOC = 818
    CLO = 820
    TCLO = 821
    TARA = 841
    TARATEST = 842
    ZEETHDEV = 859
    FSCMAINNET = 868
    BNKEN = 876
    DXT = 877
    AMBROS = 880
    WAN = 888
    GAR_TEST_S0 = 900
    GAR_TEST_S1 = 901
    GAR_TEST_S2 = 902
    GAR_TEST_S3 = 903
    PF = 909
    DBONE = 910
    TFIRE = 917
    MODESEP = 919
    YDK = 927
    TPLS = 940
    T2BPLS = 941
    T3PLS = 942
    T4PLS = 943
    MUNODE = 956
    CCN = 970
    HUYGENS = 971
    ASCRAEUS = 972
    YETI = 977
    TOP_EVM = 980
    MEMOCHAIN = 985
    TOP = 989
    ELM = 990
    _5IRE = 997
    LN = 998
    TWAN = 999
    GTON = 1000
    BAOBAB = 1001
    TET = 1003
    T_EKTA = 1004
    TNEW = 1007
    EUN = 1008
    EVC = 1010
    NEW = 1012
    SKU = 1022
    TCLV = 1023
    CLV = 1024
    TBTT = 1028
    CFX = 1030
    PRX = 1031
    BRONOS_TESTNET = 1038
    BRONOS_MAINNET = 1039
    SHIMMEREVM_TESTNET_DEPRECATED = 1071
    SHIMMEREVM_TESTNET = 1072
    MINTARA_TESTNET = 1079
    MINTARA = 1080
    METIS_ANDROMEDA = 1088
    HUMANS = 1089
    MOAC = 1099
    ZKEVM = 1101
    TBLXQ = 1107
    BLXQ = 1108
    WEMIX = 1111
    TWEMIX = 1112
    TCORE = 1115
    CORE = 1116
    DOGSM = 1117
    DFI = 1130
    DFI_T = 1131
    CHANGI = 1133
    ASART = 1138
    MATH = 1139
    TMATH = 1140
    PLEXCHAIN = 1149
    AUOC = 1170
    SHT = 1177
    IORA = 1197
    AVIS = 1201
    WTT = 1202
    POPCAT = 1213
    ENTER = 1214
    XZO = 1229
    ULTRONTESTNET = 1230
    UTRONMAINNET = 1231
    STEP = 1234
    ARC = 1243
    TARC = 1244
    OM = 1246
    CICT = 1252
    HO = 1280
    MBEAM = 1284
    MRIVER = 1285
    MROCK_OLD = 1286
    MBASE = 1287
    MROCK = 1288
    SWTR = 1291
    BOBABEAM = 1294
    BOBABASE = 1297
    TDOS = 1311
    ALYX = 1314
    AIA = 1319
    AIATESTNET = 1320
    GETH = 1337
    ELST = 1338
    ELSM = 1339
    CIC = 1353
    ZAFIC = 1369
    KLC = 1379
    ASAR = 1388
    MUN = 1392
    ZKEVMTEST = 1402
    TESTNET_ZKEVM_MANGO_PRE_AUDIT_UPGRADED = 1422
    RIK = 1433
    LAS = 1440
    TESTNET_ZKEVM_MANGO = 1442
    GIL = 1452
    CTEX = 1455
    CHAINX = 1501
    SHERPAX = 1506
    SHERPAXTESTNET = 1507
    BEAGLE = 1515
    TENET = 1559
    CATE = 1618
    ATH = 1620
    BTA = 1657
    YUMA = 1662
    GOBI = 1663
    LUDAN = 1688
    ANYTYPECHAIN = 1701
    TBSI = 1707
    TTBSI = 1708
    PCM = 1718
    TEAPARTY = 1773
    GAUSS = 1777
    KERLEANO = 1804
    RANA = 1807
    CUBE = 1818
    CUBET = 1819
    TSF = 1856
    WBT = 1875
    GITSHOCKCHAIN = 1881
    LIGHTLINK_PHOENIX = 1890
    LIGHTLINK_PEGASUS = 1891
    BOYA = 1898
    BITCI = 1907
    TBITCI = 1908
    ONUS_TESTNET = 1945
    DCHAIN_MAINNET = 1951
    DEXILLA = 1954
    MTC = 1967
    TSCS = 1969
    SCS = 1970
    ATLR = 1971
    ONUS_MAINNET = 1975
    EUNTEST = 1984
    SATOSHIE = 1985
    SATOSHIE_TESTNET = 1986
    EGEM = 1987
    EKTA = 1994
    EDX = 1995
    DC = 2000
    MILKADA = 2001
    MILKALGO = 2002
    CLOUDWALK_TESTNET = 2008
    CLOUDWALK_MAINNET = 2009
    NETZM = 2016
    PMINT_DEV = 2018
    PMINT_TEST = 2019
    PMINT = 2020
    EDG = 2021
    EDGT = 2022
    TAYCAN_TESTNET = 2023
    RPG = 2025
    CFG = 2031
    NCFG = 2032
    KIWI = 2037
    SHRAPTEST = 2038
    OTP = 2043
    SHRAPNEL = 2044
    STOS_TESTNET = 2047
    STOS_MAINNET = 2048
    QKA = 2077
    AIR = 2088
    ALGL = 2089
    ECO = 2100
    ESP = 2101
    EXN = 2109
    METAD = 2122
    MEU = 2124
    BIGSB = 2137
    DFIO_META_TEST = 2138
    BOA = 2151
    FRA = 2152
    FINDORA_TESTNET = 2153
    FINDORA_FORGE = 2154
    MSN = 2199
    ABNM = 2202
    BTC = 2203
    EVANESCO = 2213
    TKAVA = 2221
    KAVA = 2222
    VCHAIN = 2223
    KRST = 2241
    BOMB = 2300
    AREVIA = 2309
    SMA = 2323
    ALT = 2330
    SMAM = 2332
    DEPRECATED_KROMA_SEPOLIA = 2357
    KROMA_SEPOLIA = 2358
    BOMBT = 2399
    TCGV = 2400
    XODEX = 2415
    U2U_NEBULAS = 2484
    KTOC = 2559
    TPC = 2569
    POCRNET = 2606
    REDLC = 2611
    EZCHAIN = 2612
    FUJI_EZCHAIN = 2613
    TWBT = 2625
    TMORPH = 2710
    BOBAGOERLI = 2888
    BTY = 2999
    CENNZ_R = 3000
    CENNZ_N = 3001
    CAU = 3003
    _3ULL = 3011
    ORL = 3031
    BFC = 3068
    FILECOIN_HYPERSPACE = 3141
    DUBX = 3269
    TESTDUBX = 3270
    DEBOUNCE_DEVNET = 3306
    ZCRBEACH = 3331
    W3Q_T = 3333
    W3Q_G = 3334
    PRB = 3400
    SCAIT = 3434
    PRBTESTNET = 3500
    JFIN = 3501
    PANDO_MAINNET = 3601
    PANDO_TESTNET = 3602
    BTCT = 3636
    BTCM = 3637
    JOULEVERSE = 3666
    BTX = 3690
    EMPIRE = 3693
    SPCT = 3698
    SPCM = 3699
    XPLATEST = 3701
    CSB = 3737
    ALV = 3797
    KALYMAINNET = 3888
    KALYTESTNET = 3889
    DRAC = 3912
    DOST = 3939
    DYNO = 3966
    TDYNO = 3967
    YCC = 3999
    OZO = 4000
    PERIUM = 4001
    TFTM = 4002
    BOBAOPERATESTNET = 4051
    NAHMII3MAINNET = 4061
    NAHMII3TESTNET = 4062
    OASIS = 4090
    BNIT = 4096
    BNIM = 4099
    AIOZ_TESTNET = 4102
    TPBXT = 4141
    PHIV1 = 4181
    LUKSO_TESTNET = 4201
    NEXI = 4242
    BOBAFUJITESTNET = 4328
    BEAM = 4337
    HTML = 4444
    ORDERLYL2 = 4460
    IOTEX_MAINNET = 4689
    IOTEX_TESTNET = 4690
    TESTMEV = 4759
    TBXN = 4777
    TXVM = 4918
    XVM = 4919
    BXN = 4999
    MANTLE = 5000
    MANTLE_TESTNET = 5001
    TREASURENET = 5002
    TNTEST = 5005
    FTN = 5165
    TLC = 5177
    ES = 5197
    HMND = 5234
    _OLD_FIRE = 5290
    UZMI = 5315
    TTRN = 5353
    VEX = 5522
    NAHMII = 5551
    NAHMIITESTNET = 5553
    CVERSE = 5555
    OBNBT = 5611
    ARCT = 5616
    TANSSICC = 5678
    TSYS = 5700
    HIK = 5729
    SATST = 5758
    GGUI = 5777
    ONTOLOGYTESTNET = 5851
    RBD = 5869
    TRESTEST = 6065
    TRESMAIN = 6066
    CASCADIA = 6102
    UPTN_TEST = 6118
    UPTN = 6119
    PEERPAY = 6502
    SRC_TEST = 6552
    FOX = 6565
    PIXIE_CHAIN = 6626
    IRIS = 6688
    STANDM = 6789
    TOMBCHAIN = 6969
    PSC = 6999
    ZETACHAIN_MAINNET = 7000
    ZETACHAIN_ATHENS = 7001
    ELLA = 7027
    PLANQ = 7070
    BITROCK = 7171
    KLY = 7331
    EON = 7332
    SHYFT = 7341
    RABA = 7484
    MEV = 7518
    TADIL = 7575
    ADIL = 7576
    TRN_MAINNET = 7668
    TRN_PORCINI = 7672
    CANTO = 7700
    TESTNETCANTO = 7701
    TBITROCK = 7771
    RISEOFTHEWARBOTSTESTNET = 7777
    TSCAS = 7878
    ARD = 7895
    DOS = 7979
    TELEPORT = 8000
    TELEPORT_TESTNET = 8001
    MDGL = 8029
    LIBERTY10 = 8080
    LIBERTY20 = 8081
    SPHINX10 = 8082
    BITETH = 8086
    STREAMUX = 8098
    MEERTEST = 8131
    MEERMIX = 8132
    MEERPRIV = 8133
    AMANA = 8134
    FLANA = 8135
    MIZANA = 8136
    TBOC = 8181
    CYPRESS = 8217
    BTON = 8272
    KORTHO = 8285
    FUCK = 8387
    BASE = 8453
    TOKI = 8654
    TOKI_TESTNET = 8655
    OLO = 8723
    TOLO = 8724
    ALPH = 8738
    TMY = 8768
    MARO = 8848
    UNQ = 8880
    QTZ = 8881
    OPL = 8882
    SPH = 8883
    XANACHAIN = 8888
    VSC = 8889
    MMT = 8898
    JBC = 8899
    GMMT = 8989
    BERG = 8995
    EVMOS_TESTNET = 9000
    EVMOS = 9001
    BRB = 9012
    GENEC = 9100
    _OLD_TFIRE = 9170
    COF = 9223
    DOGST = 9339
    TRPG = 9527
    QETTEST = 9528
    TESTNEON = 9559
    MAINNETDEV = 9700
    BOBABNBTESTNET = 9728
    NETZT = 9768
    PN = 9779
    CARBON = 9790
    CARBON_TESTNET = 9792
    TIMP = 9818
    IMP = 9819
    TMIND = 9977
    AGNG = 9990
    MIND = 9996
    ALT_TESTNET = 9997
    MYN = 9999
    SMARTBCH = 10000
    SMARTBCHTEST = 10001
    GON = 10024
    JOCT = 10081
    SJ = 10086
    GEN = 10101
    CHI = 10200
    PWR = 10201
    AA = 10243
    _0XT = 10248
    TWLC = 10395
    JADE = 10507
    SNOW = 10508
    CCP = 10823
    QUADRANS = 10946
    QUADRANSTESTNET = 10947
    ASTRA = 11110
    WAGMI = 11111
    ASTRA_TESTNET = 11115
    HBIT = 11119
    ISLM = 11235
    SHYFTT = 11437
    SRDXT = 11612
    SAN = 11888
    ARIANEE = 11891
    SATS = 12009
    TZERO = 12051
    ZERO = 12052
    BRC = 12123
    FIBO = 12306
    BLGCHAIN = 12321
    STEPTEST = 12345
    TRIK = 12715
    TQNET = 12890
    SPS = 13000
    CREDIT = 13308
    BEAM_TESTNET = 13337
    PHOENIX = 13381
    SUS = 13812
    SPS_TEST = 14000
    HMND_T5 = 14853
    LOOP = 15551
    TRUSTTESTNET = 15555
    EOS_TESTNET = 15557
    MTT = 16000
    MTTTEST = 16001
    GENESYS = 16507
    NYANCAT = 16688
    AIRDAO = 16718
    TIVAR = 16888
    HOLESKY = 17000
    PCT = 17180
    EOS = 17777
    ZKST = 18000
    STN = 18122
    POM = 18159
    MXCZKEVM = 18686
    HMV = 19011
    BTCIX = 19845
    CAMELARK = 20001
    CLOTESTNET = 20729
    P12 = 20736
    CENNZ_A = 21337
    OMC = 21816
    SFL = 22023
    AIRDAO_TEST = 22040
    NAUTCHAIN = 22222
    MAP = 22776
    ABNT = 23006
    OPSIDE = 23118
    SAPPHIRE = 23294
    SAPPHIRE_TESTNET = 23295
    WEB = 24484
    MINTME = 24734
    GOLDT = 25888
    BKCT = 25925
    FRM = 26026
    HTZ = 26600
    OAC = 26863
    OBGOR = 28528
    PIECE = 30067
    CERI = 30103
    ESN = 31102
    CLDTX = 31223
    CLD = 31224
    GOT = 31337
    FILECOIN_WALLABY = 31415
    BRISE = 32520
    FSN = 32659
    ZIL = 32769
    ZIL_TESTNET = 33101
    AVS = 33333
    J2O = 35011
    Q = 35441
    Q_TESTNET = 35443
    CMRPG = 38400
    TTRPG = 38401
    NRG = 39797
    OHO = 39815
    OX_BETA = 41500
    PC = 42069
    ARB1 = 42161
    ARB_NOVA = 42170
    CELO = 42220
    EMERALD_TESTNET = 42261
    EMERALD = 42262
    KETH = 42888
    AVAETH = 43110
    FUJI = 43113
    AVAX = 43114
    BOBAAVAX = 43288
    FREN = 44444
    ALFA = 44787
    AUTOBAHNNETWORK = 45000
    TFSN = 46688
    REI = 47805
    FLORIPA = 49049
    TBFC = 49088
    TNRG = 49797
    LOE = 50001
    TGTON = 50021
    OPSIDE_TESTNET = 51178
    SRDXM = 51712
    DFK = 53935
    ISLMT = 54211
    TORONETTESTNET = 54321
    TETH = 55004
    REICHAIN = 55555
    TREI = 55556
    BOBABNB = 56288
    VELO = 56789
    TSYS_ROLLUX = 57000
    SEPPGN = 58008
    LINEA_TESTNET = 59140
    LINEA = 59144
    TKM_TEST0 = 60000
    TKM_TEST1 = 60001
    TKM_TEST2 = 60002
    TKM_TEST103 = 60103
    AIUM_DEV = 61800
    ETICA = 61803
    DOKEN = 61916
    BKLV = 62320
    MTV = 62621
    ECS = 63000
    ECS_TESTNET = 63001
    SRC = 65450
    MCL = 67390
    COSMIC = 67588
    CNDR = 69420
    TKM0 = 70000
    TKM1 = 70001
    TKM2 = 70002
    TKM103 = 70103
    GUAPX = 71111
    CKB = 71393
    GW_TESTNET_V1 = 71401
    GW_MAINNET_V1 = 71402
    VT = 73799
    MVM = 73927
    RESIN = 75000
    VSCM = 77612
    TORONET = 77777
    FIRENZE = 78110
    DFLY = 78281
    AMPLIFY = 78430
    BULLETIN = 78431
    CONDUIT = 78432
    STANDT = 79879
    MATICMUM = 80001
    AMANATEST = 81341
    AMANAMIX = 81342
    AMANAPRIV = 81343
    FLANATEST = 81351
    FLANAMIX = 81352
    FLANAPRIV = 81353
    MIZANATEST = 81361
    MIZANAMIX = 81362
    MIZANAPRIV = 81363
    QNET = 81720
    BASEGOR = 84531
    AERIE = 84886
    CYBER = 85449
    NAUTTEST = 88002
    CHZ = 88880
    IVAR = 88888
    BVHL = 90210
    NAUT = 91002
    LAMBDA_TESTNET = 92001
    MANTIS = 96970
    BOBABNBOLD = 97288
    ELT = 99099
    USCTEST = 99998
    USC = 99999
    QKC_R = 100000
    QKC_S0 = 100001
    QKC_S1 = 100002
    QKC_S2 = 100003
    QKC_S3 = 100004
    QKC_S4 = 100005
    QKC_S5 = 100006
    QKC_S6 = 100007
    QKC_S7 = 100008
    VECHAIN = 100009
    VECHAIN_TESTNET = 100010
    CHI1 = 100100
    SVRNT = 101010
    CRFI = 103090
    BRO = 108801
    QKC_D_R = 110000
    QKC_D_S0 = 110001
    QKC_D_S1 = 110002
    QKC_D_S2 = 110003
    QKC_D_S3 = 110004
    QKC_D_S4 = 110005
    QKC_D_S5 = 110006
    QKC_D_S6 = 110007
    QKC_D_S7 = 110008
    TESTSBR = 111000
    SBR = 111111
    METAO = 112358
    DADIL = 123456
    ETND = 131419
    ICPLAZA = 142857
    TAIKO_A2 = 167004
    TAIKO_L2 = 167005
    TAIKO_L3 = 167006
    TKO_JOLNIR = 167007
    CONDOR = 188881
    MILKTADA = 200101
    MILKTALGO = 200202
    AKA = 200625
    ALAYA = 201018
    ALAYADEV = 201030
    MYTH = 201804
    TDSC = 202020
    TWL_JELLIE = 202624
    PLATON = 210425
    MAS = 220315
    REAP = 221230
    REAP_TESTNET = 221231
    TAFECO = 224168
    HSKTEST = 230315
    HYM = 234666
    ATS = 246529
    ATSTAU = 246785
    SAAKURU_TESTNET = 247253
    CMP_MAINNET = 256256
    GZ_TESTNET = 266256
    EGONT = 271271
    SOCHAIN = 281121
    FILECOIN_CALIBRATION = 314159
    TC = 330844
    AVST = 333331
    OONETEST = 333666
    OONEDEV = 333777
    SPARTA = 333888
    OLYMPUS = 333999
    BITFINITY = 355113
    HAP_TESTNET = 373737
    METAL = 381931
    TAHOE = 381932
    TPBXM = 404040
    KEK = 420420
    TKEK = 420666
    ALTERIUM = 420692
    ARB_RINKEBY = 421611
    ARB_GOERLI = 421613
    ARB_SEP = 421614
    FASTEXTESTNET = 424242
    MARKR_GO = 431140
    DEXALOT_TESTNET = 432201
    DEXALOT = 432204
    WLKT = 444900
    PSEP = 471100
    OC = 474142
    CMP = 512512
    ETHF = 513100
    SCR_SEPOLIA = 534351
    SCR = 534352
    SCR_ALPHA = 534353
    SCR_PREALPHA = 534354
    SHI = 534849
    BESC = 535037
    RTH = 622277
    BRNKC = 641230
    ALL = 651940
    VPIONEER = 666666
    BRNKCTEST = 751230
    MIEXS = 761412
    OCTA = 800001
    CURVEM = 827431
    BLOQS4GOOD = 846000
    VISION = 888888
    PSC_S0 = 900000
    PSC_T_S0 = 910000
    PSC_D_S0 = 920000
    PSC_D_S1 = 920001
    TFNCY = 923018
    ELV = 955305
    ETHO = 1313114
    XERO = 1313500
    KINTSUGI = 1337702
    KILN = 1337802
    ZHEJIANG = 1337803
    DBK = 2021398
    PLIAN_MAINNET = 2099156
    PLATONDEV = 2203181
    PLATONDEV2 = 2206132
    FILECOIN_BUTTERFLY = 3141592
    MANTATESTNET = 3441005
    ALT_ZEROGAS = 4000003
    WORLDSCAL = 4281033
    MXC = 5167003
    IMVERSED = 5555555
    IMVERSED_TESTNET = 5555558
    SAAKURU = 7225878
    VSL = 7355310
    TQOM = 7668378
    MUSIC = 7762959
    ZORA = 7777777
    PLIAN_MAINNET_L2 = 8007736
    HAP = 8794598
    QUARIX_TESTNET = 8888881
    QUARIX = 8888888
    PLIAN_TESTNET_L2 = 10067275
    SVRNM = 10101010
    SEP = 11155111
    TPEP = 13371337
    ANDUSCHAIN_MAINNET = 14288640
    PLIAN_TESTNET = 16658437
    ILT = 18289463
    SPECTRUM = 20180430
    QKI = 20181205
    PG = 20201022
    XLON = 22052002
    EXLVOLTA = 27082017
    EXL = 27082022
    AUXI = 28945486
    FLA = 29032022
    FILECOIN_LOCAL = 31415926
    JOYS = 35855456
    MAIS = 43214913
    AQUA = 61717561
    BAKERLOO_0 = 65010000
    PICCADILLY_0 = 65100000
    TEAM = 88888888
    TOYS = 99415706
    GTH = 192837465
    KANAZAWA = 222000222
    NEONEVM_DEVNET = 245022926
    NEONEVM_MAINNET = 245022934
    NEONEVM_TESTNET = 245022940
    RAZOR = 278611351
    ONELEDGER = 311752642
    MELD = 333000333
    CALYPSO_TESTNET = 344106930
    TGTH = 356256156
    DGTH = 486217935
    NEBULA_STAGING = 503129905
    IPOS = 1122334455
    CYB = 1146703430
    HUMAN_MAINNET = 1273227453
    AURORA = 1313161554
    AURORA_TESTNET = 1313161555
    AURORA_BETANET = 1313161556
    CHAOS_TENET = 1351057110
    RPTR = 1380996178
    NEBULA_MAINNET = 1482601649
    CALYPSO_MAINNET = 1564830818
    HMY_S0 = 1666600000
    HMY_S1 = 1666600001
    HMY_S2 = 1666600002
    HMY_S3 = 1666600003
    HMY_B_S0 = 1666700000
    HMY_B_S1 = 1666700001
    HMY_PS_S0 = 1666900000
    HMY_PS_S1 = 1666900001
    HOP = 2021121117
    EUROPA = 2046399126
    A8 = 2863311531
    PIRL = 3125659152
    FRANKENSTEIN = 4216137055
    TPALM = 11297108099
    PALM = 11297108109
    ALPHABET = 111222333444
    NTT = 197710212030
    NTT_HARADEV = 197710212031
    ZENIQ = 383414847825
    IPDC = 666301171999
    MOLE = 6022140761023
    GW_TESTNET_V1_DEPRECATED = 868455272153094
