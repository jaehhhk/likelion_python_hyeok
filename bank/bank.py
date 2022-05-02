from re import search

def display_user_info(user: dict, sep: str):
  count = 0
  for key in user:
    if(count != 2):
      print(f'{key} : {user[key]} {sep}', end = '')
    else:
      print(f'{key} : {user[key]} 원', end = '')
    count += 1
  print('\n', end = '')

def check_duplication(accounts: list, account: str) -> bool:
  if account in accounts:
    return True
  else:
    return False

def del_acc(accounts: list, account: str) -> bool:
  if account in accounts:
    return False
  else:
    return True

def find_user_index(accounts: list, account: str) -> int:
  try:
    user_index = accounts.index(account)
  except ValueError:
    user_index = None
      
  # Error : users dict 내 찾는 user가 없는 경우
  if user_index == None:
    print("해당 계좌번호를 가진 사용자가 없습니다.")
    return -1
  
  return user_index


class Bank():
  def __init__(self):
    self.users = []
    self.accounts = []

  # ================= 계좌생성 method =================
  def create_account(self):
    print("======계좌개설======")
    account = input("계좌번호 : ")
    name = input("이름 : ")
    money = input("예금 : ")

    # Error : 잘못된 account 형식 전달
    while not account.isdigit():
      print("잘못된 형식의 계좌번호입니다.")
      account = input("계좌번호 : ")
    # Error : 중복된 계좌번호
    while check_duplication(self.accounts, account):
      print("이미 있는 계좌번호입니다.")
      account = input("계좌번호 : ")

    # Error : 잘못된 name 형식 전달
    while search('[0-9]', name):
      print("잘못된 형식의 이름을 전달했습니다 : 이름 내 숫자가 포함되어 있습니다.\n")
      name = input("이름 : ")

    # Error : 잘못된 deposit 형식 전달
    while not money.isdigit() or int(money) < 0:
      print("입금하신 금액이 올바르지 않습니다 : 음수 입력\n")
      money = int(input("예금 : "))

    user = {"계좌번호" : account,
            "이름" : name,
            "잔액": int(money)
            }

    self.accounts.append(account)
    self.users.append(user)
    print("##계좌개설을 완료하였습니다##")


  # =================== 입금 method ===================
  def deposit(self):
    print("======입금 하기======")
    account = input("입금하실 계좌번호를 입력해주세요 : ")
    # Error : 잘못된 account 형식 전달
    while not account.isdigit():
      print("잘못된 형식의 계좌번호입니다.")
      account = input("계좌번호 : ")

    user_index = find_user_index(self.accounts, account)
    if user_index < 0:
      return

    user = self.users[user_index]

    # 현재 사용자 정보 보여주기
    display_user_info(user, '\n')

    money = input("입금하실 금액을 입력해주세요 : ")
    # Error : 잘못된 money 입력
    while not money.isdigit() or int(money) < 0:
      print("입금하신 금액이 올바르지 않습니다.\n")
      money = input("예금 : ")
    
    user["잔액"] += int(money)
    
    # Display
    print(f'##계좌잔고: {user["잔액"]} 원##')
    print("##입금이 완료되었습니다##")
    print("================")


  # =================== 출금 method ===================
  def withdraw(self):
    print("======출금 하기======")

    account = input("출금하실 계좌번호를 입력해주세요 : ")
    # Error : 잘못된 account 형식 전달
    while not account.isdigit():
      print("잘못된 형식의 계좌번호입니다.")
      account = input("계좌번호 : ")
    
    user_index = find_user_index(self.accounts, account)
    if user_index < 0:
      return

    user = self.users[user_index]

    # 현재 사용자 정보 보여주기
    display_user_info(user, '\n')

    money = input("출금하실 금액을 입력해주세요 : ")
    # Error : 잘못된 money 입력
    while not money.isdigit() or int(money) < 0:
      print("입금하신 금액이 올바르지 않습니다 : 음수 입력\n")
      money = input("예금 : ")

    
    # Error : 계좌 내 금액보다 더 많은 돈을 출금했을 경우
    while user["잔액"] - int(money) < 0:
      print("계좌 내 금액보다 큰 값의 금액을 입력하셨습니다.")
      money = input("출금하실 잔액을 입력해주세요 : ")

    user["잔액"] -= int(money)

    # Display
    print(f'##계좌잔고: {user["잔액"]} 원##')
    print("##출금이 완료되었습니다##")
    print("================")


  # =================== 조회 method ===================  
  def inquiry(self):
    print("======전체 조회======")
    for user in self.users:
      display_user_info(user, '/ ')
    print("====================")

 # 혁이 추가기능 -> 이름 바꾸기
  def del_account(self):
    del_name = input("삭제하실 계좌번호를 입력하세요: ")

    while del_acc(self.accounts, del_name):
       print("##존재하지 않는 계좌번호 입니다##")
       del_name = input("삭제하실 계좌번호를 입력하세요: ")
    
    self.accounts.remove(del_name)

    for i in range(len(self.users)):
      if self.users[i]["계좌번호"] == del_name:
        print('##삭제를 완료하였습니다##')
        del self.users[i]