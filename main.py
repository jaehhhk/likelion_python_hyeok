from bank import Bank

if __name__ == "__main__":
  bank = Bank()

  while(True):
    print("======Bank Menu=====")
    print("1. 계좌 개설")
    print("2. 입금 하기")
    print("3. 출금 하기")
    print("4. 전체 조회")
    print("5. 계좌 삭제")     # 혁이 추가기능
    print("6. 프로그램 종료")
    print("====================")

    btn = input("입력: ")
    while not btn.isdigit() or (int(btn) < 0 or int(btn) > 6) :
      print("1 ~ 6 사이 숫자를 입력해주세요.")
      btn = input("입력: ")
    
    if(btn == '6'):
      print("##프로그램을 종료합니다##")
      break
    elif(btn == '1'):
      bank.create_account()
    elif(btn == '2'):
      bank.deposit()
    elif(btn == '3'):
      bank.withdraw()
    elif(btn == '4'):
      bank.inquiry()
    elif(btn == '5'):
      bank.del_account()