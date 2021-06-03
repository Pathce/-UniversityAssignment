class Scanner():
    def __init__(self, target_file):
        self.__target_file = target_file
        self.__token = ""
        self.__token_list = []
        self.__keyword = ["package", "is", "begin", "end", "write"]
        self.__token_dict = {
            "package": 0,    "is": 1, "begin": 2,  "end": 3,    "write": 4,
            ":=": 5,
            "+": 6,          "-": 7,  "*": 8,     "/": 9,
            "(": 10,          ")": 11,
            ";": 12,
            "ID": 13,
            "INTLIT": 14,
            "$": 15
        }

    def checkAnnotation(self, token):
        if token == "--":
            return True
        else:
            return False

    def scanFile(self):
        cnt = 0 # 토큰의 첫글자를 받으면 1로 바뀌고 토큰이 끝나면 0으로 초기화
        token_type = ""
        for token_line in self.__target_file:
            self.__token = ""   # 토큰 초기화
            for i, token in enumerate(token_line, 0):
                # 주석 검사
                if token == "-":
                    if self.checkAnnotation(token_line[i:i+2]):
                        # 이전까지 입력된 토큰이 있는 경우 토큰 리스트에 추가
                        if token:
                            if self.__token in self.__keyword:
                                token_type = self.__token
                            self.__token_list.append([self.__token_dict[token_type], self.__token])
                            self.__token = ""
                            token_type = ""
                            cnt = 0
                        break   # 주석이 맞으면 라인을 통째로 넘김

                if token == " " or token == "\n":
                    if cnt == 1:
                        if token_type == "ID" and self.__token in self.__keyword:
                            token_type = self.__token
                        self.__token_list.append([self.__token_dict[token_type], self.__token])
                        self.__token = ""
                        token_type = ""
                        cnt = 0

                # 토큰이 연산자, 괄호, 세미콜론인지 검사
                if token in ["+", "-", "*", "/", "(", ")", ";"]:
                    # 이전까지 입력된 토큰이 있는 경우 토큰 리스트에 추가
                    if self.__token and self.__token != " ":
                        if self.__token in self.__keyword:
                            token_type = self.__token
                        self.__token_list.append([self.__token_dict[token_type], self.__token])
                        self.__token = ""
                        token_type = ""
                        cnt = 0
                    self.__token_list.append([self.__token_dict[token], token])
                    
                # 토큰이 :이 오면 다음 토큰이 =이 오는지 검사
                if token == ":":
                    # 이전까지 입력된 토큰이 있는 경우 토큰 리스트에 추가
                    if self.__token and self.__token != " ":
                        if self.__token in self.__keyword:
                            token_type = self.__token
                        self.__token_list.append([self.__token_dict[token_type], self.__token])
                        self.__token = ""
                        token_type = ""
                    cnt = 2
                    self.__token += token
                if cnt == 2 and token == "=":
                    self.__token += token
                    token_type = self.__token
                    self.__token_list.append([self.__token_dict[token_type], self.__token])
                    self.__token = ""
                    token_type = ""
                    cnt = 0

                # 토큰이 정수인지 검사
                if cnt == 0 and token.isdigit():
                    cnt = 1
                    token_type = "INTLIT"
                if token_type == "INTLIT" and not token.isdigit():
                    print(f"ERROR : Invalid token {self.__token}, {token}")

                # 토큰이 문자열인지 검사
                if cnt == 0 and token.isalpha():
                    cnt = 1
                    token_type = "ID"
                if token_type == "ID" and not(token.isalpha() or token.isdigit()):
                    print(f"ERROR : Invalid token ch t : {self.__token}, t : {token}, {token_type}")

                if cnt == 1 and (token.isdigit or token.isalpha):
                    self.__token += token

        self.__token_list.append([self.__token_dict["$"], "$"])

        return self.__token_list








