# ----------------------------------
# 암호분석 2023
#
# TC20에 대한 TMTO 공격
# - 평문/암호문: 32비트, 암호키:24비트
# - 파라미터 설정: m=t=l=2^8 (mtl = 2^24)
# - 메모리(M) = m*l = 2^16
# - 계산량(T) = t*l = 2^16
# ----------------------------------

import TC20_lib as TC20
import pickle  # 변수저장
import random  # 난수생성
import copy  # deep copy


# ============================================================
# 이전에 만든 함수들
# ============================================================
# --- int(4bytes) to list 0x12345678 -> [ 0x12, 0x34, 0x56, 0x78 ]
def int2list(n):
    out_list = []
    out_list.append((n >> 24) & 0xFF)
    out_list.append((n >> 16) & 0xFF)
    out_list.append((n >> 8) & 0xFF)
    out_list.append((n) & 0xFF)

    return out_list


# --- list to int [ 0x12, 0x34, 0x56, 0x78 ] -> 0x12345678
def list2int(l):
    n = 0
    num_byte = len(l)
    for i in range(len(l)):
        n += l[i] << 8 * (num_byte - i - 1)

    return n


# - 변수를 파일에 저장하기
def save_var_to_file(var, filename):
    f = open(filename, "w+b")
    pickle.dump(var, f)
    f.close()


# - 파일에서 변수를 가져오기
def load_var_from_file(filename):
    f = open(filename, "rb")
    var = pickle.load(f)
    f.close()
    return var


# ============================================================

# --------------------------------
# 평문-암호문(32비트): PT = [*,*,*,*] --> CT = [*,*,*,*]
# 키 크기 - 공격시간을 고려하여 24비트 키로 한정함: key = [0,*,*,*]
key_bit = 24  # 키공간 24비트 key = [0,*,*,*]

# ---------------------------------
# TMTO Table: { (SP:EP) }
#   #SP = #EP = 2^8,   #chains: m = 2^8, #tables: l = 2^8

# ============================================================
# P0 : 선택평문 (공격자가 획득 가능한 암호문에 대응되는 평문)
# X_{j+1} = E(P0, X_{j})  # key bit = block size 인 경우
# X_{j+1} = R( E(P0, X_{j}) )  # R: 32비트 [*,*,*,*] -> 24비트 [0,*,*,*]
# SP = X0(Key) -> X1 -> X2 -> ... -> Xt = EP  (encryption key chain)
# ============================================================


# ------------
# 암호문(32비트)을 다음 단계 암호키(24비트)로 만드는 함수
# R: 32비트 -> 24비트
# R: [a,b,c,d] -> [0,b,c,d]
def R(ct):
    # next_key = ct
    next_key = copy.deepcopy(ct)
    next_key[0] = 0
    return next_key


# -------------
# Encryption key chain 만들기
#   SP = (24비트 랜덤키)
#   P0 = (선택평문, 고정값)
#    t = 체인의 길이
def chain_EP(SP, P0, t):
    Xj = SP
    for j in range(0, t):
        ct = TC20.TC20_Enc(P0, Xj)
        Xj = R(ct)  # next Xj (출력 암호문 32비트를 암호키 24비트로)
    return Xj


# ===========
# chain 만들기 - 확인용 화면출력 함수 (공격에는 불필요)
def chain_EP_debug_print(SP, P0, t):
    Xj = SP
    print("SP =", SP)
    for j in range(0, t):
        ct = TC20.TC20_Enc(P0, Xj)
        Xj = R(ct)  # next Xj
        print(" -> ", ct, " -> ", Xj)
    return Xj


# ===========
# chain 확인용 파일출력 함수 (공격에는 불필요)
# SP -> ... -> EP 의 모든 중간값을 출력한다. (폴더: ./debug/)
# Xj[0,*,*,*] --> ct[*,*,*,*] --> R(ct)[0,*,*,*]
def chain_EP_debug_file(SP, P0, t, chain_num, table_num):
    file_name = "deeee/TMTO-chain-" + str(table_num) + "-" + str(chain_num) + ".txt"
    f = open(file_name, "w+")
    Xj = SP
    # print('SP =', SP)
    f.write("SP = [0, %d, %d, %d] \n" % (Xj[1], Xj[2], Xj[3]))
    for j in range(0, t):
        ct = TC20.TC20_Enc(P0, Xj)
        Xj = R(ct)  # X_{j+1}
        # print('-->', ct, ' -->', Xj)
        f.write(" --> [%d, %d, %d, %d] " % (ct[0], ct[1], ct[2], ct[3]))
        f.write(" --> [%d, %d, %d, %d] \n" % (Xj[0], Xj[1], Xj[2], Xj[3]))
    f.close()
    return Xj


# --------------------------------
# TMTO 테이블 한개 만들기 (번호=ell)
# 입력:
#      P0: 선택(고정)평문
#       m: #SP (행의 개수)    m=2^8: SP1 ~ SP2^8
#       t: 체인의 길이(열)    j=0, ... , j=t
#     ell: 테이블 번호        ell = 0 ~ 255
# 출력:
#    사전    : { (Key=EP, Value=SP) }
#    저장위치: ./tmto_table/TMTO-ell.dic
def make_one_tmto_table(P0, m, t, ell):
    tmto_dic = {}  # (SP,EP), 정렬기준 EP (EP를 검색하기 위해)
    for i in range(0, m):
        # 랜덤한 시작점
        SP = [0, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        # 끝점계산 후 디버깅용 파일에 출력
        EP = chain_EP_debug_file(SP, P0, t, i, ell)
        # 디버깅용 파일이 필요없는 경우 아래를 대신 사용함
        # EP = chain_EP(SP, P0, t)

        # 정수로 만들어 (SP, EP)를 사전에 넣는다 { (Key=EP, Value=SP) }
        SP_int = list2int(SP)
        EP_int = list2int(EP)
        tmto_dic[EP_int] = SP_int
    # 만든 테이블 사전을 파일로 저장한다
    # 파일명: TMTO-0, TMTO-1, ... , TMTO-255
    file_name = "tmto_table-2/TMTO-" + str(ell) + ".dic"
    save_var_to_file(tmto_dic, file_name)


# ---------------------
# TMTO 테이블 전체 만들기
# 입력:
#   P0: 고정평문
#   m: 행(row)의 개수 (체인의 개수)
#   t: 열(col)의 개수 (체인의 길이)
#   num_of_tables: TMTO 테이블 개수 (=256)
def generate_chain(SP, P0, t):
    chain = []
    Xj = SP
    for j in range(t):
        ct = TC20.TC20_Enc(P0, Xj)
        Xj = R(ct)
        chain.append(tuple(Xj))
    return chain


def calculate_ecr(P0, m, t, num_of_tables):
    print("Calculating ECR values for each table...")
    for ell in range(num_of_tables):
        unique_keys = set()
        for i in range(m):
            SP = [0, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            chain = generate_chain(SP, P0, t)
            unique_keys.update(chain)

        ecr = len(unique_keys) / (m * t)
        print("Table %d: ECR = %f" % (ell, ecr))
        print(".", end="")
    print("\n All TMTO tables are created.")


def make_all_tmto_tables(P0, m, t, num_of_tables):
    print("making TMTO tables", end="")
    calculate_ecr(P0, m, t, num_of_tables)


# Test Run

# random.seed(1234)  #고정된 seed --> 항상 같은 결과(랜덤)
random.seed(2023)  # 고정된 seed --> 항상 같은 결과(랜덤)

# SP = [0,1,2,3]  # 시작점

# 선택평문 (TMTO 테이블 전체에서 고정된 값으로 사용)
P0 = [1, 2, 3, 4]
# 공격 파라미터 설정
m = 256  # m: 한 테이블에 들어가는 체인의 개수
t = 256  # t: 체인의 길이
num_of_tables = 256  # 테이블 개수

# =====================
# (단계1) TMTO 테이블 만들기 (Pre-computation)
# 이 과정이 끝나면 테이블이 사전으로 저장됨
# num_of_tables에 설정한 개수만큼 사전파일이 생김(TMTO-0, TMTO-1, ...)
# =====================
make_all_tmto_tables(P0, m, t, num_of_tables)
